#import pyaudio
#import wave 
import sys, subprocess

CHUNK = 1024

""" Audio Class to support different Operating Systems """
class Audio():

    def playMp3(self, sound):
        # Pass the mp3 file to the afplay tool, os x specific (Maybe)
        # Maybe place a check here for btnCheck
        #for item in sound[:len(sound)]:
        for phrase in sound:
            subprocess.call(["afplay", "sounds/%s.mp3" % phrase])

    # Implementation to play wave sound files, (also might be redundant)
    def playWave(self, sound):
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

