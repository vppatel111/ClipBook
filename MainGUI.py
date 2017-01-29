from tkinter import * # import everything from tkinter
import pyHook, pyperclip, json
from pyHook import HookManager, GetKeyState, HookConstants
global book
#retrieves the requested element and makes it your clipboard
def retrieving(numPressed):
    if numPressed != 10: #numPressed is a global variable that is equal to what number is pressed
        tmp = pastamasta[book]
        pyperclip.copy(tmp[numPressed - 1])##does not work
        numPressed = 10
    return
#Saves the requested element
def saving(numPressed):
    if numPressed != 10: #numPressed is a global variable that is equal to what number is pressed
        pastamasta[book][numPressed - 1] = pyperclip.paste() ##does not work
        numPressed = 10
    return
#initializes list
def createNewList():
    f = open('flameo.txt', 'r+')
    for pasta in range(10):
        book1.append('')
        book2.append('')
        book3.append('')
        book4.append('')
        book5.append('')

    pastamasta.append(book1)
    pastamasta.append(book2)
    pastamasta.append(book3)
    pastamasta.append(book4)
    pastamasta.append(book5)

    return

#saves the file
def fileSave():
    f = open('flameo.txt','w')
    json.dump(pastamasta,f)
    f.close()
    return

#loads in the users file
def fileOpen():
    f = open('flameo.txt','r')
    tmp = json.load(f)
    bCounter = -1
    counter = 0
    for pastas in tmp:
        bCounter += 1
        counter = 0
        for line in pastas:
            print(bCounter)
            print(line)
            print('-----')
            pastamasta[bCounter][counter] = line
            counter += 1
    print(pastamasta)
    f.close()


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



pastamasta  = [] #holds all the lists
book1 = []
book2 = [] ##each book must be a separate list
book3 = []
book4 = []
book5 = []

createNewList()
fileOpen()
book = 0 ## Variable that holds which book we are using
root = Tk()
main_GUI = MainGUI(root) # Create a GUI object and run it
hm = pyHook.HookManager()
hm.KeyDown = checkPress
hm.HookKeyboard()
root.mainloop()
