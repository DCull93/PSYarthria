#!/usr/bin/env python

'''
 - Remove deprecation warning about media library
 - Add gender specific vocals
 - Split each bit up into different widgets, for example. options widget(I want to), Language Widget(Korean),
 - Build a gui bar where options can be passed in
 - Add gui drag and drop functionanlity
 - Add ability to go back and forth
 - Can be implemented with if "Back" in self.backBtn.text() and if "Forward" in self.forwardBtn.text()
'''

import sys
from translate import *
from PySide.QtCore import *
from PySide.QtGui import *
from configure import *

# Remove this after
qt_app = QApplication(sys.argv)

# Create instances of objects
config = Config()

class gui(QLabel):
  
  def __init__(self):
      trans = Trans()
      # These lables appear to be redundant
      QLabel.__init__(self, "No idea")

      self.sal_lbl = QLabel("yoyoyo", self)
      
      '''
      # These need work but they're the gender buttons for choosing gender specific sounds to play
      self.maleBtn = QPushButton('Male', self)
      self.maleBtn.move(50, 140)
      self.femaleBtn = QPushButton('Female', self)
      self.femaleBtn.move(60, 240)

      self.maleBtn.clicked.connect(lambda: trans.gender(self.maleBtn.text()))
      '''

      self.setMinimumSize(QSize(600, 400))
      self.setAlignment(Qt.AlignCenter)
      self.setWindowTitle("Yo")
      # Choose language button
      self.koreanBtn = QPushButton('Korean', self)
      self.koreanBtn.move(5, 40)
      
      # Click on lan pref choice button and load new panel for options
      self.koreanBtn.clicked.connect(self.languagePrefWindow)
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

      # UserInput Form button
      self.phraseBtn = QPushButton('Phrases', self)
      self.phraseBtn.show()
      self.phraseBtn.clicked.connect(lambda: self.userInput())

      self.redisDelBtn = QPushButton('Delete Configuration', self)
      self.redisDelBtn.move(10, 50)
      self.redisDelBtn.clicked.connect(lambda: self.redisWipe())

  def languagePrefWindow(self):
      self.koreanBtn.hide()
      # Function which displays the words to translate into Korean
      trans = Trans()
      # Each button represents a word
      # Check the correct language is chosen
      if "Korean" in self.koreanBtn.text():
          # Show prelims, i.e. I want, I feel, etc
          self.optionBtn = QPushButton('I want', self)
          self.optionBtn.show()
          # Hide buttons 
          self.optionBtn.clicked.connect(self.koreanLan)
          # unhide buttons if back pressed etc

  def koreanLan(self):
      trans = Trans()

      if "I want" in self.optionBtn.text():
          self.optionBtn.hide()
          self.foodBtn = QPushButton('food', self)
          self.foodBtn.show()
          self.foodBtn.move(50, 200)
          self.hotelBtn = QPushButton('hotel', self)
          self.hotelBtn.show()
          self.hotelBtn.move(50, 100)
          # Call the koreanLan method to translate the chosen word
          # Little bug here, where the "Korean" button still has a signal handler to 
          # the KoreanLan function, which we need to kill
          self.foodBtn.clicked.connect(lambda: trans.koreanLan(self.foodBtn.text(), self.optionBtn.text()))
          self.hotelBtn.clicked.connect(lambda: trans.koreanLan(self.hotelBtn.text()))


  def back(self):
      if "Back" in self.backBtn.text():
          self.koreanBtn.show()

      self.phraseBtn = QPushButton('Phrases', self)
      self.phraseBtn.show()
      self.phraseBtn.clicked.connect(lambda: self.userInput)

  def userInput(self):
      # Allow user phrase input and pass to config class
      self.myNameLE = QLineEdit(self)
      self.text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter phrases: ')
      if ok:
       config.phrases(str(self.text))

  def redisWipe(self):
      p = ''
      # call the keyDel function in the config class when the redisDelbtn is pressed
      self.redisDelBtn.clicked.connect(lambda: config.keyDel(self.redisDelBtn.text(), p))

  def run(self):
      self.show()
      qt_app.exec_()


app = gui()
app.run()
