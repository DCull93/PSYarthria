import wave

class Trans():

    def koreanLan(self, btnName):
        lists = ["hello", "btn", "kimchi", "shinbal"]
        # Do translation, i.e. run the sound file for the chosen word
        if btnName in lists:
            # Double check this shit, it's in read only mode, as long as it's hardcoded
            # There should be no way of it fucking up, however I feel uneasy about the 
            # way it's coded
            wave.open('/Users/wes/Desktop/Uni/5th/group_proj/code/PSYarthria/src/sounds/korean/%s.wave' % btnName, 'r')

