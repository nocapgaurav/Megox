import subprocess
import eel

# play assistant sound function

@eel.expose
def playAssistantSound():
    music_dir = "www/assets/audio/ui-sound.mp3"
    subprocess.Popen(["afplay", music_dir])