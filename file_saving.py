def fileSave():
    f = open('test.txt', 'w')

    for pasta in range(len(pastas)):
        f.write(pastas[pasta] + '\n')
    f.close()
    return
