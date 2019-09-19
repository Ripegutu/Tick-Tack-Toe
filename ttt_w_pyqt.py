# Trying to make ttt with the use of QTPY

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arrows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 606)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.down_arrow = QtWidgets.QToolButton(self.centralwidget)
        self.down_arrow.setGeometry(QtCore.QRect(291, 290, 27, 26))
        self.down_arrow.setArrowType(QtCore.Qt.DownArrow)
        self.down_arrow.setObjectName("down_arrow")
        self.up_arrow = QtWidgets.QToolButton(self.centralwidget)
        self.up_arrow.setGeometry(QtCore.QRect(291, 211, 27, 26))
        self.up_arrow.setArrowType(QtCore.Qt.UpArrow)
        self.up_arrow.setObjectName("up_arrow")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(170, 180, 22, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(270, 250, 63, 28))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_arrow = QtWidgets.QToolButton(self.widget)
        self.left_arrow.setArrowType(QtCore.Qt.LeftArrow)
        self.left_arrow.setObjectName("left_arrow")
        self.horizontalLayout.addWidget(self.left_arrow)
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.down_arrow.setText(_translate("MainWindow", "..."))
        self.up_arrow.setText(_translate("MainWindow", "..."))
        self.left_arrow.setText(_translate("MainWindow", "..."))
        self.toolButton.setText(_translate("MainWindow", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

