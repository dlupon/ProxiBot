# autor : LUPON Dylan
# date ; 07 / 09 / 2024

import time
import random

from Program import Program
from InputManager import InputManager
import pyautogui
import pyscreeze

image = pyautogui.screenshot()
x,y = pyautogui.locateCenterOnScreen("test.png", confidence = .5)
InputManager.MouseMove(x, y)