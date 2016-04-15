#!/usr/bin/env python

import sys
from PySide import QtCore, QtGui
from configureSet import *
from updater import *

# Remove this after
qt_app = QApplication(sys.argv)

    def __init__(self):
        """ Inititalise instances of objects """
        self.config = Config()
        self.updater = Updater()

        """ Initialise main windows """
        # These lables appear to be redundant
        #QLabel.__init__(self, "No idea")
        #QMainWindow.__init__(self)

        #QWidget.__init__(self)
        """ Call Config Layout """
        #self.configLayout()

        #self.sal_lbl = QLabel("yoyoyo", self)

        self.setMinimumSize(QSize(600, 400))
        #self.setAlignment(Qt.AlignCenter)
        #self.setWindowTitle("Yo")
        
        # Create back and forward buttons
        '''

    '''
        # Can't implement yet, needs work
        self.forBtn = QPushButton('Forward', self)
        self.forBtn.move(100, 200)
        self.backBtn = QPushButton('Back', self)
        self.backBtn.move(300, 250)
        # Create call back -> Need better way of doing this, might have to move everything
        # into widgets or some shit
        self.backBtn.clicked.connect(self.back)
        '''
        '''
        """ Create Main Window """
        self.configLayout()
        self.updaterLayout()
        #self.delPhraseLayout()

    def phraseBarLayout(self, phraseBtn):
        self.mainLayout = QVBoxLayout()
        self.addButton = QPushButton('button to add other widgets')

        self.mainLayout.addWidget(self.addButton)

        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

        self.setLayout(self.mainLayout)


        

    def configLayout(self):
        """ Layout and buttons for the congiguration setup """
        """ Configuration Button """
        self.transSetupBtn = QPushButton('Set Translations up', self)
        self.transSetupBtn.show()
        self.transSetupBtn.move(500, 10)

        """ UserInput Form button """
        self.phraseBtn = QPushButton('Add Phrases', self)
        self.phraseBtn.show()
        self.phraseBtn.move(400, 14)
        self.phraseBtn.clicked.connect(lambda: self.userInput())

        """ Language Choice button """
        self.langChoiceBtn = QPushButton('Language', self)
        self.langChoiceBtn.show()
        self.langChoiceBtn.move(7, 10)
        self.langChoiceBtn.clicked.connect(lambda: self.chooseLang())

        """ Show Phrase Buttons """
        self.showPhraseBtn = QPushButton('Show Phrases', self)
        self.showPhraseBtn.show()
        self.showPhraseBtn.move(400, 60)
        self.showPhraseBtn.clicked.connect(lambda: self.showPhrases())

        self.redisLayout()

    def redisLayout(self):

        """ Redis delete buton - Need to move or delete """
        self.redisDelBtn = QPushButton('Delete Configuration', self)
        self.redisDelBtn.move(10, 50)
        self.redisDelBtn.clicked.connect(lambda: self.redisWipe())

    def updaterLayout(self):
        self.updateSysBtn = QPushButton('Update System', self)
        self.updateSysBtn.move(300, 150)
        self.updateSysBtn.show()
        self.updateAppBtn = QPushButton('Update Application', self)
        self.updateAppBtn.move(300, 200)
        self.updateAppBtn.show()

        """ Call update buttons """
        self.updateSysBtn.clicked.connect(lambda: self.updateOS())
        self.updateAppBtn.clicked.connect(lambda: self.updateApp())

    def delPhraseLayout(self):
        self.delPhraseBtn = QPushButton('Delete Phrases', self)
        self.delPhraseBtn.move(100, 200)
        self.delPhraseBtn.show()
        self.delPhraseBtn.clicked.connect(lambda: self.deletePhrases() )



    '''
    '''
    Back Button Stuff, might remove this too
    def back(self):
        if "Back" in self.backBtn.text():
            self.koreanBtn.show()

        self.phraseBtn = QPushButton('Phrases', self)
        self.phraseBtn.show()
        self.phraseBtn.clicked.connect(lambda: self.userInput)
    '''
    '''
    def userInput(self):
        # Allow user phrase input and pass to config class
        self.text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter phrases: ')
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

    def chooseLang(self):
        self.langText, ok = QInputDialog.getText(self, 'Input Dialog', 'Choose Language: ')
        if ok:
           """ Need to pass this into config """
           self.config.langInit(self.langText) 

    def showPhrases(self):
        """ Open phrases text and parse through them creating new buttons dynamically """
        with open("phrases.txt", "rb") as f:
            phrases = f.read()
            linePhrase = phrases.split('\n')
            for word in linePhrase:
                """ Dirty hack to move buttons dynamically based off of the word length """
                i = len(word) * 25
                self.phraseBtns = QPushButton(word, self)
                self.phraseBtns.show()
                self.phraseBtns.move(10, i)
                """ Call the play phrases function and pass in the phrase button name """
                self.playPhrases(self.phraseBtns)
                """ Call set phrase bar and pass buttons to widget """
                #self.phraseBarLayout(self.phraseBtns)
                

    def playPhrases(self, phraseBtn):
        phraseBtn.clicked.connect(lambda: self.config.playSounds(phraseBtn.text() ))
    
    def deletePhrases(self, delPhrase):
        """ Delete phrase button """
        print delPhrase
        

    def redisWipe(self):
        p = ''
        # call the keyDel function in the config class when the redisDelbtn is pressed
        """ A nice feature, would be to delete a given phrase..."""
        """ To do this, create a function which passes the phraseBtn name and remove from there """
        self.redisDelBtn.clicked.connect(lambda: self.config.keyDel(self.redisDelBtn.text(), p))

    def updateApp(self):
        self.updateAppBtn.clicked.connect(lambda: self.updater.updateApp())

    def updateOS(self):
        self.updateSysBtn.clicked.connect(lambda: self.updater.updateOS())

    def run(self):
        self.show()
        qt_app.exec_()

  #app = Gui()
  #app.run()
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
