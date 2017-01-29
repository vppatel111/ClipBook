def createNewList():
    f.close() #if we run into errors, look at this
    #listName = input()    ask for what they want the list to be called
    listName = 'flameo'    #for the sake of the function
    listName = listName + '.txt'
    f = open(listName, 'r+')

    pastas = []
    for pasta in range(10):
        pastas.append('')

    for pasta in range(len(pastas)):
        f.write(pastas[pasta])

    return
