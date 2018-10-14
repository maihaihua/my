import win32gui
import userInputUtils
import time

import utils.captureWindow

def mhxyHandleFilter(hwnd, mhxyHwndList):
    clsname = win32gui.GetClassName(hwnd)
    title = win32gui.GetWindowText(hwnd)
    if (clsname == "WSGAME"):
        mhxyHwndList.append(hwnd)


def getMhxyWindowHandles():
    mhxyHwndList = []
    deskTopHwnd = win32gui.GetDesktopWindow()
    win32gui.EnumChildWindows(deskTopHwnd, mhxyHandleFilter, mhxyHwndList)
    return mhxyHwndList


def getHwndPosition(hwnd):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    return left, top, right, bottom


handles = getMhxyWindowHandles()
for hwnd in handles:
    (left, top, right, bottom) = getHwndPosition(hwnd)
    print(left, top, right, bottom,right-left,bottom-top)
    utils.captureWindow.window_capture("test.png",hwnd,right-left,bottom-top)
# time.sleep(3)
# userInputUtils.clearPlayers()
# userInputUtils.clearShops()
