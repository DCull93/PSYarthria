# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Duncan Cull\Documents\PySideUI\QuList.ui'
#
# Created: Wed Apr 13 15:24:36 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_QuList(object):
    def setupUi(self, QuList):
        QuList.setObjectName("QuList")
        QuList.resize(494, 390)
        self.btn_What = QtGui.QPushButton(QuList)
        self.btn_What.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.btn_What.setStyleSheet("border: 1px solid black;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 255);\n"
"selection-color: rgb(255, 255, 0);")
        self.btn_What.setObjectName("btn_What")
        self.btn_Where = QtGui.QPushButton(QuList)
        self.btn_Where.setGeometry(QtCore.QRect(80, 10, 71, 61))
        self.btn_Where.setStyleSheet("border: 1px solid black;\n"
"selection-color: rgb(255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 255);")
        self.btn_Where.setObjectName("btn_Where")
        self.btn_Which = QtGui.QPushButton(QuList)
        self.btn_Which.setGeometry(QtCore.QRect(10, 70, 71, 61))
        self.btn_Which.setStyleSheet("border: 1px solid black;\n"
"selection-color: rgb(255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 255);")
        self.btn_Which.setObjectName("btn_Which")
        self.btn_Who = QtGui.QPushButton(QuList)
        self.btn_Who.setGeometry(QtCore.QRect(150, 10, 71, 61))
        self.btn_Who.setStyleSheet("border: 1px solid black;\n"
"selection-color: rgb(255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 255);")
        self.btn_Who.setObjectName("btn_Who")
        self.btn_When = QtGui.QPushButton(QuList)
        self.btn_When.setGeometry(QtCore.QRect(150, 70, 71, 61))
        self.btn_When.setStyleSheet("border: 1px solid black;\n"
"selection-color: rgb(255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 255);")
        self.btn_When.setObjectName("btn_When")
        self.btn_Translation_6 = QtGui.QPushButton(QuList)
        self.btn_Translation_6.setGeometry(QtCore.QRect(80, 70, 71, 61))
        self.btn_Translation_6.setStyleSheet("border: 1px solid black;\n"
"selection-color: rgb(255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 255);")
        self.btn_Translation_6.setObjectName("btn_Translation_6")

        self.retranslateUi(QuList)
        QtCore.QMetaObject.connectSlotsByName(QuList)

    def retranslateUi(self, QuList):
        QuList.setWindowTitle(QtGui.QApplication.translate("QuList", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_What.setText(QtGui.QApplication.translate("QuList", "What", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Where.setText(QtGui.QApplication.translate("QuList", "Where", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Which.setText(QtGui.QApplication.translate("QuList", "Which", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Who.setText(QtGui.QApplication.translate("QuList", "Who", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_When.setText(QtGui.QApplication.translate("QuList", "When", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Translation_6.setText(QtGui.QApplication.translate("QuList", "How", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    QuList = QtGui.QWidget()
    ui = Ui_QuList()
    ui.setupUi(QuList)
    QuList.show()
    sys.exit(app.exec_())

