from tkinter import * # import everything from tkinter
import pyHook, pyperclip, json
from pyHook import HookManager, GetKeyState, HookConstants
global book, bookMax
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

def savingString(numPressed, string):
    if numPressed != 10: #numPressed is a global variable that is equal to what number is pressed
        pastamasta[book][numPressed - 1] = string ##does not work
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
    global bookMax
    f = open('flameo.txt','r')
    tmp = json.load(f)
    bCounter = -1
    counter = 0
    for pastas in tmp:
        bCounter += 1
        counter = 0
        if bCounter >= 5:
            newChapter()
        for line in pastas:
            pastamasta[bCounter][counter] = line
            counter += 1
    print(pastamasta)
    bookMax = bCounter
    print(bookMax)
    f.close()
    return

def checkPress(event):
    global numPressed, book
    l_ctrl_press = GetKeyState(HookConstants.VKeyToID('VK_CONTROL'))
    l_alt_press = GetKeyState(HookConstants.VKeyToID('VK_MENU'))
    l_shift_press = GetKeyState(HookConstants.VKeyToID('VK_SHIFT'))
    print("Print", event.Key)
    print("Ascii", event.Ascii)
    if event.Key == 'Oem_3':
        if l_shift_press:
            book += 1
            if book >= bookMax:
                book = 0
            fillPastes(main_GUI)


    if event.Key in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]: #Is the list inclusive/Also should work everytime
        print("ascii satisfied")
        if l_ctrl_press and l_shift_press:
            print("ctrl-shift satisfied")
            numPressed = int(getNum(event))
            retrieving(numPressed)
        if l_alt_press and l_shift_press:
            print("alt-shift satisfied")
            numPressed = int(getNum(event))
            saving(numPressed)
            fillPastes(main_GUI)
            fileSave()
    return True

def getNum(event):
    print(event.Key)
    return event.Key

def fillPastes(main_GUI):
    main_GUI.clearPasteLb()
    tmp2 = pastamasta[book]
    for paste in tmp2:
        main_GUI.setPasteLb(paste) #Could add a bit more functionality here (only have short descriptor)


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
        self.pasteLb.bind('<<ListboxSelect>>', self.on_select)

        self.menubar = Menu(master)
        self.prompt1 = Label(master,text="Chapter: " + str(book))
        self.prompt1.grid(row=0, column=0, sticky=N, pady=75)
        self.menubar.add_command(label="Add Chapter",command=self.add_Chapter)
        self.menubar.add_command(label="Next Chapter", command=self.next_chapter)
        self.menubar.add_command(label="Previous Chapter", command=self.prev_chapter)
        self.menubar.add_command(label="Remove Current Chapter", command=self.removeChapter)
        #self.menubar.add_command(label="Remove Chapter")
        self.menubar.add_command(label="Quit", command=root.quit)
        self.menubar.add_command(label="Clear Chapter", command=self.clear_chapter)
        self.master.config(menu=self.menubar)
        self.master.config(menu=self.menubar)

        self.pasteViewLbl = Text(master)
        self.pasteViewLbl.insert(END, "Test")
        self.pasteViewLbl.grid(row=0, column=1, columnspan=3, pady=20, padx=10)

        self.e = Entry(master, width=100)
        self.e.grid(row=2, column=1, columnspan=2)

        self.prompt = Label(master, text="Input which selection to save over:")
        self.prompt.grid(row=3, column=2, sticky=E,padx=65)

        self.e2 = Entry(master, width=10)
        self.e2.grid(row=3, column=2, stick=E)

        self.addBtn = Button(master, text="Add Paste", command=lambda e=self.e, e2=self.e2: self.callback(e, e2))
        self.addBtn.grid(row=2, column=0, pady=10)

        self.removeBtn = Button(master, text="Remove Paste", command=lambda e=self.e, e2=self.e2: self.removePasteLb(e2))
        self.removeBtn.grid(row=3, column=0, pady=10)

    def next_chapter(self):
        global book, bookMax
        book += 1
        if book >= bookMax+1:
            book = bookMax
        print(book)
        fillPastes(main_GUI)
        self.prompt1.config(text="Chapter: " + str(book))

    def prev_chapter(self):
        global book

        if book > 0:
            book -= 1
        fillPastes(main_GUI)
        self.prompt1.config(text="Chapter: " + str(book))

    # Added Code #
    def clear_chapter(self):
        for i in range(1, 10):
            savingString(i, " ")
            fillPastes(main_GUI)
            fileSave()

    def callback(event, e, e2):
        savingString(int(e2.get()), e.get())
        fillPastes(main_GUI)
        fileSave()

    def setPasteLb(self, paste):
        self.pasteLb.insert(END, paste)

    def removePasteLb(self,e2):
        savingString(int(e2.get()),' ')
        fillPastes(main_GUI)
        fileSave()

    def clearPasteLb(self):
        self.pasteLb.delete(0, END)

    def on_select(self, event):
        print("catching event")
        self.pasteViewLbl.delete(1.0, END)
        self.pasteViewLbl.insert(END, (self.pasteLb.get(self.pasteLb.curselection())))

    def removeChapter(self):
        global bookMax, book
        pastamasta.pop(book)
        bookMax -= 1
        book -= 1
        self.prompt1.config(text="Chapter: " + str(book))
        fillPastes(main_GUI)
        fileSave()

    def add_Chapter(self):
        global book,bookMax
        newChapter()
        book = bookMax
        self.prompt1.config(text="Chapter: " + str(book))
        fillPastes(main_GUI)



def newChapter():
    global bookMax
    bookMax += 1
    tmp = list()
    for i in range(10):
        tmp.append(' ')
    pastamasta.append(tmp)

pastamasta  = [] #holds all the lists
book1 = []
book2 = [] ##each book must be a separate list
book3 = []
book4 = []
book5 = []

book = 0 ## Variable that holds which book we are using
bookMax = 5
createNewList()
fileOpen()
root = Tk()
main_GUI = MainGUI(root) # Create a GUI object and run it

fillPastes(main_GUI)

hm = pyHook.HookManager()
hm.KeyDown = checkPress
hm.HookKeyboard()
root.mainloop()
