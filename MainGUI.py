from tkinter import * # import everything from tkinter
import pyHook, pythoncom, ctypes
import sys
from pyHook import HookManager, GetKeyState, HookConstants

def checkPress(event):
    print(event.Key)
    l_ctrl_press = GetKeyState(HookConstants.VKeyToID('VK_CONTROL'))
    l_alt_press = GetKeyState(HookConstants.VKeyToID('VK_MENU'))
    l_shift_press = GetKeyState(HookConstants.VKeyToID('VK_SHIFT'))
    if event.Ascii in range(48,58):
        if l_ctrl_press and l_shift_press:
            numPessed = getNum(event)
            sys.exit("Stopped") ##TODO: NOT STOP

        if l_alt_press and l_shift_press:
            numPressed = getNum(event)
            sys.exit("Stopped") ##TODO: NOT STOP

    return True
# GUI Class
class MainGUI:
    def __init__(self, master):
        self.master = master
        master.title("ClipBook")

        # Declare GUI elements
        self.pasteLb = Listbox(master)
        self.pasteLb.insert(END, "a list entry")
        for item in ["one", "two", "three", "four"]:
            self.pasteLb.insert(END, item)
        self.pasteLb.grid(row=0, column=0, padx=10, pady=10)

        self.pasteViewLbl = Text(master)
        self.pasteViewLbl.insert(END, "Test")
        self.pasteViewLbl.grid(row=0, column=1, pady=20, padx=10)

        self.addBtn = Button(master, text="Add Paste")
        self.addBtn.grid(row=2, column=0, pady=10)

        self.removeBtn = Button(master, text="Remove Paste")
        self.removeBtn.grid(row=3, column=0, pady=10)



root = Tk()
main_GUI = MainGUI(root) # Create a GUI object and run it
hm = pyHook.HookManager()
hm.KeyDown = checkPress
hm.HookKeyboard()
root.mainloop()
