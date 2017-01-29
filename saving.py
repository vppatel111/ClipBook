def saving():
    global numPressed, ctrlShift, pastas
    while ctrlShift: #ctrlShift is a global variable that is true if ctrl and shift both pressed
        if numPressed != 10: #numPressed is a global variable that is equal to what number is pressed
            pastas[numPressed - 1] = pyperclip.paste()
            numPressed = 10
    return
