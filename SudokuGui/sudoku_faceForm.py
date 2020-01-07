# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sudoku_faceForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(510, 15, 251, 21))
        self.time.setObjectName("time")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 451, 451))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.Level_state = QtWidgets.QLineEdit(self.centralwidget)
        self.Level_state.setGeometry(QtCore.QRect(510, 80, 61, 31))
        self.Level_state.setObjectName("Level_state")
        self.surplus = QtWidgets.QLineEdit(self.centralwidget)
        self.surplus.setGeometry(QtCore.QRect(680, 80, 61, 31))
        self.surplus.setObjectName("surplus")
        self.Check_state = QtWidgets.QLabel(self.centralwidget)
        self.Check_state.setGeometry(QtCore.QRect(501, 144, 271, 191))
        self.Check_state.setObjectName("Check_state")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(500, 380, 93, 28))
        self.start.setObjectName("start")
        self.Ok = QtWidgets.QPushButton(self.centralwidget)
        self.Ok.setGeometry(QtCore.QRect(640, 380, 93, 28))
        self.Ok.setObjectName("Ok")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuLevel = QtWidgets.QMenu(self.menubar)
        self.menuLevel.setObjectName("menuLevel")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEasy = QtWidgets.QAction(MainWindow)
        self.actionEasy.setObjectName("actionEasy")
        self.actionMedium = QtWidgets.QAction(MainWindow)
        self.actionMedium.setObjectName("actionMedium")
        self.actionHard = QtWidgets.QAction(MainWindow)
        self.actionHard.setObjectName("actionHard")
        self.menuLevel.addAction(self.actionEasy)
        self.menuLevel.addAction(self.actionMedium)
        self.menuLevel.addAction(self.actionHard)
        self.menubar.addAction(self.menuLevel.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.time.setText(_translate("MainWindow", "TextLabel"))
        self.tableWidget.setSortingEnabled(False)
        self.Check_state.setText(_translate("MainWindow", "TextLabel"))
        self.start.setText(_translate("MainWindow", "PushButton"))
        self.Ok.setText(_translate("MainWindow", "PushButton"))
        self.menuLevel.setTitle(_translate("MainWindow", "Level"))
        self.actionEasy.setText(_translate("MainWindow", "Easy"))
        self.actionMedium.setText(_translate("MainWindow", "Medium"))
        self.actionHard.setText(_translate("MainWindow", "Hard"))
