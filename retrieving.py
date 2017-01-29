def retrieving():
    global numPressed, ctrlAlt, pastas
    while ctrlAlt: #ctrlAlt is a global variable that is true if ctrl and alt both pressed
        if numPressed != 10: #numPressed is a global variable that is equal to what number is pressed
            pyperclip.copy(pastas[numPressed - 1])
            numPressed = 10
    return
