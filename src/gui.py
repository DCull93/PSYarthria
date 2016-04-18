import sys
from configureSet import *
from updater import *
from PySide import QtCore, QtGui

class Ui_MainWindow(object):

    def __init__(self):
        """ Initialise instances and structures """
        self.config = Config()
        self.phraseList = []
        self.verbList = []

    def setupUi(self, MainWindow):
        """ Sets main window and central widget up """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(491, 500)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 50, 491, 491))
        self.widget.setObjectName("widget")

        self.btn_Language = QtGui.QPushButton(self.widget)
        self.btn_Language.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_Language.setStyleSheet("border: 1px solid black")
        self.btn_Language.setObjectName("btn_Language")

                """ >>>>>Duncan's Gui Code<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< """

        """ >>>>>>>>>>Pronoun buttons<<<<<<<<<<< """

        self.btn_Pron_She = QtGui.QPushButton(self.widget)
        self.btn_Pron_She.setGeometry(QtCore.QRect(70, 310, 71, 61))
        self.btn_Pron_She.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black")
        self.btn_Pron_She.setObjectName("btn_Pron_She")
        self.btn_Pron_She.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Pron_She.text() + " "))

        self.btn_Pron_I = QtGui.QPushButton(self.widget)
        self.btn_Pron_I.setGeometry(QtCore.QRect(0, 250, 71, 61))
        self.btn_Pron_I.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border: 1px solid black;\n"
"color: rgb(255, 255, 255);")
        self.btn_Pron_I.setObjectName("btn_Pron_I")
        self.btn_Pron_I.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Pron_I.text() + " "))

        self.btn_Pron_They = QtGui.QPushButton(self.widget)
        self.btn_Pron_They.setGeometry(QtCore.QRect(70, 250, 71, 61))
        self.btn_Pron_They.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border: 1px solid black;\n"
"color: rgb(255, 255, 255);")
        self.btn_Pron_They.setObjectName("btn_Pron_They")
        self.btn_Pron_They.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Pron_They.text() + " "))

        self.btn_Pron_Mine = QtGui.QPushButton(self.widget)
        self.btn_Pron_Mine.setGeometry(QtCore.QRect(140, 310, 71, 61))
        self.btn_Pron_Mine.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black")
        self.btn_Pron_Mine.setObjectName("btn_Pron_Mine")
        self.btn_Pron_Mine.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Pron_Mine.text() + " "))

        self.btn_Pron_People = QtGui.QPushButton(self.widget)
        self.btn_Pron_People.setGeometry(QtCore.QRect(70, 190, 71, 61))
        self.btn_Pron_People.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border: 1px solid black;\n"
"color: rgb(255, 255, 255);")
        self.btn_Pron_People.setObjectName("btn_Pron_People")
        self.btn_Pron_People.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Pron_People.text() + " "))

        self.btn_Pron_You = QtGui.QPushButton(self.widget)
        self.btn_Pron_You.setGeometry(QtCore.QRect(0, 190, 71, 61))
        self.btn_Pron_You.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border: 1px solid black;\n"
"color: rgb(255, 255, 255);")
        self.btn_Pron_You.setObjectName("btn_Pron_You")
        self.btn_Pron_You.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Pron_You.text() + " "))

        self.btn_Pron_We = QtGui.QPushButton(self.widget)
        self.btn_Pron_We.setGeometry(QtCore.QRect(140, 190, 71, 61))
        self.btn_Pron_We.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border: 1px solid black;\n"
