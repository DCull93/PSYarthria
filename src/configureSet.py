# Configuration class which sets up vocabulary, words, phrases etc from google trasnlate
from gtts import gTTS
from translate import *
from tempfile import TemporaryFile
import redis
import wave

class Config():
  """ Initialise the Redis server """
  def __init__(self):
      self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

  def phrases(self, pBtnName, text):
      """ Allow users to add word, phrases, lists of phrases, this will be an object in memory """

      """ Create translate instance """
      pS = Audio()
      if text in pBtnName:
          """ Init key for Redis """
          phrase = '' 
          """ Add phrases that the user choices to the key which is then stored in Redis """
          #self.r.append(phrase, text + '\n')
          #self.r.set('%s' % text, text + '\n')
          self.r.set('%s' % pBtnName, '%s' % pBtnName + '\n')
          
          """ Grab the user's phrases/words """
          p  = self.r.get('%s' % pBtnName)
          
          """ Call gtts and translate user input to given language """
          tts = gTTS(text=p, lang='ko')

          """ Pass sound from write_to_reddish method """
          tts.save("%s.mp3" % p)
          
          """ Play Mp3 file - Link each phrase an word to button and run in mem """
          pS.playMp3(p)

          '''
          # This translation stuff works now
          gs = goslate.Goslate()
          for i in p:
              de =  gs.translate(p, 'de')
      
          for line in de:
              print "English phrase %s" % p
              print "Deutch phrase %s" % de
          '''

  def keyDel(self, redisDelBtn, p):

      if "Delete Configuration" in redisDelBtn:
          print "[*] Deleting Redis key..."
          self.r.delete(p)
