# Configuration class which sets up vocabulary, words, phrases etc from google trasnlate
import goslate
import redis
import concurrent.futures

class Config():
  # Initialise the Redis server 
  def __init__(self):
      self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

  def phrases(self, text):
  # Allow users to add word, phrases, lists of phrases, this will be an object in memory
      # Init key for Redis
      phrase = '' 
      # Add phrases that the user choices to the key which is then stored in Redis
      self.r.append(phrase, text + '\n')
      
      # Grab the user's phrases/words
      p  = self.r.get(phrase)
      
      # This translation stuff works now
      '''
      gs = goslate.Goslate()
      for i in p:
          de =  gs.translate(p, 'de')
  
      for line in de:
          print line
      '''

      print p
      
  def keyDel(self, redisDelBtn, p):

      if "Delete Configuration" in redisDelBtn:
          print "[*] Deleting keys cause Sam is a cunt..."
          self.r.delete(p)


      
      
