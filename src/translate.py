import pyaudio
import wave 
import sys

CHUNK = 1024

class Trans():

    def koreanLan(self, btnName, btnOption):
        lists = ["food", "hotel"]
        # Do translation, i.e. run the sound file for the chosen word
        if btnName in lists and "I want" in btnOption:
            # Double check this shit, it's in read only mode, as long as it's hardcoded
            # There should be no way of it fucking up, however I feel uneasy about the 
            # way it's coded
            # Open option and play link with word
            link = wave.open('sounds/korean/%s.wave' % btnOption, 'r')
            word = wave.open('sounds/korean/%s.wave' % btnName, 'r')

            self.playSound(link)
            self.playSound(word)


    def playSound(self, sound):
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(sound.getsampwidth()),
                        channels=sound.getnchannels(),
                        rate=sound.getframerate(),
                        output=True)
        data = sound.readframes(CHUNK)

        while data != '':
            stream.write(data)
            data = sound.readframes(CHUNK)

        stream.stop_stream()
        stream.close()

        p.terminate()
