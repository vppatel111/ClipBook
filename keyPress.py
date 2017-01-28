import pyHook, pythoncom
import sys
from pyHook import HookManager, GetKeyState, HookConstants
numPressed = 10
def checkPress(event):
    l_ctrl_press = GetKeyState(HookConstants.VKeyToID('VK_CONTROL'))
    l_alt_press = GetKeyState(HookConstants.VKeyToID('VK_MENU'))
    l_shift_press = GetKeyState(HookConstants.VKeyToID('VK_SHIFT'))
    if event.Ascii in range(48,58):
        if l_ctrl_press and l_shift_press:
            numPessed = getNum(event)
            sys.exit("Stopped") ##TODO: NOT STOP

        if l_alt_press and l_shift_press:
            numPressed = getNum(event)
            sys.exit("Stopped")
    return True

def getNum(event):
    print(event.Key)
    return event.Key

#LOOPS and listens for global input
#Recieves notification of global input
hm = pyHook.HookManager()
hm.KeyDown = checkPress
hm.HookKeyboard()
pythoncom.PumpMessages()
