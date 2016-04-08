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

import sys, os
from translate import *
from PySide.QtCore import *
from PySide.QtGui import *
from configureSet import *

# Remove this after
qt_app = QApplication(sys.argv)

# Create instances of objects
config = Config()

class gui(QLabel):
  
  def __init__(self):
      trans = Audio()
      # These lables appear to be redundant
      QLabel.__init__(self, "No idea")

      self.sal_lbl = QLabel("yoyoyo", self)

      self.setMinimumSize(QSize(600, 400))
      self.setAlignment(Qt.AlignCenter)
      self.setWindowTitle("Yo")
      
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
      self.myNameLE = QLineEdit(self)
      self.text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter phrases: ')
      if ok: 
          """ This Func needs to pass unique id/text for each btn back to phrase func """
          """ Dynamically create phrase buttons """
          self.phraseBtns = QPushButton('%s' % self.text, self)
          #self.phraseBtns.setObjectName('phraseBtn-%s' % self.text)
          """ Horrible Hack, but dynamically positions buttons """
          i = len(self.text) * 25
          self.phraseBtns.show()
          self.phraseBtns.move(len(self.text), i)

          """ Call sound function whenenver a phrase button is pressed """
          #self.phraseBtns.clicked.connect(lambda: config.phrases(self.text) )

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
