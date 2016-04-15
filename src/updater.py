import subprocess
import platform

class Updater():

    def updateOS(self):
        """ Check for type of OS and then decide update procedure (System update) """
        if platform.system() == "Darwin":
            print "[*] Updating via brew..."
            try:
                subprocess.check_call(["brew", "update"])
                subprocess.check_call(["brew", "upgrade"])
            except OSError:
                print "[*] Error can't find brew package manager, might not be installed..."
        elif platform.system() == "Windows":
            print "[*] Updating via Windows update manager..."

    def updateApp(self):  
        try: 
            print "[*] Updating Application, please be patient..."
           # subprocess.check_call(["git", "pull"])
            print "[*] Update complete, restarting application now..."
            quit()
        except OSError:
            print "[*] Error can't find git, might not be installed..."

      
