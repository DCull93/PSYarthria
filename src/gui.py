#!/usr/bin/env python

'''
 - Build a gui bar where options can be passed in
 - Add functionality for different language options (Build logic for this)
 - Add voice functionality 
 - Add gui drag and drop functionanlity
 - Lang choice selection opens new buttons etc



'''
import sys
from translate import *
from PySide.QtCore import *
from PySide.QtGui import *

# Remove this after
qt_app = QApplication(sys.argv)

class gui(QLabel):
  
  def __init__(self):
      QLabel.__init__(self, "No idea")
      self.sal_lbl = QLabel("yoyoyo", self)

      self.setMinimumSize(QSize(600, 400))
      self.setAlignment(Qt.AlignCenter)
      self.setWindowTitle("Yo")
      self.btn = QPushButton('Korean', self)
      self.btn.move(5, 40)
      
      # Click on Korean choice button and load new panel for K words
      self.btn.clicked.connect(self.koreanWindow)
      #self.btn.clicked.connect(lambda: trans.koreanLan(self.btn.text()))

  def koreanWindow(self):
      # Function which displays the words to translate into Korean
      trans = Trans()
      self.koreanBtn = QPushButton('kimchi', self)
      # Check the correct language is chosen
      if "Korean" in self.btn.text():
          self.koreanBtn.show()
          self.koreanBtn.move(5, 100)
          # Call the koreanLan method to translate the chosen word
          # Little bug here, where the "Korean" button still has a signal handler to 
          # the KoreanLan function, which we need to kill
          self.btn.clicked.connect(lambda: trans.koreanLan(self.koreanBtn.text()))

      


  def run(self):
      self.show()
      qt_app.exec_()


app = gui()
app.run()
