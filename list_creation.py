def createNewList():
    #listName = input()    ask for what they want the list to be called
    listName = 'flameo'    #for the sake of the function
    listName = listName + '.txt'
    f = open(listName, 'w')

    for pasta in range(len(pastas)):
        f.write('\n')
    f.close()
    return

pastas = []
for i in range(10):
    pastas.append('')
