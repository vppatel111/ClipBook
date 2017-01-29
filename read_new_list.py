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
