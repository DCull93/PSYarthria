# Configuration class which sets up vocabulary, words, phrases etc from google trasnlate
from gtts import gTTS
from translate import *
import redis
import os, glob

class Config():
  """ Initialise the Redis server """
  def __init__(self):
      self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

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
      
      """ Create translate instance """
      pS = Audio()

      """ Grab the user's phrases/words """
      # This needs to grab the btn that is pressed, may be in wrong scope
      print text

      """ Call gtts and translate phrase to given language """
      tts = gTTS(text=text, lang=self.lang)

      """ Save sound from write_to_reddish method """
      tts.save("%s.mp3" % text)

      pS.playMp3(text)
  
  def keyDel(self, redisDelBtn, p):

      if "Delete Configuration" in redisDelBtn:
          print "[*] Deleting Phrases and MP3s..." 
          for filename in glob.glob('*.mp3'):
              os.remove(filename)
          for phraseFile in glob.glob('phrases.txt'):
              os.remove(phraseFile)

          print "[*] Deleting Redis key..."
          self.r.delete(p)
