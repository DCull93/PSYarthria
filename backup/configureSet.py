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

  def phrases(self, text):
      """ Allow users to add word, phrases, lists of phrases, this will be an object in memory """

      """ Create translate instance """
      pS = Audio()

      """ Init key for Redis """
      #phrase = id(text) + len(text)
      key = ''
      """ Add phrases that the user choices to the key which is then stored in Redis """
      #self.r.set(text, text)
      #self.r.getset('%s' % text, text + '\n')
      self.r.append(key, text + '\n')
          
      """ Grab the user's phrases/words """
      # This needs to grab the btn that is pressed, may be in wrong scope
      p  = self.r.get(key)
      print p
          
      """ Call gtts and translate phrase to given language """
      tts = gTTS(text=p, lang='ko')

      """ Save sound from write_to_reddish method """
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
          print "[*] Deleting MP3s..."
          os.remove('*mp3')