"color: rgb(255, 255, 255);")
        self.btn_Pron_We.setObjectName("btn_Pron_We")
        self.btn_Pron_We.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Pron_We.text() + " "))

        self.btn_Pron_He = QtGui.QPushButton(self.widget)
        self.btn_Pron_He.setGeometry(QtCore.QRect(140, 250, 71, 61))
        self.btn_Pron_He.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black")
        self.btn_Pron_He.setObjectName("btn_Pron_Me")
        self.btn_Pron_He.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Pron_He.text() + " "))

        self.btn_Pron_It = QtGui.QPushButton(self.widget)
        self.btn_Pron_It.setGeometry(QtCore.QRect(0, 310, 71, 61))
        self.btn_Pron_It.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black")
        self.btn_Pron_It.setObjectName("btn_Pron_It")
        self.btn_Pron_It.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Pron_It.text() + " "))

        """>>>>>>>>>>Common Word or Phrase buttons<<<<<<<<<<"""

        self.btn_Cmn_No = QtGui.QPushButton(self.widget)
        self.btn_Cmn_No.setGeometry(QtCore.QRect(210, 70, 71, 61))
        self.btn_Cmn_No.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid black")
        self.btn_Cmn_No.setObjectName("btn_Cmn_No")
        self.btn_Cmn_No.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Cmn_No.text() + " "))

        self.btn_Cmn_Time = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Time.setGeometry(QtCore.QRect(0, 130, 71, 61))
        self.btn_Cmn_Time.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(255, 170, 0);")
        self.btn_Cmn_Time.setObjectName("btn_Cmn_Time")
        self.btn_Cmn_Time.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Cmn_Time.text() + " "))

        self.btn_Cmn_Good = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Good.setGeometry(QtCore.QRect(350, 70, 71, 61))
        self.btn_Cmn_Good.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid black")
        self.btn_Cmn_Good.setText("Good")
        self.btn_Cmn_Good.setObjectName("btn_Cmn_Good")
        self.btn_Cmn_Good.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Cmn_Good.text() + " "))

        self.btn_Cmn_Bad = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Bad.setGeometry(QtCore.QRect(350, 130, 71, 61))
        self.btn_Cmn_Bad.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid black")
        self.btn_Cmn_Bad.setObjectName("btn_Cmn_Bad")
        self.btn_Cmn_Bad.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Cmn_Bad.text() + " "))

        self.btn_Cmn_Yes = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Yes.setGeometry(QtCore.QRect(140, 70, 71, 61))
        self.btn_Cmn_Yes.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid black")
        self.btn_Cmn_Yes.setObjectName("btn_Cmn_Yes")
        self.btn_Cmn_Yes.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Cmn_Yes.text() + " "))

        self.btn_Cmn_Hello = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Hello.setGeometry(QtCore.QRect(0, 70, 71, 61))
        self.btn_Cmn_Hello.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(255, 170, 0);")
        self.btn_Cmn_Hello.setObjectName("btn_Cmn_Hello")
        self.btn_Cmn_Hello.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Cmn_Hello.text() + " "))

        self.btn_Cmn_Feeling = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Feeling.setGeometry(QtCore.QRect(140, 130, 71, 61))
        self.btn_Cmn_Feeling.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid black")
        self.btn_Cmn_Feeling.setObjectName("btn_Cmn_Feeling")
        self.btn_Cmn_Feeling.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Cmn_Feeling.text() + " "))

        self.btn_Cmn_IDK = QtGui.QPushButton(self.widget)
        self.btn_Cmn_IDK.setGeometry(QtCore.QRect(280, 130, 71, 61))
        self.btn_Cmn_IDK.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid black")
        self.btn_Cmn_IDK.setObjectName("btn_Cmn_IDK")
        self.btn_Cmn_IDK.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Cmn_IDK.text() + " "))

        self.btn_Cmn_Goodbye = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Goodbye.setGeometry(QtCore.QRect(70, 70, 71, 61))
        self.btn_Cmn_Goodbye.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(255, 170, 0);")
        self.btn_Cmn_Goodbye.setObjectName("btn_Cmn_Goodbye")
        self.btn_Cmn_Goodbye.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Cmn_Goodbye.text() + " "))

        self.btn_Cmn_Howareyou = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Howareyou.setGeometry(QtCore.QRect(210, 130, 71, 61))
        self.btn_Cmn_Howareyou.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(255, 170, 0);")
        self.btn_Cmn_Howareyou.setObjectName("btn_Cmn_Howareyou")
        self.btn_Cmn_Howareyou.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Cmn_Howareyou.text() + " "))

        self.btn_Cmn_Hungry = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Hungry.setGeometry(QtCore.QRect(70, 130, 71, 61))
        self.btn_Cmn_Hungry.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(255, 170, 0);")
        self.btn_Cmn_Hungry.setObjectName("btn_Cmn_Hungry")
        self.btn_Cmn_Hungry.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Cmn_Hungry.text() + " "))

        self.btn_Cmn_And = QtGui.QPushButton(self.widget)
        self.btn_Cmn_And.setGeometry(QtCore.QRect(280, 70, 71, 61))
        self.btn_Cmn_And.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid black")
        self.btn_Cmn_And.setObjectName("btn_Cmn_And")
        self.btn_Cmn_And.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Cmn_And.text() + " "))

        """>>>>>>>>>>Verb buttons<<<<<<<<<<"""



        self.btn_Verb_Go = QtGui.QPushButton(self.widget)
        self.btn_Verb_Go.setGeometry(QtCore.QRect(280, 250, 71, 61))
        self.btn_Verb_Go.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Go.setObjectName("btn_Verb_Go")
        self.btn_Verb_Go.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Verb_Go.text() + " "))
        self.btn_Verb_Go.clicked.connect(lambda: self.func(self.widget, self.go_widget))

        self.btn_Verb_Dislike = QtGui.QPushButton(self.widget)
        self.btn_Verb_Dislike.setGeometry(QtCore.QRect(350, 250, 71, 61))
        self.btn_Verb_Dislike.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Dislike.setObjectName("btn_Verb_Dislike")
        self.btn_Verb_Dislike.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Verb_Dislike.text() + " "))

        self.btn_Verb_Do = QtGui.QPushButton(self.widget)
        self.btn_Verb_Do.setGeometry(QtCore.QRect(210, 250, 71, 61))
        self.btn_Verb_Do.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Do.setObjectName("btn_Verb_Do")
        self.btn_Verb_Do.clicked.connect(lambda: self.func(self.widget, self.do_widget))

        self.btn_Verb_Like = QtGui.QPushButton(self.widget)
        self.btn_Verb_Like.setGeometry(QtCore.QRect(350, 190, 71, 61))
        self.btn_Verb_Like.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Like.setObjectName("btn_Verb_Like")
        self.btn_Verb_Like.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Verb_Like.text() + " "))

        self.btn_Verb_Eat = QtGui.QPushButton(self.widget)
        self.btn_Verb_Eat.setGeometry(QtCore.QRect(280, 310, 71, 61))
        self.btn_Verb_Eat.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Eat.setObjectName("btn_Verb_Eat")
        self.btn_Verb_Eat.clicked.connect(lambda: self.func(self.widget, self.eat_widget))

        self.btn_Verb_Come = QtGui.QPushButton(self.widget)
        self.btn_Verb_Come.setGeometry(QtCore.QRect(420, 190, 71, 61))
        self.btn_Verb_Come.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Come.setObjectName("btn_Verb_Come")
        self.btn_Verb_Come.clicked.connect(lambda: self.func(self.widget, self.come_widget))

        self.btn_Verb_Drink = QtGui.QPushButton(self.widget)
        self.btn_Verb_Drink.setGeometry(QtCore.QRect(350, 310, 71, 61))
        self.btn_Verb_Drink.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Drink.setObjectName("btn_Verb_Drink")
        self.btn_Verb_Drink.clicked.connect(lambda: self.func(self.widget, self.drink_widget))

        self.btn_Verb_Want = QtGui.QPushButton(self.widget)
        self.btn_Verb_Want.setGeometry(QtCore.QRect(210, 310, 71, 61))
        self.btn_Verb_Want.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Want.setObjectName("btn_Verb_Want")
        self.btn_Verb_Want.clicked.connect(lambda: self.func(self.widget, self.want_widget))

        """>>>>>>>>>>Other buttons<<<<<<<<<<"""

        self.btn_Food = QtGui.QPushButton(self.widget)
        self.btn_Food.setGeometry(QtCore.QRect(280, 190, 71, 61))
        self.btn_Food.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(208, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_Food.setObjectName("btn_Food")
        self.btn_Food.clicked.connect(lambda: self.func(self.widget, self.food_widget))

        self.btn_Pointers = QtGui.QPushButton(self.widget)
        self.btn_Pointers.setGeometry(QtCore.QRect(420, 250, 71, 61))
        self.btn_Pointers.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border: 1px solid black")        
        self.btn_Pointers.setObjectName("btn_Pointers")
        self.btn_Pointers.clicked.connect(lambda: self.func(self.widget, self.pointers_widget))

        self.btn_Prep = QtGui.QPushButton(self.widget)
        self.btn_Prep.setGeometry(QtCore.QRect(210, 190, 71, 61))
        self.btn_Prep.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border: 1px solid black")
        self.btn_Prep.setObjectName("btn_Prep")
        self.btn_Prep.clicked.connect(lambda: self.func(self.widget, self.prep_widget))

        self.btn_Clear = QtGui.QPushButton(self.widget)
        self.btn_Clear.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_Clear.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.btn_Clear.setObjectName("btn_Clear")
        self.btn_Clear.clicked.connect(lambda: self.SentenceBuilder.setText(""))

        self.btn_Sports = QtGui.QPushButton(self.widget)
        self.btn_Sports.setGeometry(QtCore.QRect(280, 10, 71, 61))
        self.btn_Sports.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(208, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_Sports.setObjectName("btn_Sports")
        self.btn_Sports.clicked.connect(lambda: self.func(self.widget, self.sports_Group))

        self.btn_Articles = QtGui.QPushButton(self.widget)
        self.btn_Articles.setGeometry(QtCore.QRect(420, 70, 71, 61))
        self.btn_Articles.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border: 1px solid black")
        self.btn_Articles.setObjectName("btn_Articles")
        self.btn_Articles.clicked.connect(lambda: self.func(self.widget, self.widget_5))

        self.btn_Cmn_Or = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Or.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_Cmn_Or.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid black")
        self.btn_Cmn_Or.setObjectName("btn_Cmn_Or")
        self.btn_Cmn_Or.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Cmn_Or.text() + " "))

        self.btn_Is = QtGui.QPushButton(self.widget)
        self.btn_Is.setGeometry(QtCore.QRect(210, 10, 71, 61))
        self.btn_Is.setStyleSheet("border: 1px solid black")
        self.btn_Is.setObjectName("btn_Is")
        self.btn_Is.clicked.connect(lambda: self.func(self.widget, self.widget_3))

        self.btn_Questions = QtGui.QPushButton(self.widget)
        self.btn_Questions.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_Questions.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.btn_Questions.setObjectName("btn_Questions")
        self.btn_Questions.clicked.connect(lambda: self.func(self.widget, self.widget_2))

        self.btn_School = QtGui.QPushButton(self.widget)
        self.btn_School.setGeometry(QtCore.QRect(420, 10, 71, 61))
        self.btn_School.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(208, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_School.setObjectName("btn_School")
        self.btn_School.clicked.connect(lambda: self.func(self.widget, self.school_Group))

        self.btn_Cmn_Home = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Home.setGeometry(QtCore.QRect(420, 130, 71, 61))
        self.btn_Cmn_Home.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(208, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_Cmn_Home.setObjectName("btn_Cmn_Home")
        self.btn_Cmn_Home.clicked.connect(lambda: self.func(self.widget, self.home_Group))

        self.btn_Phrases = QtGui.QPushButton(self.widget)
        self.btn_Phrases.setGeometry(QtCore.QRect(350, 10, 71, 61))
        self.btn_Phrases.setStyleSheet("border: 1px solid black")
        self.btn_Phrases.setObjectName("btn_Phrases")
        self.btn_Phrases.clicked.connect(lambda: self.func(self.widget, self.widget_4))

        """ xxxxxxxxxx Object name: widget_2 des: Questions xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.widget_2.setObjectName("widget_2")
        self.widget_2.hide()

        """Where Button"""
        self.btn_Where = QtGui.QPushButton(self.widget_2)
        self.btn_Where.setGeometry(QtCore.QRect(120, 80, 71, 61))
        self.btn_Where.setStyleSheet("border: 1px solid black;\n"
"selection-color: rgb(255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 255);")
        self.btn_Where.setObjectName("btn_Where")
        self.btn_Where.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Where.text() + " "))
        self.btn_Where.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_2))

        self.btn_When = QtGui.QPushButton(self.widget_2)
        self.btn_When.setGeometry(QtCore.QRect(190, 140, 71, 61))
        self.btn_When.setStyleSheet("border: 1px solid black;\n"
"selection-color: rgb(255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 255);")
        self.btn_When.setObjectName("btn_When")
        self.btn_When.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_When.text() + " "))
        self.btn_When.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_2))

        self.btn_What = QtGui.QPushButton(self.widget_2)
        self.btn_What.setGeometry(QtCore.QRect(50, 80, 71, 61))
        self.btn_What.setStyleSheet("border: 1px solid black;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 255);\n"
"selection-color: rgb(255, 255, 0);")
        self.btn_What.setObjectName("btn_What")
        self.btn_What.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_What.text() + " "))
        self.btn_What.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_2))

        self.btn_How = QtGui.QPushButton(self.widget_2)
        self.btn_How.setGeometry(QtCore.QRect(120, 140, 71, 61))
        self.btn_How.setStyleSheet("border: 1px solid black;\n"
"selection-color: rgb(255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 255);")
        self.btn_How.setObjectName("btn_Translation_6")
        self.btn_How.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_How.text() + " "))
        self.btn_How.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_2))

        self.btn_Which = QtGui.QPushButton(self.widget_2)
        self.btn_Which.setGeometry(QtCore.QRect(50, 140, 71, 61))
        self.btn_Which.setStyleSheet("border: 1px solid black;\n"
"selection-color: rgb(255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 255);")
        self.btn_Which.setObjectName("btn_Which")
        self.btn_Which.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Which.text() + " "))
        self.btn_Which.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_2))

        self.btn_Who = QtGui.QPushButton(self.widget_2)
        self.btn_Who.setGeometry(QtCore.QRect(190, 80, 71, 61))
        self.btn_Who.setStyleSheet("border: 1px solid black;\n"
"selection-color: rgb(255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 255);")
        self.btn_Who.setObjectName("btn_Who")
        self.btn_Who.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Who.text() + " "))
        self.btn_Who.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_2))

        """xxxxxxxxxx Object name: widget_3 Des: state of being i.e. is/am/are/will/were xxxxxxxxxxxxxxxxxxxxxxxx"""

        self.widget_3 = QtGui.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.widget_3.setObjectName("widget_3")
        self.widget_3.hide()

        """ Is button """
        self.btn_is = QtGui.QPushButton(self.widget_3)
        self.btn_is.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_is.setStyleSheet("border: 1px solid black")
        self.btn_is.setObjectName("btn_is")
        self.btn_is.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_is.text() + " "))
        self.btn_is.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_3))

        """ Is not button """
        self.btn_is_not = QtGui.QPushButton(self.widget_3)
        self.btn_is_not.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_is_not.setStyleSheet("border: 1px solid black")
        self.btn_is_not.setObjectName("btn_is_not")
        self.btn_is_not.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_is_not.text() + " "))
        self.btn_is_not.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_3))

        """ Am button """
        self.btn_am = QtGui.QPushButton(self.widget_3)
        self.btn_am.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_am.setStyleSheet("border: 1px solid black")
        self.btn_am.setObjectName("btn_am")
        self.btn_am.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_am.text() + " "))
        self.btn_am.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_3))

        """ Am not button """
        self.btn_am_not = QtGui.QPushButton(self.widget_3)
        self.btn_am_not.setGeometry(QtCore.QRect(210, 10, 71, 61))
        self.btn_am_not.setStyleSheet("border: 1px solid black")
        self.btn_am_not.setObjectName("btn_am")
        self.btn_am_not.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_am_not.text() + " "))
        self.btn_am_not.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_3))

        """ Are button """
        self.btn_are = QtGui.QPushButton(self.widget_3)
        self.btn_are.setGeometry(QtCore.QRect(280, 10, 71, 61))
        self.btn_are.setStyleSheet("border: 1px solid black")
        self.btn_are.setObjectName("btn_am")
        self.btn_are.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_are.text() + " "))
        self.btn_are.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_3))

        """ Are not button """
        self.btn_are_not = QtGui.QPushButton(self.widget_3)
        self.btn_are_not.setGeometry(QtCore.QRect(350, 10, 71, 61))
        self.btn_are_not.setStyleSheet("border: 1px solid black")
        self.btn_are_not.setObjectName("btn_am")
        self.btn_are_not.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_are_not.text() + " "))
        self.btn_are_not.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_3))

        """ Was button """
        self.btn_was = QtGui.QPushButton(self.widget_3)
        self.btn_was.setGeometry(QtCore.QRect(420, 10, 71, 61))
        self.btn_was.setStyleSheet("border: 1px solid black")
        self.btn_was.setObjectName("btn_am")
        self.btn_was.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_was.text() + " "))
        self.btn_was.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_3))

        """ Was not button """
        self.btn_was_not = QtGui.QPushButton(self.widget_3)
        self.btn_was_not.setGeometry(QtCore.QRect(0, 70, 71, 61))
        self.btn_was_not.setStyleSheet("border: 1px solid black")
        self.btn_was_not.setObjectName("btn_am")
        self.btn_was_not.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_was_not.text() + " "))
        self.btn_was_not.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_3))

        """ Were button """
        self.btn_were = QtGui.QPushButton(self.widget_3)
        self.btn_were.setGeometry(QtCore.QRect(70, 70, 71, 61))
        self.btn_were.setStyleSheet("border: 1px solid black")
        self.btn_were.setObjectName("btn_am")
        self.btn_were.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_were.text() + " "))
        self.btn_were.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_3))


        """ Were not button """
        self.btn_were_not = QtGui.QPushButton(self.widget_3)
        self.btn_were_not.setGeometry(QtCore.QRect(140, 70, 71, 61))
        self.btn_were_not.setStyleSheet("border: 1px solid black")
        self.btn_were_not.setObjectName("btn_am")
        self.btn_were_not.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_were_not.text() + " "))
        self.btn_were_not.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_3))

        """ Will button """
        self.btn_will = QtGui.QPushButton(self.widget_3)
        self.btn_will.setGeometry(QtCore.QRect(210, 70, 71, 61))
        self.btn_will.setStyleSheet("border: 1px solid black")
        self.btn_will.setObjectName("btn_am")
        self.btn_will.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_will.text() + " "))
        self.btn_will.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_3))

        """ Will not button """
        self.btn_will_not = QtGui.QPushButton(self.widget_3)
        self.btn_will_not.setGeometry(QtCore.QRect(280, 70, 71, 61))
        self.btn_will_not.setStyleSheet("border: 1px solid black")
        self.btn_will_not.setObjectName("btn_am")
        self.btn_will_not.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_will_not.text() + " "))
        self.btn_will_not.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_3))

        """>>>>>>>>>> Object name: widget_4 --- description: Phrases widget <<<<<<<<<<"""

        self.widget_4 = QtGui.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.widget_4.setObjectName("widget_4")
        self.widget_4.hide()

        self.btn_add_phrases = QtGui.QPushButton(self.widget_4)
        self.btn_add_phrases.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_add_phrases.setStyleSheet("border: 1px solid black")
        self.btn_add_phrases.setObjectName("btn_add_phrases")

        self.btn_deleteConfig = QtGui.QPushButton(self.widget_4)
        self.btn_deleteConfig.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_deleteConfig.setStyleSheet("border: 1px solid black")
        self.btn_deleteConfig.setObjectName("btn_deleteConfig")

        self.btn_b2m_phrase = QtGui.QPushButton(self.widget_4)
        self.btn_b2m_phrase.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_phrase.setStyleSheet("border: 1px solid black")
        self.btn_b2m_phrase.setObjectName("btn_b2m_phrase")
        self.btn_b2m_phrase.setText("Return")
        self.btn_b2m_phrase.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_4))

        """>>>>>>>>>>>> Object name: widget_5 Description: article widget <<<<<<<<<<"""

        self.widget_5 = QtGui.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.widget_5.setObjectName("widget_5")
        self.widget_5.hide()

        self.btn_a = QtGui.QPushButton(self.widget_5)
        self.btn_a.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_a.setStyleSheet("border: 1px solid black")
        self.btn_a.setObjectName("btn_a")
        self.btn_a.setText("a ")
        self.btn_a.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_a.text()))

        self.btn_an = QtGui.QPushButton(self.widget_5)
        self.btn_an.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_an.setStyleSheet("border: 1px solid black")
        self.btn_an.setObjectName("btn_an")
        self.btn_an.setText("an ")
        self.btn_an.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_an.text()))

        self.btn_the = QtGui.QPushButton(self.widget_5)
        self.btn_the.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_the.setStyleSheet("border: 1px solid black")
        self.btn_the.setObjectName("btn_the")
        self.btn_the.setText("the ")
        self.btn_the.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_the.text()))

        self.btn_some = QtGui.QPushButton(self.widget_5)
        self.btn_some.setGeometry(QtCore.QRect(0, 70, 71, 61))
        self.btn_some.setStyleSheet("border: 1px solid black")
        self.btn_some.setObjectName("btn_some")
        self.btn_some.setText("some ")
        self.btn_some.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_some.text()))

        self.btn_few = QtGui.QPushButton(self.widget_5)
        self.btn_few.setGeometry(QtCore.QRect(70, 70, 71, 61))
        self.btn_few.setStyleSheet("border: 1px solid black")
        self.btn_few.setObjectName("btn_few")
        self.btn_few.setText("few ")
        self.btn_few.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_few.text()))

        self.btn_one = QtGui.QPushButton(self.widget_5)
        self.btn_one.setGeometry(QtCore.QRect(140, 70, 71, 61))
        self.btn_one.setStyleSheet("border: 1px solid black")
        self.btn_one.setObjectName("btn_one")
        self.btn_one.setText("one ")
        self.btn_one.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_one.text()))

        self.btn_b2m_art = QtGui.QPushButton(self.widget_5)
        self.btn_b2m_art.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_art.setStyleSheet("border: 1px solid black")
        self.btn_b2m_art.setObjectName("btn_b2m_art")
        self.btn_b2m_art.setText("Return")
        self.btn_b2m_art.clicked.connect(lambda: self.funcReverse(self.widget, self.widget_5))

        """>>>>>>>>>>> Object name: do_widget Description: To Do conjugations do/done/doing"""

        self.do_widget = QtGui.QWidget(self.centralwidget)
        self.do_widget.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.do_widget.setObjectName("do_widget")
        self.do_widget.hide()

        self.btn_do = QtGui.QPushButton(self.do_widget)
        self.btn_do.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_do.setStyleSheet("border: 1px solid black")
        self.btn_do.setObjectName("btn_do")
        self.btn_do.setText("do ")
        self.btn_do.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_do.text()))

        self.btn_done = QtGui.QPushButton(self.do_widget)
        self.btn_done.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_done.setStyleSheet("border: 1px solid black")
        self.btn_done.setObjectName("btn_done")
        self.btn_done.setText("done ")
        self.btn_done.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_done.text()))

        self.btn_doing = QtGui.QPushButton(self.do_widget)
        self.btn_doing.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_doing.setStyleSheet("border: 1px solid black")
        self.btn_doing.setObjectName("btn_doing")
        self.btn_doing.setText("doing ")
        self.btn_doing.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_doing.text()))

        self.btn_to_do = QtGui.QPushButton(self.do_widget)
        self.btn_to_do.setGeometry(QtCore.QRect(210, 10, 71, 61))
        self.btn_to_do.setStyleSheet("border: 1px solid black")
        self.btn_to_do.setObjectName("btn_to_do")
        self.btn_to_do.setText("to do ")
        self.btn_to_do.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_to_do.text()))

        self.btn_b2m_do = QtGui.QPushButton(self.do_widget)
        self.btn_b2m_do.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_do.setStyleSheet("border: 1px solid black")
        self.btn_b2m_do.setObjectName("btn_b2m_do")
        self.btn_b2m_do.setText("Return")
        self.btn_b2m_do.clicked.connect(lambda: self.funcReverse(self.widget, self.do_widget))  

        """>>>>>>>>>> Object name: go_Widget Description: go conjugations <<<<<<<<<<"""

        self.go_widget = QtGui.QWidget(self.centralwidget)
        self.go_widget.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.go_widget.setObjectName("go_widget")
        self.go_widget.hide()

        self.btn_go = QtGui.QPushButton(self.go_widget)
        self.btn_go.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_go.setStyleSheet("border: 1px solid black")
        self.btn_go.setObjectName("btn_do")
        self.btn_go.setText("go ")
        self.btn_go.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_go.text()))

        self.btn_gone = QtGui.QPushButton(self.go_widget)
        self.btn_gone.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_gone.setStyleSheet("border: 1px solid black")
        self.btn_gone.setObjectName("btn_gone")
        self.btn_gone.setText("gone ")
        self.btn_gone.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_gone.text()))

        self.btn_going = QtGui.QPushButton(self.go_widget)
        self.btn_going.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_going.setStyleSheet("border: 1px solid black")
        self.btn_going.setObjectName("btn_going")
        self.btn_going.setText("going ")
        self.btn_going.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_going.text()))

        self.btn_to_go = QtGui.QPushButton(self.go_widget)
        self.btn_to_go.setGeometry(QtCore.QRect(210, 10, 71, 61))
        self.btn_to_go.setStyleSheet("border: 1px solid black")
        self.btn_to_go.setObjectName("btn_to_go")
        self.btn_to_go.setText("to go ")
        self.btn_to_go.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_to_go.text()))

        self.btn_go_to = QtGui.QPushButton(self.go_widget)
        self.btn_go_to.setGeometry(QtCore.QRect(280, 10, 71, 61))
        self.btn_go_to.setStyleSheet("border: 1px solid black")
        self.btn_go_to.setObjectName("btn_to_go")
        self.btn_go_to.setText("go to ")
        self.btn_go_to.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_go_to.text()))

        self.btn_going_to = QtGui.QPushButton(self.go_widget)
        self.btn_going_to.setGeometry(QtCore.QRect(350, 10, 71, 61))
        self.btn_going_to.setStyleSheet("border: 1px solid black")
        self.btn_going_to.setObjectName("btn_going_to")
        self.btn_going_to.setText("going to ")
        self.btn_going_to.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_going_to.text()))

        self.btn_b2m_go = QtGui.QPushButton(self.go_widget)
        self.btn_b2m_go.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_go.setStyleSheet("border: 1px solid black")
        self.btn_b2m_go.setObjectName("btn_b2m_go")
        self.btn_b2m_go.setText("Return")
        self.btn_b2m_go.clicked.connect(lambda: self.funcReverse(self.widget, self.go_widget))  

        """>>>>>>>>>> Object name: come_Widget Description: come conjugations<<<<<<<<<<"""

        self.come_widget = QtGui.QWidget(self.centralwidget)
        self.come_widget.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.come_widget.setObjectName("come_widget")
        self.come_widget.hide()

        self.btn_come = QtGui.QPushButton(self.come_widget)
        self.btn_come.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_come.setStyleSheet("border: 1px solid black")
        self.btn_come.setObjectName("btn_come")
        self.btn_come.setText("come ")
        self.btn_come.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_come.text()))

        self.btn_came = QtGui.QPushButton(self.come_widget)
        self.btn_came.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_came.setStyleSheet("border: 1px solid black")
        self.btn_came.setObjectName("btn_came")
        self.btn_came.setText("came ")
        self.btn_came.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_came.text()))

        self.btn_coming = QtGui.QPushButton(self.come_widget)
        self.btn_coming.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_coming.setStyleSheet("border: 1px solid black")
        self.btn_coming.setObjectName("btn_coming")
        self.btn_coming.setText("coming ")
        self.btn_coming.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_coming.text()))

        self.btn_b2m_come = QtGui.QPushButton(self.come_widget)
        self.btn_b2m_come.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_come.setStyleSheet("border: 1px solid black")
        self.btn_b2m_come.setObjectName("btn_b2m_come")
        self.btn_b2m_come.setText("Return")
        self.btn_b2m_come.clicked.connect(lambda: self.funcReverse(self.widget, self.come_widget)) 

        """>>>>>>>>>> Object name: want_Widget Description: want conjugations<<<<<<<<<<"""

        self.want_widget = QtGui.QWidget(self.centralwidget)
        self.want_widget.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.want_widget.setObjectName("want_widget")
        self.want_widget.hide()

        self.btn_want = QtGui.QPushButton(self.want_widget)
        self.btn_want.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_want.setStyleSheet("border: 1px solid black")
        self.btn_want.setObjectName("btn_want")
        self.btn_want.setText("want ")
        self.btn_want.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_want.text()))

        self.btn_wanted = QtGui.QPushButton(self.want_widget)
        self.btn_wanted.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_wanted.setStyleSheet("border: 1px solid black")
        self.btn_wanted.setObjectName("btn_wanted")
        self.btn_wanted.setText("wanted ")
        self.btn_wanted.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_wanted.text()))

        self.btn_wantto = QtGui.QPushButton(self.want_widget)
        self.btn_wantto.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_wantto.setStyleSheet("border: 1px solid black")
        self.btn_wantto.setObjectName("btn_wantto")
        self.btn_wantto.setText("want to ")
        self.btn_wantto.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_wantto.text()))

        self.btn_b2m_want = QtGui.QPushButton(self.want_widget)
        self.btn_b2m_want.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_want.setStyleSheet("border: 1px solid black")
        self.btn_b2m_want.setObjectName("btn_b2m_want")
        self.btn_b2m_want.setText("Return")
        self.btn_b2m_want.clicked.connect(lambda: self.funcReverse(self.widget, self.want_widget))

        """>>>>>>>>>> Object name: drink_Widget Description: drink conjugations <<<<<<<<<<"""

        self.drink_widget = QtGui.QWidget(self.centralwidget)
        self.drink_widget.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.drink_widget.setObjectName("drink_widget")
        self.drink_widget.hide()

        self.btn_drink = QtGui.QPushButton(self.drink_widget)
        self.btn_drink.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_drink.setStyleSheet("border: 1px solid black")
        self.btn_drink.setObjectName("btn_drink")
        self.btn_drink.setText("drink ")
        self.btn_drink.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_drink.text()))

        self.btn_drunk = QtGui.QPushButton(self.drink_widget)
        self.btn_drunk.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_drunk.setStyleSheet("border: 1px solid black")
        self.btn_drunk.setObjectName("btn_drunk")
        self.btn_drunk.setText("drunk ")
        self.btn_drunk.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_drunk.text()))

        self.btn_drinking = QtGui.QPushButton(self.drink_widget)
        self.btn_drinking.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_drinking.setStyleSheet("border: 1px solid black")
        self.btn_drinking.setObjectName("btn_drinking")
        self.btn_drinking.setText("drinking ")
        self.btn_drinking.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_drinking.text()))

        self.btn_b2m_drink = QtGui.QPushButton(self.drink_widget)
        self.btn_b2m_drink.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_drink.setStyleSheet("border: 1px solid black")
        self.btn_b2m_drink.setObjectName("btn_b2m_drink")
        self.btn_b2m_drink.setText("Return")
        self.btn_b2m_drink.clicked.connect(lambda: self.funcReverse(self.widget, self.drink_widget))

        """>>>>>>>>>> Object name: home_Group Description: home group words <<<<<<<<<<"""

        self.home_Group = QtGui.QWidget(self.centralwidget)
        self.home_Group.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.home_Group.setObjectName("home_Group")
        self.home_Group.hide()

        self.btn_house = QtGui.QPushButton(self.home_Group)
        self.btn_house.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_house.setStyleSheet("border: 1px solid black")
        self.btn_house.setObjectName("btn_drink")
        self.btn_house.setText("house ")
        self.btn_house.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_house.text()))

        self.btn_kitchen = QtGui.QPushButton(self.home_Group)
        self.btn_kitchen.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_kitchen.setStyleSheet("border: 1px solid black")
        self.btn_kitchen.setObjectName("btn_kitchen")
        self.btn_kitchen.setText("kitchen ")
        self.btn_kitchen.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_kitchen.text()))

        self.btn_tv = QtGui.QPushButton(self.home_Group)
        self.btn_tv.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_tv.setStyleSheet("border: 1px solid black")
        self.btn_tv.setObjectName("btn_tv")
        self.btn_tv.setText("TV ")
        self.btn_tv.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_tv.text()))

        self.btn_b2m_home = QtGui.QPushButton(self.home_Group)
        self.btn_b2m_home.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_home.setStyleSheet("border: 1px solid black")
        self.btn_b2m_home.setObjectName("btn_b2m_drink")
        self.btn_b2m_home.setText("Return")
        self.btn_b2m_home.clicked.connect(lambda: self.funcReverse(self.widget, self.home_Group))

        """>>>>>>>>>>Object name: school_Group Description: school group words<<<<<<<<<<"""

        self.school_Group = QtGui.QWidget(self.centralwidget)
        self.school_Group.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.school_Group.setObjectName("school_Group")
        self.school_Group.hide()

        self.btn_school = QtGui.QPushButton(self.school_Group)
        self.btn_school.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_school.setStyleSheet("border: 1px solid black")
        self.btn_school.setObjectName("btn_drink")
        self.btn_school.setText("school ")
        self.btn_school.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_school.text()))

        self.btn_maths = QtGui.QPushButton(self.school_Group)
        self.btn_maths.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_maths.setStyleSheet("border: 1px solid black")
        self.btn_maths.setObjectName("btn_maths")
        self.btn_maths.setText("maths ")
        self.btn_maths.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_maths.text()))

        self.btn_pencil = QtGui.QPushButton(self.school_Group)
        self.btn_pencil.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_pencil.setStyleSheet("border: 1px solid black")
        self.btn_pencil.setObjectName("btn_pencil")
        self.btn_pencil.setText("pencil ")
        self.btn_pencil.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_pencil.text()))

        self.btn_b2m_school = QtGui.QPushButton(self.school_Group)
        self.btn_b2m_school.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_school.setStyleSheet("border: 1px solid black")
        self.btn_b2m_school.setObjectName("btn_b2m_school")
        self.btn_b2m_school.setText("Return")
        self.btn_b2m_school.clicked.connect(lambda: self.funcReverse(self.widget, self.school_Group))

        """>>>>>>>>>>Object name: sports_Group Description: sport group words<<<<<<<<<<"""

        self.sports_Group = QtGui.QWidget(self.centralwidget)
        self.sports_Group.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.sports_Group.setObjectName("sports_Group")
        self.sports_Group.hide()

        self.btn_football = QtGui.QPushButton(self.sports_Group)
        self.btn_football.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_football.setStyleSheet("border: 1px solid black")
        self.btn_football.setObjectName("btn_football")
        self.btn_football.setText("football ")
        self.btn_football.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_football.text()))

        self.btn_to_play  = QtGui.QPushButton(self.sports_Group)
        self.btn_to_play.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_to_play.setStyleSheet("border: 1px solid black")
        self.btn_to_play.setObjectName("btn_to_play")
        self.btn_to_play.setText("to play ")
        self.btn_to_play.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_to_play.text()))

        self.btn_tennis = QtGui.QPushButton(self.sports_Group)
        self.btn_tennis.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_tennis.setStyleSheet("border: 1px solid black")
        self.btn_tennis.setObjectName("btn_tennis")
        self.btn_tennis.setText("tennis ")
        self.btn_tennis.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_tennis.text()))

        self.btn_b2m_sports = QtGui.QPushButton(self.sports_Group)
        self.btn_b2m_sports.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_sports.setStyleSheet("border: 1px solid black")
        self.btn_b2m_sports.setObjectName("btn_b2m_sports")
        self.btn_b2m_sports.setText("Return")
        self.btn_b2m_sports.clicked.connect(lambda: self.funcReverse(self.widget, self.sports_Group))

        """>>>>>>>>>> Object name: prep_widget Description: widget containing prepositions<<<<<<<<<<"""

        self.prep_widget = QtGui.QWidget(self.centralwidget)
        self.prep_widget.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.prep_widget.setObjectName("prep_widget")
        self.prep_widget.hide()

        self.btn_at = QtGui.QPushButton(self.prep_widget)
        self.btn_at.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_at.setStyleSheet("border: 1px solid black")
        self.btn_at.setObjectName("btn_at")
        self.btn_at.setText("at ")
        self.btn_at.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_at.text()))

        self.btn_as = QtGui.QPushButton(self.prep_widget)
        self.btn_as.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_as.setStyleSheet("border: 1px solid black")
        self.btn_as.setObjectName("btn_as")
        self.btn_as.setText("as ")
        self.btn_as.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_as.text()))

        self.btn_with = QtGui.QPushButton(self.prep_widget)
        self.btn_with.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_with.setStyleSheet("border: 1px solid black")
        self.btn_with.setObjectName("btn_with")
        self.btn_with.setText("with ")
        self.btn_with.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_with.text()))

        self.btn_but = QtGui.QPushButton(self.prep_widget)
        self.btn_but.setGeometry(QtCore.QRect(0, 70, 71, 61))
        self.btn_but.setStyleSheet("border: 1px solid black")
        self.btn_but.setObjectName("btn_but")
        self.btn_but.setText("but ")
        self.btn_but.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_but.text()))

        self.btn_in = QtGui.QPushButton(self.prep_widget)
        self.btn_in.setGeometry(QtCore.QRect(70, 70, 71, 61))
        self.btn_in.setStyleSheet("border: 1px solid black")
        self.btn_in.setObjectName("btn_in")
        self.btn_in.setText("in ")
        self.btn_in.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_in.text()))

        self.btn_before = QtGui.QPushButton(self.prep_widget)
        self.btn_before.setGeometry(QtCore.QRect(140, 70, 71, 61))
        self.btn_before.setStyleSheet("border: 1px solid black")
        self.btn_before.setObjectName("btn_before")
        self.btn_before.setText("before ")
        self.btn_before.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_before.text()))

        self.btn_b2m_prep = QtGui.QPushButton(self.prep_widget)
        self.btn_b2m_prep.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_prep.setStyleSheet("border: 1px solid black")
        self.btn_b2m_prep.setObjectName("btn_b2m_prep")
        self.btn_b2m_prep.setText("Return")
        self.btn_b2m_prep.clicked.connect(lambda: self.funcReverse(self.widget, self.prep_widget))

        """>>>>>>>>>> Object name: eat_widget description: conjugations for the verb eat <<<<<<<<<<"""

        self.eat_widget = QtGui.QWidget(self.centralwidget)
        self.eat_widget.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.eat_widget.setObjectName("eat_widget")
        self.eat_widget.hide()

        self.btn_eat = QtGui.QPushButton(self.eat_widget)
        self.btn_eat.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_eat.setStyleSheet("border: 1px solid black")
        self.btn_eat.setObjectName("btn_eat")
        self.btn_eat.setText("eat ")
        self.btn_eat.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_eat.text()))

        self.btn_ate = QtGui.QPushButton(self.eat_widget)
        self.btn_ate.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_ate.setStyleSheet("border: 1px solid black")
        self.btn_ate.setObjectName("btn_ate")
        self.btn_ate.setText("ate ")
        self.btn_ate.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_ate.text()))

        self.btn_eating = QtGui.QPushButton(self.eat_widget)
        self.btn_eating.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_eating.setStyleSheet("border: 1px solid black")
        self.btn_eating.setObjectName("btn_eating")
        self.btn_eating.setText("eating ")
        self.btn_eating.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_eating.text()))

        self.btn_eaten = QtGui.QPushButton(self.eat_widget)
        self.btn_eaten.setGeometry(QtCore.QRect(0, 70, 71, 61))
        self.btn_eaten.setStyleSheet("border: 1px solid black")
        self.btn_eaten.setObjectName("btn_eaten")
        self.btn_eaten.setText("eaten ")
        self.btn_eaten.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_eaten.text()))

        self.btn_b2m_eat = QtGui.QPushButton(self.eat_widget)
        self.btn_b2m_eat.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_eat.setStyleSheet("border: 1px solid black")
        self.btn_b2m_eat.setObjectName("btn_b2m_eat")
        self.btn_b2m_eat.setText("Return")
        self.btn_b2m_eat.clicked.connect(lambda: self.funcReverse(self.widget, self.eat_widget))

        """>>>>>>>>>> Object name: pointers_widget description: this, that, those, there <<<<<<<<<<"""

        self.pointers_widget = QtGui.QWidget(self.centralwidget)
        self.pointers_widget.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.pointers_widget.setObjectName("pointers_widget")
        self.pointers_widget.hide()

        self.btn_this = QtGui.QPushButton(self.pointers_widget)
        self.btn_this.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_this.setStyleSheet("border: 1px solid black")
        self.btn_this.setObjectName("btn_this")
        self.btn_this.setText("this ")
        self.btn_this.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_this.text()))

        self.btn_that = QtGui.QPushButton(self.pointers_widget)
        self.btn_that.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_that.setStyleSheet("border: 1px solid black")
        self.btn_that.setObjectName("btn_that")
        self.btn_that.setText("that ")
        self.btn_that.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_that.text()))

        self.btn_these = QtGui.QPushButton(self.pointers_widget)
        self.btn_these.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_these.setStyleSheet("border: 1px solid black")
        self.btn_these.setObjectName("btn_these")
        self.btn_these.setText("these ")
        self.btn_these.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_these.text()))

        self.btn_those = QtGui.QPushButton(self.pointers_widget)
        self.btn_those.setGeometry(QtCore.QRect(0, 70, 71, 61))
        self.btn_those.setStyleSheet("border: 1px solid black")
        self.btn_those.setObjectName("btn_those")
        self.btn_those.setText("those ")
        self.btn_those.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_those.text()))

        self.btn_b2m_pointers = QtGui.QPushButton(self.pointers_widget)
        self.btn_b2m_pointers.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_pointers.setStyleSheet("border: 1px solid black")
        self.btn_b2m_pointers.setObjectName("btn_b2m_pointers")
        self.btn_b2m_pointers.setText("Return")
        self.btn_b2m_pointers.clicked.connect(lambda: self.funcReverse(self.widget, self.pointers_widget))

        """>>>>>>>>>> Object name: food_widget Description: food list<<<<<<<<<<"""

        self.food_widget = QtGui.QWidget(self.centralwidget)
        self.food_widget.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.food_widget.setObjectName("food_widget")
        self.food_widget.hide()

        self.btn_apple = QtGui.QPushButton(self.food_widget)
        self.btn_apple.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_apple.setStyleSheet("border: 1px solid black")
        self.btn_apple.setObjectName("btn_apple")
        self.btn_apple.setText("apple ")
        self.btn_apple.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_apple.text()))

        self.btn_pizza = QtGui.QPushButton(self.food_widget)
        self.btn_pizza.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_pizza.setStyleSheet("border: 1px solid black")
        self.btn_pizza.setObjectName("btn_pizza")
        self.btn_pizza.setText("pizza ")
        self.btn_pizza.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_pizza.text()))

        self.btn_chocolate = QtGui.QPushButton(self.food_widget)
        self.btn_chocolate.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_chocolate.setStyleSheet("border: 1px solid black")
        self.btn_chocolate.setObjectName("btn_chocolate")
        self.btn_chocolate.setText("chocolate ")
        self.btn_chocolate.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_chocolate.text()))

        self.btn_kimchi = QtGui.QPushButton(self.food_widget)
        self.btn_kimchi.setGeometry(QtCore.QRect(0, 70, 71, 61))
        self.btn_kimchi.setStyleSheet("border: 1px solid black")
        self.btn_kimchi.setObjectName("btn_kimchi")
        self.btn_kimchi.setText("kimchi ")
        self.btn_kimchi.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_kimchi.text()))

        self.btn_steak = QtGui.QPushButton(self.food_widget)
        self.btn_steak.setGeometry(QtCore.QRect(70, 70, 71, 61))
        self.btn_steak.setStyleSheet("border: 1px solid black")
        self.btn_steak.setObjectName("btn_steak")
        self.btn_steak.setText("steak ")
        self.btn_steak.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_steak.text()))

        self.btn_salmon = QtGui.QPushButton(self.food_widget)
        self.btn_salmon.setGeometry(QtCore.QRect(140, 70, 71, 61))
        self.btn_salmon.setStyleSheet("border: 1px solid black")
        self.btn_salmon.setObjectName("btn_salmon")
        self.btn_salmon.setText("Salmon ")
        self.btn_salmon.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_salmon.text()))

        self.btn_b2m_food = QtGui.QPushButton(self.food_widget)
        self.btn_b2m_food.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_food.setStyleSheet("border: 1px solid black")
        self.btn_b2m_food.setObjectName("btn_b2m_food")
        self.btn_b2m_food.setText("Return")
        self.btn_b2m_food.clicked.connect(lambda: self.funcReverse(self.widget, self.food_widget))

        """ End of Duncan's code """

        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(14, 0, 490, 61))
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

        """ Delete Word button and call """
        self.btn_delWord = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_delWord.setObjectName("btn_delWord")
        self.btn_delWord.clicked.connect(lambda: self.wordDelete() )

        self.horizontalLayout.addWidget(self.btn_delWord)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        """ Add text to buttons in Main window Widgets """
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Language.setText(QtGui.QApplication.translate("MainWindow", "Language", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Speak.setText(QtGui.QApplication.translate("MainWindow", "Speak", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add_phrases.setText(QtGui.QApplication.translate("MainWindow", "Add Phrases", None, QtGui.QApplication.UnicodeUTF8))

        self.btn_delWord.setText(QtGui.QApplication.translate("MainWindow", "Delete \n" " Word", None, QtGui.QApplication.UnicodeUTF8))

        self.btn_deleteConfig.setText(QtGui.QApplication.translate("MainWindow", "Delete\n Configuration", None, QtGui.QApplication.UnicodeUTF8))

        """ Perform actions on button presses """
        self.btn_add_phrases.clicked.connect(lambda: self.userInput())
        self.btn_Language.clicked.connect(lambda: self.chooseLang())
        """ Delete phrases from file """
        self.btn_deleteConfig.clicked.connect(lambda: self.redisWipe())

        """ Pass array into speak parser """
        self.btn_Speak.clicked.connect(lambda: self.config.playSounds(self.phraseList) )

self.btn_Pron_She.setText(QtGui.QApplication.translate("MainWindow", "She", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_No.setText(QtGui.QApplication.translate("MainWindow", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Prep.setText(QtGui.QApplication.translate("MainWindow", "Prepositions", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Clear.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Food.setText(QtGui.QApplication.translate("MainWindow", "Food", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Time.setText(QtGui.QApplication.translate("MainWindow", "What time\n"
" is it?", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Sports.setText(QtGui.QApplication.translate("MainWindow", "Sports", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Go.setText(QtGui.QApplication.translate("MainWindow", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_And.setText(QtGui.QApplication.translate("MainWindow", "and", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_I.setText(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_They.setText(QtGui.QApplication.translate("MainWindow", "They", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Dislike.setText(QtGui.QApplication.translate("MainWindow", "Dislike", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Bad.setText(QtGui.QApplication.translate("MainWindow", "Bad", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_It.setText(QtGui.QApplication.translate("MainWindow", "It", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Yes.setText(QtGui.QApplication.translate("MainWindow", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Hello.setText(QtGui.QApplication.translate("MainWindow", "Hello", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Do.setText(QtGui.QApplication.translate("MainWindow", "Do", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_Mine.setText(QtGui.QApplication.translate("MainWindow", "Mine", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Feeling.setText(QtGui.QApplication.translate("MainWindow", "I\'m feeling", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Like.setText(QtGui.QApplication.translate("MainWindow", "Like", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Articles.setText(QtGui.QApplication.translate("MainWindow", "Articles", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_People.setText(QtGui.QApplication.translate("MainWindow", "People", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_You.setText(QtGui.QApplication.translate("MainWindow", "You", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Or.setText(QtGui.QApplication.translate("MainWindow", "or", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_IDK.setText(QtGui.QApplication.translate("MainWindow", "I don\'t know", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Eat.setText(QtGui.QApplication.translate("MainWindow", "Eat", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Goodbye.setText(QtGui.QApplication.translate("MainWindow", "Goodbye", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Is.setText(QtGui.QApplication.translate("MainWindow", "is/were/was\n"
"/are \n"
"(+negatives)", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_We.setText(QtGui.QApplication.translate("MainWindow", "We", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Questions.setText(QtGui.QApplication.translate("MainWindow", "Questions\n"
" ?", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pointers.setText(QtGui.QApplication.translate("MainWindow", "Pointers", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Come.setText(QtGui.QApplication.translate("MainWindow", "Come", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_School.setText(QtGui.QApplication.translate("MainWindow", "School", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_He.setText(QtGui.QApplication.translate("MainWindow", "He", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Drink.setText(QtGui.QApplication.translate("MainWindow", "Drink", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Hungry.setText(QtGui.QApplication.translate("MainWindow", "I\'m hungry", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Want.setText(QtGui.QApplication.translate("MainWindow", "Want", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Howareyou.setText(QtGui.QApplication.translate("MainWindow", "How are\nyou?", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Home.setText(QtGui.QApplication.translate("MainWindow", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Phrases.setText(QtGui.QApplication.translate("MainWindow", "Phrases", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Speak.setText(QtGui.QApplication.translate("MainWindow", "Speak", None, QtGui.QApplication.UnicodeUTF8))
        #self.btn_translation_2.setText(QtGui.QApplication.translate("MainWindow", "Delete \n"
#" Word", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Where.setText(QtGui.QApplication.translate("MainWindow", "Where", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_When.setText(QtGui.QApplication.translate("MainWindow", "When", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_What.setText(QtGui.QApplication.translate("MainWindow", "What", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_How.setText(QtGui.QApplication.translate("MainWindow", "How", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Which.setText(QtGui.QApplication.translate("MainWindow", "Which", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Who.setText(QtGui.QApplication.translate("MainWindow", "Who", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_is.setText(QtGui.QApplication.translate("MainWindow", "is", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_is_not.setText(QtGui.QApplication.translate("MainWindow", "is not", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_am.setText(QtGui.QApplication.translate("MainWindow", "am", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_am_not.setText(QtGui.QApplication.translate("MainWindow", "am not", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_are.setText(QtGui.QApplication.translate("MainWindow", "are", None, QtGui.QApplication.UnicodeUTF8))  
        self.btn_are_not.setText(QtGui.QApplication.translate("MainWindow", "are not", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_will.setText(QtGui.QApplication.translate("MainWindow", "will", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_will_not.setText(QtGui.QApplication.translate("MainWindow", "will not", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_was.setText(QtGui.QApplication.translate("MainWindow", "was", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_was_not.setText(QtGui.QApplication.translate("MainWindow", "was not", None, QtGui.QApplication.UnicodeUTF8))  
        self.btn_were.setText(QtGui.QApplication.translate("MainWindow", "were", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_were_not.setText(QtGui.QApplication.translate("MainWindow", "were not", None, QtGui.QApplication.UnicodeUTF8))

        """ Open question Widget and close question widget """
    def func(self, widget, widget2):
        widget.hide()
        widget2.show()

    def funcReverse(self, widget, widget2):
        widget.show()
        widget2.hide()

    def wordDelete(self):
        """ Need logic here to delete word in phrase list that sentenceBuilder removes """
        self.SentenceBuilder.cursorWordBackward(True)
        self.SentenceBuilder.del_()
        self.phraseList.pop()

    def chooseLang(self):
        self.langText, ok = QtGui.QInputDialog.getText(self.widget, 'Input Dialog', 'Choose Language: ')
        if ok:
           """ Need to pass this into config """
           self.config.langInit(self.langText)

    def userInput(self):
        # Allow user phrase input and pass to config class
        self.text, ok = QtGui.QInputDialog.getText(self.widget, 'Input Dialog', 'Enter phrases: ')
        if ok:
            # Save phrases to a file, I hate doing this so it needs resolving
            try:
                with open("phrases.txt", "ab") as f:
                    f.write(self.text + '\n')
            except IOError:
                with open("phrases.txt", "w"):
                    os.utime("phrases.txt", None)


            """ Call phrases to download sounds """
            self.config.phrases(self.text)
            self.showPhrases()

    def showPhrases(self):
        """ Set base coordinates"""
        baseX = 140
        baseY = 10
        """ Open phrases text and parse through them creating new buttons dynamically """
        with open("phrases.txt", "rb") as f:
            phrases = f.read()
            linePhrase = phrases.split('\n')
        for word in linePhrase:
            self.phraseBtns = QtGui.QPushButton(self.widget_4)
            self.phraseBtns.setGeometry(QtCore.QRect(0, 10, 71, 61))
            self.phraseBtns.setStyleSheet("background-color: rgb(170, 170, 255);\n" "color: rgb(255, 255, 255);\n" "border: 1px solid black;")
            # Create base positions
            self.phraseBtns.move(baseX, baseY)
            self.phraseBtns.setText(QtGui.QApplication.translate("MainWindow", word, None, QtGui.QApplication.UnicodeUTF8))
            self.phraseBtns.show()
            """ Call passToBar and pass phrases that are then store in an array """
            self.passToBar(self.phraseBtns)
            """ Needs fixing """
            if baseX <= 420:
                baseX += 70
                baseY += 0

            if baseY <= 420:
                baseX += 0
                baseY += 60

            if baseX == 420 and baseY == 310:
                "Print, too many phrases, create new widget"


    def verbPhrases(self, text):
        """ Call phrases and download translation of given text """
        self.config.phrases(text)
        """ Pass this text to the speak bar """
        self.passToBar(self.btn_Iam)

    def passToBar(self, phraseBtn):
        """ Pass phrase button text which will then get appended to the relative list """
        phraseBtn.clicked.connect(lambda: self.appendPhrases(phraseBtn.text() ))

    def appendPhrases(self, phrases):
        """ Append button text to the array list for the speak function """
        """ Add check in here to append to correct array - this is dirty and needs fixing """
        if "I am" in phrases:
            self.verbList.append(phrases)
        else:
            self.SentenceBuilder.insert(phrases + " ")
            self.phraseList.append(phrases)

    def redisWipe(self):
        p = ''
        # call the keyDel function in the config class when the redisDelbtn is pressed
        """ A nice feature, would be to delete a given phrase..."""
        """ To do this, create a function which passes the phraseBtn name and remove from there """
        self.btn_deleteConfig.clicked.connect(lambda: self.config.keyDel(self.btn_deleteConfig.text(), p))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
