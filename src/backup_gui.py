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
        MainWindow.resize(894, 742)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 50, 491, 671))
        self.widget.setObjectName("widget")
        
        """ Sets the Add Phrases button in """
        self.btn_addPhrases = QtGui.QPushButton(self.widget)
        self.btn_addPhrases.setGeometry(QtCore.QRect(140, 10, 71, 61))
        self.btn_addPhrases.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.btn_addPhrases.setObjectName("btn_AddPhrases")
        
        """ Add static Phrases """
        self.btn_Iam = QtGui.QPushButton(self.widget)
        self.btn_Iam.setGeometry(QtCore.QRect(160, 20, 81, 71))
        self.btn_addPhrases.setStyleSheet("background-color: rgb(180, 180, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.btn_addPhrases.setObjectName("btn_Iam")

        self.btn_deleteConfig = QtGui.QPushButton(self.widget)
        self.btn_deleteConfig.setGeometry(QtCore.QRect(260, 10, 71, 61))
        self.btn_deleteConfig.setStyleSheet("border: 1px solid black")

        self.btn_Language = QtGui.QPushButton(self.widget)
        self.btn_Language.setGeometry(QtCore.QRect(0, 10, 71, 61))
        self.btn_Language.setStyleSheet("border: 1px solid black")
        self.btn_Language.setObjectName("btn_Language")

        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(14, 0, 891, 61))
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

        self.horizontalLayout.addWidget(self.btn_delWord)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """ Add text to buttons in Main window Widgets """
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Language.setText(QtGui.QApplication.translate("MainWindow", "Language", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Speak.setText(QtGui.QApplication.translate("MainWindow", "Speak", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_addPhrases.setText(QtGui.QApplication.translate("MainWindow", "Add Phrases", None, QtGui.QApplication.UnicodeUTF8))

        self.btn_delWord.setText(QtGui.QApplication.translate("MainWindow", "Delete \n" " Word", None, QtGui.QApplication.UnicodeUTF8))

        self.btn_deleteConfig.setText(QtGui.QApplication.translate("MainWindow", "Delete Configuration", None, QtGui.QApplication.UnicodeUTF8))

        self.btn_Iam.setText(QtGui.QApplication.translate("MainWindow", "I am", None, QtGui.QApplication.UnicodeUTF8))

        """ Perform actions on button presses """
        self.btn_addPhrases.clicked.connect(lambda: self.userInput())
        self.btn_Language.clicked.connect(lambda: self.chooseLang())
        """ Delete phrases from file """
        self.btn_deleteConfig.clicked.connect(lambda: self.redisWipe())
        """ Delete words from bar """
        self.btn_delWord.clicked.connect(lambda: self.wordDelete())
        """ Pass array into speak parser """
        self.btn_Speak.clicked.connect(lambda: self.config.playSounds(self.phraseList) )
        """ Call verb phrases, to download translated text and append to verb array """
        self.btn_Iam.clicked.connect(lambda: self.verbPhrases(self.btn_Iam.text()) )

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

