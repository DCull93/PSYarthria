import pyaudio
import wave
import sys, subprocess

""" Audio Class to support different Operating Systems """
class Audio():

    def playMp3(self, sound, staticSound):
        # Pass the mp3 file to the afplay tool, os x specific (Maybe)
        # Maybe place a check here for btnCheck
        #for item in sound[:len(sound)]:
        for phrase in sound:
            subprocess.call(["afplay", "sounds/%s.mp3" % phrase])

        for statPhrase in staticSound:
            subprocess.call(["afplay", "sounds/%s.mp3" % statPhrase])

    # Implementation to play wave sound files for Debian Support (Linux)
    def playWave(self, sound, staticSound):
        for statPhrase in staticSound:
            subprocess.call(["afplay", "sounds/%s.wav" % statPhrase])

	    for word in sound:
	        subprocess.call(["aplay", "sounds/%s.wav" % word])
