# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Mar 17 22:47:14 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(928, 490)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.fileButton = QtGui.QPushButton(self.centralWidget)
        self.fileButton.setObjectName("fileButton")
        self.verticalLayout.addWidget(self.fileButton)
        self.filenameLabel = QtGui.QLabel(self.centralWidget)
        self.filenameLabel.setText("")
        self.filenameLabel.setObjectName("filenameLabel")
        self.verticalLayout.addWidget(self.filenameLabel)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.minEntry = QtGui.QSpinBox(self.centralWidget)
        self.minEntry.setObjectName("minEntry")
        self.verticalLayout.addWidget(self.minEntry)
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.maxEntry = QtGui.QSpinBox(self.centralWidget)
        self.maxEntry.setObjectName("maxEntry")
        self.verticalLayout.addWidget(self.maxEntry)
        self.findPeakButton = QtGui.QPushButton(self.centralWidget)
        self.findPeakButton.setObjectName("findPeakButton")
        self.verticalLayout.addWidget(self.findPeakButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.canvasLayout = QtGui.QHBoxLayout()
        self.canvasLayout.setObjectName("canvasLayout")
        self.horizontalLayout_2.addLayout(self.canvasLayout)
        self.rightLayout = QtGui.QVBoxLayout()
        self.rightLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.rightLayout.setObjectName("rightLayout")
        self.peaksText = QtGui.QPlainTextEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peaksText.sizePolicy().hasHeightForWidth())
        self.peaksText.setSizePolicy(sizePolicy)
        self.peaksText.setMinimumSize(QtCore.QSize(200, 0))
        self.peaksText.setObjectName("peaksText")
        self.rightLayout.addWidget(self.peaksText)
        self.saveButton = QtGui.QPushButton(self.centralWidget)
        self.saveButton.setObjectName("saveButton")
        self.rightLayout.addWidget(self.saveButton)
        self.horizontalLayout_2.addLayout(self.rightLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Signal peak", None, QtGui.QApplication.UnicodeUTF8))
        self.fileButton.setText(QtGui.QApplication.translate("MainWindow", "Open file...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Min width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Max width", None, QtGui.QApplication.UnicodeUTF8))
        self.findPeakButton.setText(QtGui.QApplication.translate("MainWindow", "I\'m so late find them! ", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("MainWindow", "Save...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open...", None, QtGui.QApplication.UnicodeUTF8))

