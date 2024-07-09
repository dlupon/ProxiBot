# autor : LUPON Dylan
# date ; 07 / 09 / 2024

import random
import math
import time
import pyautogui as pauto

class InputManager:

    # MOUSE PROPERTIES
    DEFAULT_SPEED : float = 1000
    MOUSE_LEFT_CLICK : str = "left"
    MOUSE_MIDDLE_CLICK : str = "middle"
    MOUSE_RIGHT_CLICK : str = "right"

    ################################### MOUSE

    # MOVEMENTS
    def MouseMove(pX : float,  pY : float, pSpeed : float = DEFAULT_SPEED) -> float:
        lDistance : float = InputManager.GetDistance(pauto.position(), pauto.Point(pX, pY))
        lDuration : float = lDistance / pSpeed
        pauto.moveTo(pX, pY, duration = lDuration)
        return lDuration

    def MouseMoveInstant(pX : float, pY : float) : pauto.moveTo(pX, pY, duration= 0)

    # CLICK
    def MouseClick(pClickCount : int = 1, pClickType : str = MOUSE_LEFT_CLICK):
        for lClickIndex in range(pClickCount):
            pauto.click(button= pClickType)

    ################################### UTILITIES

    def GetDistance(pPointA : pauto.Point, pPointB : pauto.Point) -> float:
        lCurrentPosition : pauto.Point = pPointA
        lNewPosition : pauto.Point = pPointB
        lDistance : float = math.pow(lCurrentPosition.x - lNewPosition.x, 2) + math.pow(lCurrentPosition.y - lNewPosition.y, 2)
        lDistance : float = math.sqrt(lDistance)
        return lDistance