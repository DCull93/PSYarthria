# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Duncan Cull\Documents\PySideUI\UIv2.ui'
#
# Created: Wed Apr 13 15:02:47 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 442)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.widget.setObjectName("widget")
        self.btn_Pron_HeShe = QtGui.QPushButton(self.widget)
        self.btn_Pron_HeShe.setGeometry(QtCore.QRect(70, 310, 71, 61))
        self.btn_Pron_HeShe.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black")
        self.btn_Pron_HeShe.setObjectName("btn_Pron_HeShe")
        self.btn_Cmn_No = QtGui.QPushButton(self.widget)
        self.btn_Cmn_No.setGeometry(QtCore.QRect(210, 70, 71, 61))
        self.btn_Cmn_No.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid black")
        self.btn_Cmn_No.setObjectName("btn_Cmn_No")
        self.btn_Verb_Look = QtGui.QPushButton(self.widget)
        self.btn_Verb_Look.setGeometry(QtCore.QRect(210, 190, 71, 61))
        self.btn_Verb_Look.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Look.setObjectName("btn_Verb_Look")
        self.btn_Clear = QtGui.QPushButton(self.widget)
        self.btn_Clear.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_Clear.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.btn_Clear.setObjectName("btn_Clear")
        self.btn_Verb_Hear = QtGui.QPushButton(self.widget)
        self.btn_Verb_Hear.setGeometry(QtCore.QRect(280, 190, 71, 61))
        self.btn_Verb_Hear.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Hear.setObjectName("btn_Verb_Hear")
        self.btn_Cmn_Time = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Time.setGeometry(QtCore.QRect(0, 130, 71, 61))
        self.btn_Cmn_Time.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(255, 170, 0);")
        self.btn_Cmn_Time.setObjectName("btn_Cmn_Time")
        self.btn_Nouns = QtGui.QPushButton(self.widget)
        self.btn_Nouns.setGeometry(QtCore.QRect(280, 10, 71, 61))
        self.btn_Nouns.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(208, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_Nouns.setObjectName("btn_Nouns")
        self.btn_Verb_Go = QtGui.QPushButton(self.widget)
        self.btn_Verb_Go.setGeometry(QtCore.QRect(280, 250, 71, 61))
        self.btn_Verb_Go.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Go.setObjectName("btn_Verb_Go")
        self.btn_Cmn_Not = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Not.setGeometry(QtCore.QRect(280, 70, 71, 61))
        self.btn_Cmn_Not.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid black")
        self.btn_Cmn_Not.setObjectName("btn_Cmn_Not")
        self.btn_Pron_I = QtGui.QPushButton(self.widget)
        self.btn_Pron_I.setGeometry(QtCore.QRect(0, 250, 71, 61))
        self.btn_Pron_I.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border: 1px solid black;\n"
"color: rgb(255, 255, 255);")
        self.btn_Pron_I.setObjectName("btn_Pron_I")
        self.btn_Cmn_Good = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Good.setGeometry(QtCore.QRect(350, 70, 71, 61))
        self.btn_Cmn_Good.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid black")
        self.btn_Cmn_Good.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Pictures/WDF_2613889.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Cmn_Good.setIcon(icon)
        self.btn_Cmn_Good.setObjectName("btn_Cmn_Good")
        self.btn_Pron_They = QtGui.QPushButton(self.widget)
        self.btn_Pron_They.setGeometry(QtCore.QRect(70, 250, 71, 61))
        self.btn_Pron_They.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border: 1px solid black;\n"
"color: rgb(255, 255, 255);")
        self.btn_Pron_They.setObjectName("btn_Pron_They")
        self.btn_Verb_Dislike = QtGui.QPushButton(self.widget)
        self.btn_Verb_Dislike.setGeometry(QtCore.QRect(350, 250, 71, 61))
        self.btn_Verb_Dislike.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Dislike.setObjectName("btn_Verb_Dislike")
        self.btn_Cmn_Bad = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Bad.setGeometry(QtCore.QRect(350, 130, 71, 61))
        self.btn_Cmn_Bad.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid black")
        self.btn_Cmn_Bad.setObjectName("btn_Cmn_Bad")
        self.btn_Pron_It = QtGui.QPushButton(self.widget)
        self.btn_Pron_It.setGeometry(QtCore.QRect(0, 310, 71, 61))
        self.btn_Pron_It.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black\n"
