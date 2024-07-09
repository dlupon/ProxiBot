# autor : LUPON Dylan
# date ; 07 / 09 / 2024

import math
import pyautogui as pauto

class InputManager:

    class Mouse:

        DEFAULT_SPEED : float = 10
        MOUSE_LEFT_CLICK : str = "left"
        MOUSE_MIDDLE_CLICK : str = "middle"
        MOUSE_RIGHT_CLICK : str = "right"

        # MOVEMENTS
        def MouseMove(pX : float,  pY : float, pSpeed : float = DEFAULT_SPEED):
            lDistance : float = GetDistance(pauto.position(), pauto.Point(pX, pY))
            lDuration : float = lDistance / pSpeed
            pauto.moveTo(pX, pY, duration = lDuration)

        def MouseMoveInstant(pX : float, pY : float) : pauto.moveTo(pX, pY, duration= 0)

        # CLICK
        def MouseClick(pClickCount : int = 1, pClickType : string = MOUSE_LEFT_CLICK):
            for lClickIndex in range(pClickCount):
                pauto.click(button= pClickType)

    class KeyBoard:

        pass

    ################################### UTILITIES

    def GetDistance(pPointA : pauto.Point, pPointB : pauto.Point) -> float:
        lCurrentPosition : pauto.Point = pPointA
        lNewPosition : pauto.Point = pPointB
        lDistance : float = math.pow(lCurrentPosition.x - lNewPosition.x, 2) + math.pow(lCurrentPosition.y - lNewPosition.y, 2)
        lDistance : float = math.sqrt(lDistance)
        return lDistance