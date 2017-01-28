from tkinter import * # import everything from tkinter

# GUI Class
class MainGUI:
    def __init__(self, master):
        self.master = master
        master.title("ClipBook")

        # Declare GUI elements
        self.listbox = Listbox(master)
        self.listbox.insert(END, "a list entry")
        for item in ["one", "two", "three", "four"]:
            self.listbox.insert(END, item)
        self.listbox.pack()

root = Tk()
main_GUI = MainGUI(root) # Create a GUI object and run it
root.mainloop()