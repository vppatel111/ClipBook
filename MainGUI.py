from tkinter import * # import everything from tkinter

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
        self.pasteViewLbl.grid(row=0, column=1, rowspan=2, pady=20, padx=10)

        self.clearBtn = Button(master, text="Clear")
        self.clearBtn.grid(row=1, column=0, pady=10)

root = Tk()
main_GUI = MainGUI(root) # Create a GUI object and run it
root.mainloop()