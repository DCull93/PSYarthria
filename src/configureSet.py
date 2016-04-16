# Configuration class which sets up vocabulary, words, phrases etc from google trasnlate
from BingTranslator import Translator, AudioSpeaked
from audio import *
import wave
import platform
import redis
import os, glob

class Config():
  """ Initialise the Redis server """
  def __init__(self):
      self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

  def bingInit(self):
      """ Init the API keys for Bing Translate """
      self.client_id = "GroupProjectUni"
      with open("secret.txt", "r") as f:
          self.client_secret = f.readline()

  def langInit(self, lang):
      self.lang = lang

  def redisStorage():
      """ Init Key for Redis """
      #self.r.set(key, text)
      """ Add phrases that the user choices to the key which is then stored in Redis """
      #self.r.set(key, text)
      #self.r.getset('%s' % text, text + '\n')
      #self.r.append(key, text + '\n')
      pass

  def phrases(self, text):
      """ Everytime this func gets called create the phrase and store in Redis with unique key """

      """ Grab the user's phrases/words """
      # This needs to grab the btn that is pressed, may be in wrong scope
      
      """ Grab init keys from bingInit() """
      self.bingInit()
      """ Create translator object with creds """
      translator = Translator(self.client_id, self.client_secret)
      """ Request translation of given text """
      phrase_trans = translator.translate(text, self.lang)
      """ Download MP3 sound or WAVE of translation """
      if platform.system() == "Darwin":
          try:
              url = translator.speak_phrase(phrase_trans, self.lang, "audio/mp3", "MaxQuality")
              """ Download and save audio file """
              AudioSpeaked.download(url, "sounds/", "%s.mp3" % text)
          except OSError:
              print "OS Not supported"
      elif platform.uname()[1] == "debian":
          try:
              url = translator.speak_phrase(phrase_trans, self.lang, "audio/wav", "MaxQuality")
              """ Download and save audio file """
              AudioSpeaked.download(url, "sounds/", "%s.wav" % text)
          except OSError:
              print "OS Not supported"

  def playSounds(self, text):
      """ Create Audio Instance """
      pS = Audio()
      if platform.system() == "Darwin":
          try:
              pS.playMp3(text)
          except OSError:
              print "[*] Operating System no supported..."
      elif platform.uname()[1] == "debian":
          """ Open wave file corresponding to the text input """
          waveSound = wave.open('sounds/%s.wav' % text, 'rb')
          """ Pass wave file format to playWave function for parsing """
          pS.playWave(waveSound)
  
  def keyDel(self, redisDelBtn, p):

      if "Delete Configuration" in redisDelBtn:
          print "[*] Deleting Phrases and MP3s..." 
          """ Remove the phrase buttons """
          for filename in glob.glob('sounds/*.mp3'):
              os.remove(filename)
          for phraseFile in glob.glob('phrases.txt'):
              os.remove(phraseFile)

          print "[*] Deleting Redis key..."
          self.r.delete(p)
