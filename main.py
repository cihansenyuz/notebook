### functions ######
def getNotes(sourceFileName):
    '''(string) -> list
    This function reads the file and creates a list from the data, returns the list
    '''
    try:
        with open(sourceFileName, "r") as file:
            tempList = []
            for line in file:
                tempList.append(line)
        return tempList
    except FileNotFoundError:
        print("Warning: No file found, if you had saved notes, check whether the directory is correct\n")
    except Exception:
        print("Error: Something went wrong, please try again\n")

def printNotes():
    '''(none) -> none
    This function prints all the notes in the list
    '''
    print("###YOUR NOTES###")
    counter = 1
    for notes in noteList:
        print(counter, end=") ")
        print(notes, end='')
        counter = counter + 1
    print("################")
####################

###get saved notes from previous run###
noteList = getNotes("notes.txt")

#######################################

###ask user action & editing the list#########
while 1:
    printNotes()
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
    elif selection == '0':
        with open("notes.txt", "w") as file:
            for notes in noteList:
                file.write(notes)
        exit()
    else:
        input("ERROR: Not a valid action, please try again...\Enter to continue")
    
#############################################
