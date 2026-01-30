import eel
import os
import time

from engine.features import *
from engine.command import *
playAssistantSound()


eel.init('www')


# Start backend only (do NOT open chrome automatically)
eel.start('index.html', host='localhost', port=8000, block=False, mode=None)

time.sleep(1)

# Open Chrome App Window manually
os.system('open -na "Google Chrome" --args --app="http://localhost:8000/index.html"')

while True:
    eel.sleep(1)