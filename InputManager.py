# autor : LUPON Dylan
# date : 07 / 09 / 2024

import math
import pyautogui
from pyautogui import Point

class InputManager:

    ################################### VARIABLES

    # MOUSE PROPERTIES
    DEFAULT_SPEED : float = 1000
    MOUSE_LEFT_CLICK : str = "left"
    MOUSE_MIDDLE_CLICK : str = "middle"
    MOUSE_RIGHT_CLICK : str = "right"

    mouseIsClicking : bool = False

    ################################### MOUSE

    # MOVEMENTS
    def MouseMove(pX : float,  pY : float, pSpeed : float = DEFAULT_SPEED) -> float:
        lDistance : float = InputManager.GetDistance(pyautogui.position(), Point(pX, pY))
        lDuration : float = lDistance / pSpeed
        pyautogui.moveTo(pX, pY, duration = lDuration)
        return lDuration
    
    def MouseMove(pPoint : Point, pSpeed : float = DEFAULT_SPEED) -> float: return InputManager.MouseMove(Point.x, Point.y, pSpeed)

    def MouseMoveInstant(pX : float, pY : float) : pyautogui.moveTo(pX, pY, duration= 0)

    def MouseMoveInstant(pPoint : Point) -> float: InputManager.MouseMoveInstant(Point.x, Point.y)

    # CLICK
    def MouseClick(pClickCount : int = 1, pClickType : str = MOUSE_LEFT_CLICK):
        for lClickIndex in range(pClickCount):
            pyautogui.click(button= pClickType)

    ################################### MOUSE
    
    def KeyShortCut(*pKeys : str): pyautogui.shortcut(*pKeys)
    
    def KeyType(pInput : str): pyautogui.typewrite(pInput)

    ################################### UTILITIES

    def GetDistance(pPointA : Point, pPointB : Point) -> float:
        lCurrentPosition : Point = pPointA
        lNewPosition : Point = pPointB
        lDistance : float = math.pow(lCurrentPosition.x - lNewPosition.x, 2) + math.pow(lCurrentPosition.y - lNewPosition.y, 2)
        lDistance : float = math.sqrt(lDistance)
        return lDistance