"")
        self.btn_Pron_It.setObjectName("btn_Pron_It")
        self.btn_Cmn_Yes = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Yes.setGeometry(QtCore.QRect(140, 70, 71, 61))
        self.btn_Cmn_Yes.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid black\n"
"")
        self.btn_Cmn_Yes.setObjectName("btn_Cmn_Yes")
        self.btn_Cmn_Hello = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Hello.setGeometry(QtCore.QRect(0, 70, 71, 61))
        self.btn_Cmn_Hello.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(255, 170, 0);")
        self.btn_Cmn_Hello.setObjectName("btn_Cmn_Hello")
        self.btn_Verb_Do = QtGui.QPushButton(self.widget)
        self.btn_Verb_Do.setGeometry(QtCore.QRect(210, 250, 71, 61))
        self.btn_Verb_Do.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Do.setObjectName("btn_Verb_Do")
        self.btn_Pron_Mine = QtGui.QPushButton(self.widget)
        self.btn_Pron_Mine.setGeometry(QtCore.QRect(140, 310, 71, 61))
        self.btn_Pron_Mine.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black")
        self.btn_Pron_Mine.setObjectName("btn_Pron_Mine")
        self.btn_Cmn_Feeling = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Feeling.setGeometry(QtCore.QRect(140, 130, 71, 61))
        self.btn_Cmn_Feeling.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid black")
        self.btn_Cmn_Feeling.setObjectName("btn_Cmn_Feeling")
        self.btn_Verb_Like = QtGui.QPushButton(self.widget)
        self.btn_Verb_Like.setGeometry(QtCore.QRect(350, 190, 71, 61))
        self.btn_Verb_Like.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Like.setObjectName("btn_Verb_Like")
        self.btn_Cmn_Colours = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Colours.setGeometry(QtCore.QRect(420, 70, 71, 61))
        self.btn_Cmn_Colours.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border: 1px solid black")
        self.btn_Cmn_Colours.setObjectName("btn_Cmn_Colours")
        self.btn_Pron_People = QtGui.QPushButton(self.widget)
        self.btn_Pron_People.setGeometry(QtCore.QRect(70, 190, 71, 61))
        self.btn_Pron_People.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border: 1px solid black;\n"
"color: rgb(255, 255, 255);")
        self.btn_Pron_People.setObjectName("btn_Pron_People")
        self.btn_Pronoun_You = QtGui.QPushButton(self.widget)
        self.btn_Pronoun_You.setGeometry(QtCore.QRect(0, 190, 71, 61))
        self.btn_Pronoun_You.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border: 1px solid black;\n"
"color: rgb(255, 255, 255);")
        self.btn_Pronoun_You.setObjectName("btn_Pronoun_You")
        self.btn_Translation = QtGui.QPushButton(self.widget)
        self.btn_Translation.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_Translation.setStyleSheet("border: 1px solid black;\n"
"selection-color: rgb(255, 255, 0);")
        self.btn_Translation.setObjectName("btn_Translation")
        self.btn_Cmn_IDK = QtGui.QPushButton(self.widget)
        self.btn_Cmn_IDK.setGeometry(QtCore.QRect(280, 130, 71, 61))
        self.btn_Cmn_IDK.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid black")
        self.btn_Cmn_IDK.setObjectName("btn_Cmn_IDK")
        self.btn_Verb_Eat = QtGui.QPushButton(self.widget)
        self.btn_Verb_Eat.setGeometry(QtCore.QRect(280, 310, 71, 61))
        self.btn_Verb_Eat.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Eat.setObjectName("btn_Verb_Eat")
        self.btn_Cmn_Goodbye = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Goodbye.setGeometry(QtCore.QRect(70, 70, 71, 61))
        self.btn_Cmn_Goodbye.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(255, 170, 0);")
        self.btn_Cmn_Goodbye.setObjectName("btn_Cmn_Goodbye")
        self.btn_Is = QtGui.QPushButton(self.widget)
        self.btn_Is.setGeometry(QtCore.QRect(210, 10, 71, 61))
        self.btn_Is.setStyleSheet("border: 1px solid black")
        self.btn_Is.setObjectName("btn_Is")
        self.btn_Pron_We = QtGui.QPushButton(self.widget)
        self.btn_Pron_We.setGeometry(QtCore.QRect(140, 190, 71, 61))
        self.btn_Pron_We.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border: 1px solid black;\n"
