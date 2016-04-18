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


        """ Sets the Add Phrases button in
        self.btn_addPhrases = QtGui.QPushButton(self.widget)
        self.btn_addPhrases.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_addPhrases.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.btn_addPhrases.setObjectName("btn_AddPhrases") """
        
        """ Add static Phrases 
        self.btn_Iam = QtGui.QPushButton(self.widget)
        self.btn_Iam.setGeometry(QtCore.QRect(160, 20, 81, 71))
        self.btn_addPhrases.setStyleSheet("background-color: rgb(180, 180, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.btn_addPhrases.setObjectName("btn_Iam") 

        self.btn_deleteConfig = QtGui.QPushButton(self.widget)
        self.btn_deleteConfig.setGeometry(QtCore.QRect(260, 10, 71, 61))
        self.btn_deleteConfig.setStyleSheet("border: 1px solid black") """

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

        self.btn_Verb_Look = QtGui.QPushButton(self.widget)
        self.btn_Verb_Look.setGeometry(QtCore.QRect(210, 190, 71, 61))
        self.btn_Verb_Look.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Look.setObjectName("btn_Verb_Look")
        self.btn_Verb_Look.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Verb_Look.text() + " "))
        #self.btn_Verb_Do.clicked.connect(lambda: self.doWidgetOpen(self.widget, self.do_widget))

        self.btn_Verb_Hear = QtGui.QPushButton(self.widget)
        self.btn_Verb_Hear.setGeometry(QtCore.QRect(280, 190, 71, 61))
        self.btn_Verb_Hear.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Hear.setObjectName("btn_Verb_Hear")
        self.btn_Verb_Hear.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Verb_Hear.text() + " "))
        #self.btn_Verb_Do.clicked.connect(lambda: self.doWidgetOpen(self.widget, self.do_widget))

        self.btn_Verb_Go = QtGui.QPushButton(self.widget)
        self.btn_Verb_Go.setGeometry(QtCore.QRect(280, 250, 71, 61))
        self.btn_Verb_Go.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Go.setObjectName("btn_Verb_Go")
        self.btn_Verb_Go.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Verb_Go.text() + " "))
        self.btn_Verb_Go.clicked.connect(lambda: self.goWidgetOpen(self.widget, self.go_widget))

        self.btn_Verb_Dislike = QtGui.QPushButton(self.widget)
        self.btn_Verb_Dislike.setGeometry(QtCore.QRect(350, 250, 71, 61))
        self.btn_Verb_Dislike.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Dislike.setObjectName("btn_Verb_Dislike")
        self.btn_Verb_Dislike.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Verb_Dislike.text() + " "))
        #self.btn_Verb_Do.clicked.connect(lambda: self.doWidgetOpen(self.widget, self.do_widget))

        self.btn_Verb_Do = QtGui.QPushButton(self.widget)
        self.btn_Verb_Do.setGeometry(QtCore.QRect(210, 250, 71, 61))
        self.btn_Verb_Do.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Do.setObjectName("btn_Verb_Do")
        self.btn_Verb_Do.clicked.connect(lambda: self.doWidgetOpen(self.widget, self.do_widget))

        self.btn_Verb_Like = QtGui.QPushButton(self.widget)
        self.btn_Verb_Like.setGeometry(QtCore.QRect(350, 190, 71, 61))
        self.btn_Verb_Like.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Like.setObjectName("btn_Verb_Like")
        self.btn_Verb_Like.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Verb_Like.text() + " "))
        #self.btn_Verb_Do.clicked.connect(lambda: self.doWidgetOpen(self.widget, self.do_widget))

        self.btn_Verb_Eat = QtGui.QPushButton(self.widget)
        self.btn_Verb_Eat.setGeometry(QtCore.QRect(280, 310, 71, 61))
        self.btn_Verb_Eat.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Eat.setObjectName("btn_Verb_Eat")
        self.btn_Verb_Eat.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Verb_Eat.text() + " "))
        #self.btn_Verb_Do.clicked.connect(lambda: self.doWidgetOpen(self.widget, self.do_widget))

        self.btn_Verb_Wear = QtGui.QPushButton(self.widget)
        self.btn_Verb_Wear.setGeometry(QtCore.QRect(420, 250, 71, 61))
        self.btn_Verb_Wear.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Wear.setObjectName("btn_Verb_Wear")
        self.btn_Verb_Wear.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_Verb_Wear.text() + " "))
        #self.btn_Verb_Do.clicked.connect(lambda: self.doWidgetOpen(self.widget, self.do_widget))

        self.btn_Verb_Come = QtGui.QPushButton(self.widget)
        self.btn_Verb_Come.setGeometry(QtCore.QRect(420, 190, 71, 61))
        self.btn_Verb_Come.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Come.setObjectName("btn_Verb_Come")
        self.btn_Verb_Come.clicked.connect(lambda: self.comeWidgetOpen(self.widget, self.come_widget))

        self.btn_Verb_Drink = QtGui.QPushButton(self.widget)
        self.btn_Verb_Drink.setGeometry(QtCore.QRect(350, 310, 71, 61))
        self.btn_Verb_Drink.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Drink.setObjectName("btn_Verb_Drink")
        self.btn_Verb_Drink.clicked.connect(lambda: self.drinkWidgetOpen(self.widget, self.drink_widget))

        self.btn_Verb_Want = QtGui.QPushButton(self.widget)
        self.btn_Verb_Want.setGeometry(QtCore.QRect(210, 310, 71, 61))
        self.btn_Verb_Want.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(85, 255, 127);")
        self.btn_Verb_Want.setObjectName("btn_Verb_Want")
        self.btn_Verb_Want.clicked.connect(lambda: self.wantWidgetOpen(self.widget, self.want_widget))

        """>>>>>>>>>>Misc buttons<<<<<<<<<<"""

        self.btn_Clear = QtGui.QPushButton(self.widget)
        self.btn_Clear.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_Clear.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.btn_Clear.setObjectName("btn_Clear")
        self.btn_Clear.clicked.connect(lambda: self.SentenceBuilder.setText(""))

        self.btn_Nouns = QtGui.QPushButton(self.widget)
        self.btn_Nouns.setGeometry(QtCore.QRect(280, 10, 71, 61))
        self.btn_Nouns.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(208, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_Nouns.setObjectName("btn_Nouns")

        self.btn_punctuation = QtGui.QPushButton(self.widget)
        self.btn_punctuation.setGeometry(QtCore.QRect(420, 70, 71, 61))
        self.btn_punctuation.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border: 1px solid black")
        self.btn_punctuation.setObjectName("btn_punctuation")
        self.btn_punctuation.clicked.connect(lambda: self.punctWidgetOpen(self.widget, self.widget_5))

        self.btn_Translation = QtGui.QPushButton(self.widget)
        self.btn_Translation.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_Translation.setStyleSheet("border: 1px solid black;\n"
"selection-color: rgb(255, 255, 0);")
        self.btn_Translation.setObjectName("btn_Translation")

        self.btn_Is = QtGui.QPushButton(self.widget)
        self.btn_Is.setGeometry(QtCore.QRect(210, 10, 71, 61))
        self.btn_Is.setStyleSheet("border: 1px solid black")
        self.btn_Is.setObjectName("btn_Is")
        self.btn_Is.clicked.connect(lambda: self.isWidgetfunc(self.widget, self.widget_3))

        self.btn_Questions = QtGui.QPushButton(self.widget)
        self.btn_Questions.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_Questions.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.btn_Questions.setObjectName("btn_Questions")
        self.btn_Questions.clicked.connect(lambda: self.func(self.widget, self.widget_2))

        self.btn_Menu = QtGui.QPushButton(self.widget)
        self.btn_Menu.setGeometry(QtCore.QRect(420, 10, 71, 61))
        self.btn_Menu.setStyleSheet("border: 1px solid black")
        self.btn_Menu.setObjectName("btn_Menu")

        self.btn_Cmn_Sizes = QtGui.QPushButton(self.widget)
        self.btn_Cmn_Sizes.setGeometry(QtCore.QRect(420, 130, 71, 61))
        self.btn_Cmn_Sizes.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border: 1px solid black")
        self.btn_Cmn_Sizes.setObjectName("btn_Cmn_Sizes")

        self.btn_Phrases = QtGui.QPushButton(self.widget)
        self.btn_Phrases.setGeometry(QtCore.QRect(350, 10, 71, 61))
        self.btn_Phrases.setStyleSheet("border: 1px solid black")
        self.btn_Phrases.setObjectName("btn_Phrases")
        self.btn_Phrases.clicked.connect(lambda: self.phrasesWidgetOpen(self.widget, self.widget_4))

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
        self.btn_is.clicked.connect(lambda: self.isWidgetReverse(self.widget, self.widget_3))

        """ Is not button """
        self.btn_is_not = QtGui.QPushButton(self.widget_3)
        self.btn_is_not.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_is_not.setStyleSheet("border: 1px solid black")
        self.btn_is_not.setObjectName("btn_is_not")
        self.btn_is_not.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_is_not.text() + " "))
        self.btn_is_not.clicked.connect(lambda: self.isWidgetReverse(self.widget, self.widget_3))

        """ Am button """
        self.btn_am = QtGui.QPushButton(self.widget_3)
        self.btn_am.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_am.setStyleSheet("border: 1px solid black")
        self.btn_am.setObjectName("btn_am")
        self.btn_am.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_am.text() + " "))
        self.btn_am.clicked.connect(lambda: self.isWidgetReverse(self.widget, self.widget_3))

        """ Am not button """
        self.btn_am_not = QtGui.QPushButton(self.widget_3)
        self.btn_am_not.setGeometry(QtCore.QRect(210, 10, 71, 61))
        self.btn_am_not.setStyleSheet("border: 1px solid black")
        self.btn_am_not.setObjectName("btn_am")
        self.btn_am_not.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_am_not.text() + " "))
        self.btn_am_not.clicked.connect(lambda: self.isWidgetReverse(self.widget, self.widget_3))

        """ Are button """
        self.btn_are = QtGui.QPushButton(self.widget_3)
        self.btn_are.setGeometry(QtCore.QRect(280, 10, 71, 61))
        self.btn_are.setStyleSheet("border: 1px solid black")
        self.btn_are.setObjectName("btn_am")
        self.btn_are.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_are.text() + " "))
        self.btn_are.clicked.connect(lambda: self.isWidgetReverse(self.widget, self.widget_3))

        """ Are not button """
        self.btn_are_not = QtGui.QPushButton(self.widget_3)
        self.btn_are_not.setGeometry(QtCore.QRect(350, 10, 71, 61))
        self.btn_are_not.setStyleSheet("border: 1px solid black")
        self.btn_are_not.setObjectName("btn_am")
        self.btn_are_not.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_are_not.text() + " "))
        self.btn_are_not.clicked.connect(lambda: self.isWidgetReverse(self.widget, self.widget_3))

        """ Was button """
        self.btn_was = QtGui.QPushButton(self.widget_3)
        self.btn_was.setGeometry(QtCore.QRect(420, 10, 71, 61))
        self.btn_was.setStyleSheet("border: 1px solid black")
        self.btn_was.setObjectName("btn_am")
        self.btn_was.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_was.text() + " "))
        self.btn_was.clicked.connect(lambda: self.isWidgetReverse(self.widget, self.widget_3))

        """ Was not button """
        self.btn_was_not = QtGui.QPushButton(self.widget_3)
        self.btn_was_not.setGeometry(QtCore.QRect(0, 70, 71, 61))
        self.btn_was_not.setStyleSheet("border: 1px solid black")
        self.btn_was_not.setObjectName("btn_am")
        self.btn_was_not.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_was_not.text() + " "))
        self.btn_was_not.clicked.connect(lambda: self.isWidgetReverse(self.widget, self.widget_3))

        """ Were button """
        self.btn_were = QtGui.QPushButton(self.widget_3)
        self.btn_were.setGeometry(QtCore.QRect(70, 70, 71, 61))
        self.btn_were.setStyleSheet("border: 1px solid black")
        self.btn_were.setObjectName("btn_am")
        self.btn_were.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_were.text() + " "))
        self.btn_were.clicked.connect(lambda: self.isWidgetReverse(self.widget, self.widget_3))


        """ Were not button """
        self.btn_were_not = QtGui.QPushButton(self.widget_3)
        self.btn_were_not.setGeometry(QtCore.QRect(140, 70, 71, 61))
        self.btn_were_not.setStyleSheet("border: 1px solid black")
        self.btn_were_not.setObjectName("btn_am")
        self.btn_were_not.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_were_not.text() + " "))
        self.btn_were_not.clicked.connect(lambda: self.isWidgetReverse(self.widget, self.widget_3))

        """ Will button """
        self.btn_will = QtGui.QPushButton(self.widget_3)
        self.btn_will.setGeometry(QtCore.QRect(210, 70, 71, 61))
        self.btn_will.setStyleSheet("border: 1px solid black")
        self.btn_will.setObjectName("btn_am")
        self.btn_will.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_will.text() + " "))
        self.btn_will.clicked.connect(lambda: self.isWidgetReverse(self.widget, self.widget_3))

        """ Will not button """
        self.btn_will_not = QtGui.QPushButton(self.widget_3)
        self.btn_will_not.setGeometry(QtCore.QRect(280, 70, 71, 61))
        self.btn_will_not.setStyleSheet("border: 1px solid black")
        self.btn_will_not.setObjectName("btn_am")
        self.btn_will_not.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_will_not.text() + " "))
        self.btn_will_not.clicked.connect(lambda: self.isWidgetReverse(self.widget, self.widget_3))

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
        self.btn_b2m_phrase.clicked.connect(lambda: self.phrasesWidgetClose(self.widget, self.widget_4))

        """>>>>>>>>>>>> Object name: widget_5 Description: Punctuation widget <<<<<<<<<<"""

        self.widget_5 = QtGui.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(0, 50, 491, 371))
        self.widget_5.setObjectName("widget_5")
        self.widget_5.hide()

        self.btn_fullstop = QtGui.QPushButton(self.widget_5)
        self.btn_fullstop.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_fullstop.setStyleSheet("border: 1px solid black")
        self.btn_fullstop.setObjectName("btn_fullstop")
        self.btn_fullstop.setText(". ")
        self.btn_fullstop.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_fullstop.text()))

        self.btn_comma = QtGui.QPushButton(self.widget_5)
        self.btn_comma.setGeometry(QtCore.QRect(70, 10, 71, 61))
        self.btn_comma.setStyleSheet("border: 1px solid black")
        self.btn_comma.setObjectName("btn_comma")
        self.btn_comma.setText(", ")
        self.btn_comma.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_comma.text()))

        self.btn_qmark = QtGui.QPushButton(self.widget_5)
        self.btn_qmark.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_qmark.setStyleSheet("border: 1px solid black")
        self.btn_qmark.setObjectName("btn_qmark")
        self.btn_qmark.setText("? ")
        self.btn_qmark.clicked.connect(lambda: self.SentenceBuilder.insert(self.btn_qmark.text()))

        self.btn_b2m_qu = QtGui.QPushButton(self.widget_5)
        self.btn_b2m_qu.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_qu.setStyleSheet("border: 1px solid black")
        self.btn_b2m_qu.setObjectName("btn_b2m_qu")
        self.btn_b2m_qu.setText("Return")
        self.btn_b2m_qu.clicked.connect(lambda: self.punctWidgetClose(self.widget, self.widget_5))

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
        self.btn_b2m_do.clicked.connect(lambda: self.doWidgetClose(self.widget, self.do_widget))  

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
        self.btn_b2m_go.clicked.connect(lambda: self.doWidgetClose(self.widget, self.go_widget))  

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
        self.btn_b2m_come.clicked.connect(lambda: self.doWidgetClose(self.widget, self.come_widget)) 

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

        self.btn_b2m_want = QtGui.QPushButton(self.want_widget)
        self.btn_b2m_want.setGeometry(QtCore.QRect(420, 310, 71, 61))
        self.btn_b2m_want.setStyleSheet("border: 1px solid black")
        self.btn_b2m_want.setObjectName("btn_b2m_want")
        self.btn_b2m_want.setText("Return")
        self.btn_b2m_want.clicked.connect(lambda: self.wantWidgetClose(self.widget, self.want_widget))

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
        self.btn_b2m_drink.clicked.connect(lambda: self.drinkWidgetClose(self.widget, self.drink_widget))










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
    
        self.btn_delWord = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_delWord.setObjectName("btn_delWord")
        self.btn_delWord.clicked.connect(lambda: self.SentenceBuilder.backspace())

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

        #self.btn_Iam.setText(QtGui.QApplication.translate("MainWindow", "I am", None, QtGui.QApplication.UnicodeUTF8))

        """ Perform actions on button presses """
        self.btn_add_phrases.clicked.connect(lambda: self.userInput())
        #self.btn_Language.clicked.connect(lambda: self.chooseLang())
        """ Delete phrases from file """
        self.btn_deleteConfig.clicked.connect(lambda: self.redisWipe())
        """ Delete words from bar """
        #self.btn_delWord.clicked.connect(lambda: self.wordDelete())
        """ Pass array into speak parser """
        self.btn_Speak.clicked.connect(lambda: self.config.playSounds(self.phraseList) )
        """ Call verb phrases, to download translated text and append to verb array """
        #self.btn_Iam.clicked.connect(lambda: self.verbPhrases(self.btn_Iam.text()) )

        self.btn_Pron_She.setText(QtGui.QApplication.translate("MainWindow", "She", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_No.setText(QtGui.QApplication.translate("MainWindow", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Look.setText(QtGui.QApplication.translate("MainWindow", "See", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Clear.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Hear.setText(QtGui.QApplication.translate("MainWindow", "Hear", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Time.setText(QtGui.QApplication.translate("MainWindow", "What time\n"
" is it?", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Nouns.setText(QtGui.QApplication.translate("MainWindow", "Nouns", None, QtGui.QApplication.UnicodeUTF8))
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
        self.btn_punctuation.setText(QtGui.QApplication.translate("MainWindow", "Punctuation", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_People.setText(QtGui.QApplication.translate("MainWindow", "People", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_You.setText(QtGui.QApplication.translate("MainWindow", "You", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Translation.setText(QtGui.QApplication.translate("MainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_IDK.setText(QtGui.QApplication.translate("MainWindow", "I don\'t know", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Eat.setText(QtGui.QApplication.translate("MainWindow", "Eat", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Goodbye.setText(QtGui.QApplication.translate("MainWindow", "Goodbye", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Is.setText(QtGui.QApplication.translate("MainWindow", "is/were/was\n"
"/are \n"
"(+negatives)", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_We.setText(QtGui.QApplication.translate("MainWindow", "We", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Questions.setText(QtGui.QApplication.translate("MainWindow", "Questions\n"
" ?", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Wear.setText(QtGui.QApplication.translate("MainWindow", "Wear", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Come.setText(QtGui.QApplication.translate("MainWindow", "Come", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Menu.setText(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Pron_He.setText(QtGui.QApplication.translate("MainWindow", "He", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Drink.setText(QtGui.QApplication.translate("MainWindow", "Drink", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Hungry.setText(QtGui.QApplication.translate("MainWindow", "I\'m hungry", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Verb_Want.setText(QtGui.QApplication.translate("MainWindow", "Want", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Howareyou.setText(QtGui.QApplication.translate("MainWindow", "How are\nyou?", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cmn_Sizes.setText(QtGui.QApplication.translate("MainWindow", "Sizes", None, QtGui.QApplication.UnicodeUTF8))
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


        """ is widget buttons """
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

        """ Open is Widget and close is widget """
    def isWidgetfunc(self, widget, widget_3):
        widget.hide()
        widget_3.show()

    def isWidgetReverse(self, widget, widget_3):
        widget.show()
        widget_3.hide()

        """ Open Phrases Widget and close phrase widget  """
    def phrasesWidgetOpen(self, widget, widget_4):
        widget.hide()
        widget_4.show()

    def phrasesWidgetClose(self, widget, widget_4):
        widget.show()
        widget_4.hide()

        """Open punct. widget and close punct. widget"""
    def punctWidgetOpen(self, widget, widget_5):
        widget.hide()
        widget_5.show()

    def punctWidgetClose(self, widget, widget_5):
        widget.show()
        widget_5.hide()

        """Open do_widget and close do_widget"""
    def doWidgetOpen(self, widget, do_widget):
        widget.hide()
        do_widget.show()

    def doWidgetClose(self, widget, do_widget):
        widget.show()
        do_widget.hide()

        """Open go_Widget and close go_Widget"""
    def goWidgetOpen(self, widget, go_Widget):
        widget.hide()
        go_Widget.show()

    def goWidgetClose(self, widget, go_widget):
        widget.show()
        go_widget.hide()    

        """Open come_Widget and close come_Widget"""
    def comeWidgetOpen(self, widget, come_Widget):
        widget.hide()
        come_Widget.show()

    def comeWidgetClose(self, widget, come_widget):
        widget.show()
        come_widget.hide() 

        """Open want_Widget and close want_Widget"""
    def wantWidgetOpen(self, widget, want_Widget):
        widget.hide()
        want_Widget.show()

    def wantWidgetClose(self, widget, want_widget):
        widget.show()
        want_widget.hide() 

        """Open drink_Widget and close drink_Widget"""
    def drinkWidgetOpen(self, widget, drink_widget):
        widget.hide()
        drink_widget.show()

    def drinkWidgetClose(self, widget, drink_widget):
        widget.show()
        drink_widget.hide() 





    def wordDelete(self):
        self.phraseList.pop()
        self.verbList.pop()

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
        """ Open phrases text and parse through them creating new buttons dynamically """
        with open("phrases.txt", "rb") as f:
            phrases = f.read()
            linePhrase = phrases.split('\n')
        for word in linePhrase:
            """ Dirty hack to move buttons dynamically based off of the word length """
            """ Fix so it is aligned and correct """
            i = len(word) * 25
            self.phraseBtns = QtGui.QPushButton(self.widget)
            self.phraseBtns.setGeometry(QtCore.QRect(0, 10, 71, 61))
            self.phraseBtns.setStyleSheet("background-color: rgb(170, 170, 255);\n" "color: rgb(255, 255, 255);\n" "border: 1px solid black;")
            self.phraseBtns.move(10, i)
            self.phraseBtns.setText(QtGui.QApplication.translate("MainWindow", word, None, QtGui.QApplication.UnicodeUTF8))
            self.phraseBtns.show()
            """ Call passToBar and pass phrases that are then store in an array """
            self.passToBar(self.phraseBtns)

    def verbPhrases(self, text):
        """ Call phrases and download translation of given text """
        self.config.phrases(text)
        """ Pass this text to the speak bar """
        self.passToBar(self.btn_Iam)

    def passToBar(self, phraseBtn):
        """ Pass phrase button text which will then get appended to the relative list """
        phraseBtn.clicked.connect(lambda: self.appendPhrases(phraseBtn.text()) )

    def appendPhrases(self, phrases):
        """ Append button text to the array list for the speak function """
        """ Add check in here to append to correct array - this is dirty and needs fixing """
        if "I am" in phrases:
            self.verbList.append(phrases)
        else:
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

