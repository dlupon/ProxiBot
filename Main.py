# autor : LUPON Dylan
# date ; 07 / 09 / 2024

import time
import random

from InputManager import InputManager as IP

for i in range(25):
    time.sleep(IP.MouseMove(random.randint(0, 1920), random.randint(0, 1080)))