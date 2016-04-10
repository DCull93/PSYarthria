#!/usr/bin/env python

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from configureSet import *

# Remove this after
qt_app = QApplication(sys.argv)

# Create instances of objects
config = Config()

class Gui(QMainWindow):
  
  def __init__(self):
      """ Initialise main windows """
      # These lables appear to be redundant
      #QLabel.__init__(self, "No idea")
      QMainWindow.__init__(self)

      #QWidget.__init__(self)
      """ Call Config Layout """
      #self.configLayout()

      #self.sal_lbl = QLabel("yoyoyo", self)

      self.setMinimumSize(QSize(600, 400))
      #self.setAlignment(Qt.AlignCenter)
      #self.setWindowTitle("Yo")
      
      # Create back and forward buttons
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

      """ Create Main Window """
      self.configLayout()

  def configLayout(self):
      """ Layout and buttons for the congiguration setup """
      """ Configuration Button """
      self.transSetupBtn = QPushButton('Set Translations up', self)
      self.transSetupBtn.show()
      self.transSetupBtn.move(500, 10)

      """ UserInput Form button """
      self.phraseBtn = QPushButton('Phrases', self)
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

      self.chooseLang()
      self.showPhrases()
      self.redisLayout()

  def redisLayout(self):

      """ Redis delete buton - Need to move or delete """
      self.redisDelBtn = QPushButton('Delete Configuration', self)
      self.redisDelBtn.move(10, 50)
      self.redisDelBtn.clicked.connect(lambda: self.redisWipe())

  '''
  Back Button Stuff, might remove this too
  def back(self):
      if "Back" in self.backBtn.text():
          self.koreanBtn.show()

      self.phraseBtn = QPushButton('Phrases', self)
      self.phraseBtn.show()
      self.phraseBtn.clicked.connect(lambda: self.userInput)
  '''
  
  def userInput(self):
      # Allow user phrase input and pass to config class
      self.text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter phrases: ')
      if ok: 
          # Save phrases to a file, I hate doing this so it needs resolving
          with open("phrases.txt", "ab") as f:
              f.write(self.text + '\n')

          """ Call phrases to download sounds """
          config.phrases(self.text)

  def chooseLang(self):
      self.langText, ok = QInputDialog.getText(self, 'Input Dialog', 'Choose Language: ')
      if ok:
         """ Need to pass this into config """
         config.langInit(self.langText) 

  def showPhrases(self):
      '''
      try and pass the text, buttons etc and do calls and signal handling here 
      '''
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

  def playPhrases(self, phraseBtn):
      phraseBtn.clicked.connect(lambda: config.playSounds(phraseBtn.text() ))
      

  def redisWipe(self):
      p = ''
      # call the keyDel function in the config class when the redisDelbtn is pressed
      self.redisDelBtn.clicked.connect(lambda: config.keyDel(self.redisDelBtn.text(), p))

  def run(self):
      self.show()
      qt_app.exec_()

app = Gui()
app.run()
