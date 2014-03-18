#!/usr/bin/env python

import logging
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING)

import os, sys
try:
    from PySide import QtCore, QtGui, QtUiTools
except ImportError:
    print "Could not load PySide (Qt) librairies, exiting."
    sys.exit(1)

import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from scipy.signal import find_peaks_cwt
import numpy as np

from mainwindow import Ui_MainWindow



class MainWindow(QtGui.QMainWindow):
    def __init__(self, peaks, *args):
        self.peaks = peaks

        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.findPeakButton.clicked.connect(self.findPeaksCallback)
        self.ui.fileButton.clicked.connect(self.loadFileCallback)
        self.ui.saveButton.clicked.connect(self.savePeaksCallback)

    def addPlot(self):
        self.fig = Figure(figsize=(600, 600), dpi=72, facecolor=(1,1,1), edgecolor=(0,0,0))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.ui.canvasLayout.addWidget(self.canvas)


        self.navi_toolbar = NavigationToolbar(self.canvas, self)
        self.ui.canvasLayout.addWidget(self.navi_toolbar)


    def loadFileCallback(self):
        filename, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open data file',)

        if filename:
            self.peaks.load(filename)
            self.update()

            self.ui.filenameLabel.setText("File: %s" % os.path.split(filename)[-1])
            self.ui.statusBar.showMessage("File opened: %s" % os.path.split(filename)[-1])

    def findPeaksCallback(self):
        self.peaks.setMinMax( int(self.ui.minEntry.text()), int(self.ui.maxEntry.text()) )
        self.ui.statusBar.showMessage("Calculating peaks")
        self.peaks.findPeaks()
        self.update()
        self.ui.statusBar.showMessage("Calculation done")

    def savePeaksCallback(self):
        filename, _ = QtGui.QFileDialog.getSaveFileName(self, 'Save peaks to',)
        if filename:
            with open(filename, 'w') as f:
                f.write(self.ui.peaksText.toPlainText())

            self.ui.statusBar.showMessage("Peaks saved to: %s" % os.path.split(filename)[-1])

    def update(self):
        self.ax.cla()

        self.ax.plot(self.peaks.x, self.peaks.y)
        if self.peaks.peaks:
            self.ax.plot(self.peaks.peaks, [self.peaks.y[i] for i in self.peaks.peaks], 'ro')

            self.ui.peaksText.setPlainText("\n".join(["%s; %s" % (p, v) for p, v in zip(self.peaks.peaks, [self.peaks.y[i] for i in self.peaks.peaks])]))

        self.canvas.draw()


class peaksFinder(object):
    def __init__(self, filename=None):
        if filename:
            self.load(filename)

        self.minWidth = 1
        self.maxWidth = 10

    def load(self, filename):
        with open(filename) as fp:
            raw = fp.readlines()
            self.data = [(float(l.strip().split('\t')[0]), float(l.strip().split('\t')[1])) for l in raw]

        self.x = [row[0] for row in self.data]
        self.y = [row[1] for row in self.data]

        self.peaks = None

    def setMinMax(self, min=None, max=None):
        if min:
            self.minWidth = min
        if max:
            self.maxWidth = max

    def findPeaks(self):
        self.peaks = find_peaks_cwt(self.y, np.arange(self.minWidth, self.maxWidth))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.connect(app, QtCore.SIGNAL("lastWindowClosed()"),
                app, QtCore.SLOT("quit()"))

    peaks = peaksFinder()

    win = MainWindow(peaks)
    win.addPlot()
    
    win.show()

    sys.exit(app.exec_())

