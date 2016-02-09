#!/usr/bin/env python
import sys
from translate import *
from PySide.QtCore import *
from PySide.QtGui import *

# Remove this after
qt_app = QApplication(sys.argv)

class gui(QLabel):
  
  def __init__(self):
      trans = Trans()

      QLabel.__init__(self, "No idea")
      self.sal_lbl = QLabel("yoyoyo", self)
      #self.sal_lbl.move(5, 40)
      self.sal_lbl.setAlignment(Qt.AlignLeft)
      self.sals = ['ahoy',
                  'fsdf',
                  'cuntbubble',
                  'tryingg',
                  'fkfkfksdf',
                  'yo',
                  'wassup']
      self.sal = QComboBox(self)
      self.sal.addItems(self.sals)
      #self.sal.move(110, 50)

      self.setMinimumSize(QSize(600, 400))
      self.setAlignment(Qt.AlignCenter)
      self.setWindowTitle("Yo")
      self.btn = QPushButton('Build Greeting', self)
      self.btn.move(5, 40)
      self.btn.clicked.connect(lambda: trans.koreanLan(self.btn.()))


  def run(self):
      self.show()
      qt_app.exec_()

'''
  def cunter():

      qt_app = QApplication(sys.argv)
      label = QLabel("GFuckkfkfkfkfkf!>!>!>!>!>.. ")

      label.show()

      qt_app.exec_()
'''
app = gui()
app.run()
