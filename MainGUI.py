from tkinter import * # import everything from tkinter
import pyHook, pythoncom, ctypes, pyperclip
import sys
from pyHook import HookManager, GetKeyState, HookConstants
import list_creation,read_new_list
global book
def retrieving(numPressed):
    if numPressed != 10: #numPressed is a global variable that is equal to what number is pressed
        pyperclip.copy(pastamasta[book][numPressed - 1])##does not work
        numPressed = 10
    return

def saving(numPressed):
    if numPressed != 10: #numPressed is a global variable that is equal to what number is pressed
        pastamasta[book][numPressed - 1] = pyperclip.paste() ##does not work
        print(pastamasta)
        numPressed = 10
    return

def createNewList():
    f = open('flameo.txt', 'r+')

    for pasta in range(10):
        pastas.append('')

    for i in range(5):
        pastamasta.append(pastas)

    return

def fileSave():
    listName = 'flameo.txt'
    f = open(listName,'w')
    for pasta in range(len(pastas)):
        f.write(pastas[pasta] + ' ')
    f.close()
    return

def readNewList():
    f.close() #if run into errors, look at this
    global pastas

    #listName = input()    ask for what the list is called
    listName = 'test'    #for the sake of the function
    listName = listName + '.txt'

    f = open(listName, 'r+')
    testString = f.read()
    pastas = testString.split()

    return


def checkPress(event):
    global copy, save, numPressed
    l_ctrl_press = GetKeyState(HookConstants.VKeyToID('VK_CONTROL'))
    l_alt_press = GetKeyState(HookConstants.VKeyToID('VK_MENU'))
    l_shift_press = GetKeyState(HookConstants.VKeyToID('VK_SHIFT'))
    if event.Ascii in range(48,58):
        if l_ctrl_press and l_shift_press:
            numPressed = int(getNum(event))
            retrieving(numPressed)
        if l_alt_press and l_shift_press:
            numPressed = int(getNum(event))
            saving(numPressed)
            fileSave()
    return True

def getNum(event):
    print(event.Key)
    return event.Key

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



pastamasta  = []
pastas = []

createNewList()
print(pastamasta)
book = 0
root = Tk()
main_GUI = MainGUI(root) # Create a GUI object and run it
hm = pyHook.HookManager()
hm.KeyDown = checkPress
hm.HookKeyboard()
root.mainloop()
