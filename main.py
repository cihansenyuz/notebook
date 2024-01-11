### functions ######
def getNotes(sourceFileName):
    '''(string) -> list
    This function reads the file and creates a list from the data, returns the list
    '''
    file = open(sourceFileName, "r")
    tempList = []
    for line in file:
        tempList.append(line)
    file.close()
    return tempList

def printNotes():
    '''(none) -> none
    This function prints all the notes in the list
    '''
    print("###YOUR NOTES###")
    counter = 1
    for notes in noteList:
        print(counter, end=" ")
        print(notes, end='')
        counter = counter + 1
    print("################")
####################

###get saved notes from previous run###
noteList = getNotes("notes.txt")
printNotes()
#######################################

###ask user action & editing the list#########
while 1:
    selection = input("\n1: New note\n2: Edit note\n3: Delete note\n0: Exit\nSELECT AN ACTION: ")
    if selection == '1':
        newNote = input("Type your note and press Enter\n") + '\n'
        noteList.append(newNote)
    elif selection == '2':
        index = int(input("Enter the index of the note to be edited: ")) - 1
        newNote = input("Type your edited note and press Enter\n") + '\n'
        noteList.remove(noteList[index])
        noteList.insert(index, newNote)
    elif selection == '3':
        index = int(input("Enter the index of the note to be deleted: ")) - 1
        noteList.remove(noteList[index])
    printNotes()
#############################################
        
###save the edited list to file & close it###
    if selection == '0':
        file = open("notes.txt", "w")
        for notes in noteList:
            file.write(notes)
        file.close()
        exit()
#############################################