"color: rgb(255, 255, 255);")
        self.btn_Pron_We.setObjectName("btn_Pron_We")
        self.btn_Questions = QtGui.QPushButton(self.widget)
        self.btn_Questions.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_Questions.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.btn_Questions.setObjectName("btn_Questions")
        self.btn_Verb_Wear = QtGui.QPushButton(self.widget)
        self.btn_Verb_Wear.setGeometry(QtCore.QRect(420, 250, 71, 61))
        self.btn_Verb_Wear.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);\n"
"")
        self.btn_Verb_Wear.setObjectName("btn_Verb_Wear")
        self.btn_Verb_Come = QtGui.QPushButton(self.widget)
        self.btn_Verb_Come.setGeometry(QtCore.QRect(420, 190, 71, 61))
        self.btn_Verb_Come.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Come.setObjectName("btn_Verb_Come")
        self.btn_Menu = QtGui.QPushButton(self.widget)
        self.btn_Menu.setGeometry(QtCore.QRect(420, 10, 71, 61))
        self.btn_Menu.setStyleSheet("border: 1px solid black")
        self.btn_Menu.setObjectName("btn_Menu")
        self.btn_Pron_Me = QtGui.QPushButton(self.widget)
        self.btn_Pron_Me.setGeometry(QtCore.QRect(140, 250, 71, 61))
        self.btn_Pron_Me.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black")
        self.btn_Pron_Me.setObjectName("btn_Pron_Me")
        self.btn_Verb_Drink = QtGui.QPushButton(self.widget)
        self.btn_Verb_Drink.setGeometry(QtCore.QRect(350, 310, 71, 61))
        self.btn_Verb_Drink.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Drink.setObjectName("btn_Verb_Drink")
        self.btn_Cmn_Hungry = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Hungry.setGeometry(QtCore.QRect(70, 130, 71, 61))
        self.btn_Cmn_Hungry.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(255, 170, 0);")
        self.btn_Cmn_Hungry.setObjectName("btn_Cmn_Hungry")
        self.btn_Verb_Want = QtGui.QPushButton(self.widget)
        self.btn_Verb_Want.setGeometry(QtCore.QRect(210, 310, 71, 61))
        self.btn_Verb_Want.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Want.setObjectName("btn_Verb_Want")
        self.btn_Language = QtGui.QPushButton(self.widget)
        self.btn_Language.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_Language.setStyleSheet("border: 1px solid black")
        self.btn_Language.setObjectName("btn_Language")
        self.btn_Cmn_Howareyou = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Howareyou.setGeometry(QtCore.QRect(210, 130, 71, 61))
        self.btn_Cmn_Howareyou.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(255, 170, 0);")
        self.btn_Cmn_Howareyou.setObjectName("btn_Cmn_Howareyou")
        self.btn_Cmn_Sizes = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Sizes.setGeometry(QtCore.QRect(420, 130, 71, 61))
        self.btn_Cmn_Sizes.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border: 1px solid black")
        self.btn_Cmn_Sizes.setObjectName("btn_Cmn_Sizes")
        self.btn_Plural = QtGui.QPushButton(self.widget)
        self.btn_Plural.setGeometry(QtCore.QRect(350, 10, 71, 61))
        self.btn_Plural.setStyleSheet("border: 1px solid black")
        self.btn_Plural.setObjectName("btn_Plural")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 491, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SentenceBuilder = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.SentenceBuilder.setText("")
        self.SentenceBuilder.setObjectName("SentenceBuilder")
        self.horizontalLayout.addWidget(self.SentenceBuilder)
        self.btn_Speak = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_Speak.setObjectName("btn_Speak")
        self.horizontalLayout.addWidget(self.btn_Speak)
        self.btn_translation_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_translation_2.setObjectName("btn_translation_2")
        self.horizontalLayout.addWidget(self.btn_translation_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_HeShe.setText(QtGui.QApplication.translate("MainWindow", "He/She", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_No.setText(QtGui.QApplication.translate("MainWindow", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Look.setText(QtGui.QApplication.translate("MainWindow", "See", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Clear.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Hear.setText(QtGui.QApplication.translate("MainWindow", "Hear", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Time.setText(QtGui.QApplication.translate("MainWindow", "What time \n"
" is it?", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Nouns.setText(QtGui.QApplication.translate("MainWindow", "Nouns", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Go.setText(QtGui.QApplication.translate("MainWindow", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Not.setText(QtGui.QApplication.translate("MainWindow", "Not", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_I.setText(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_They.setText(QtGui.QApplication.translate("MainWindow", "They", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Dislike.setText(QtGui.QApplication.translate("MainWindow", "Dislike", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Bad.setText(QtGui.QApplication.translate("MainWindow", "Bad :(", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_It.setText(QtGui.QApplication.translate("MainWindow", "It", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Yes.setText(QtGui.QApplication.translate("MainWindow", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Hello.setText(QtGui.QApplication.translate("MainWindow", "Hello", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Do.setText(QtGui.QApplication.translate("MainWindow", "Do", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_Mine.setText(QtGui.QApplication.translate("MainWindow", "Mine", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Feeling.setText(QtGui.QApplication.translate("MainWindow", "I\'m feeling...", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Like.setText(QtGui.QApplication.translate("MainWindow", "Like", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Colours.setText(QtGui.QApplication.translate("MainWindow", "Colours", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_People.setText(QtGui.QApplication.translate("MainWindow", "People", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pronoun_You.setText(QtGui.QApplication.translate("MainWindow", "You", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Translation.setText(QtGui.QApplication.translate("MainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_IDK.setText(QtGui.QApplication.translate("MainWindow", "I don\'t know", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Eat.setText(QtGui.QApplication.translate("MainWindow", "Eat", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Goodbye.setText(QtGui.QApplication.translate("MainWindow", "Goodbye", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Is.setText(QtGui.QApplication.translate("MainWindow", "is/were/was\n"
"/are \n"
"(+negatives)", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_We.setText(QtGui.QApplication.translate("MainWindow", "We", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Questions.setText(QtGui.QApplication.translate("MainWindow", "Questions \n"
" ?", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Wear.setText(QtGui.QApplication.translate("MainWindow", "Wear", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Come.setText(QtGui.QApplication.translate("MainWindow", "Come", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Menu.setText(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_Me.setText(QtGui.QApplication.translate("MainWindow", "Me", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Drink.setText(QtGui.QApplication.translate("MainWindow", "Drink", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Hungry.setText(QtGui.QApplication.translate("MainWindow", "I\'m hungry", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Want.setText(QtGui.QApplication.translate("MainWindow", "Want", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Language.setText(QtGui.QApplication.translate("MainWindow", "Language", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Howareyou.setText(QtGui.QApplication.translate("MainWindow", "How are\n"
" you?", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Sizes.setText(QtGui.QApplication.translate("MainWindow", "Sizes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Plural.setText(QtGui.QApplication.translate("MainWindow", "Plural (+s)", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Speak.setText(QtGui.QApplication.translate("MainWindow", "Speak", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_translation_2.setText(QtGui.QApplication.translate("MainWindow", "Delete \n"
" Word", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

