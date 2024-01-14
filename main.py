### functions ######
def getNotes(sourceFileName):
    '''(string) -> list
    This function reads the file and creates a list from the data, returns the list
    '''
    tempList = []
    try:
        with open(sourceFileName, "r") as file:
            for line in file:
                tempList.append(line)
    except FileNotFoundError:
        print("Warning: No file(s) found, if you had saved notes, check whether the directory is correct\n")
    except Exception:
        print("Error: Something went wrong, please try again\n")
    return tempList

def printNotes():
    '''(int) -> none
    This function prints all the notes in the list with index
    '''
    print("###YOUR NOTES###")
    counter = 1
    for notes in noteList:
        print(counter, end=") ")
        print(notes, end='')
        counter = counter + 1
    print("################")
    print(len(doneList), "note(s) marked 'done'")
    
####################

###get saved notes from previous run###
noteList = getNotes("notes.txt")
doneList = getNotes("done_notes.txt")

#######################################

###ask user action & editing the list#########
while 1:
    printNotes()
    selection = input("\n1: New note\n2: Edit note\n3: Delete note\n4: Mark a note 'done'\n0: Exit\nSELECT AN ACTION: ")
    if selection == '1':        # new note case, take input, append to the noteList
        newNote = input("Type your note and press Enter\n") + '\n'
        noteList.append(newNote)
    elif selection == '2':      # edit note case, take index and input, remove old one, insert new one
        index = int(input("Enter the index of the note to be edited: ")) - 1        # convert the input to integer since noteList needs integer index. -1 is to offset index 1 to 0.
        newNote = input("Type your edited note and press Enter\n") + '\n'           # added \n to make the file ready for the next note.
        noteList.remove(noteList[index])
        noteList.insert(index, newNote)
    elif selection == '3':      # delete note case, take index, remove from the noteList
        index = int(input("Enter the index of the note to delete: ")) - 1
        noteList.remove(noteList[index])
    elif selection == '4':      # mark done case, take index, remove from the noteList and append to the doneList
        index = int(input("Enter the index of the note to mark it done: ")) - 1
        tempNote = noteList[index]      # keep it temporarily
        noteList.remove(noteList[index])# first, remove from the noteList
        doneList.append(tempNote)       # then, append it to doneList
    elif selection == '0':      # quiting process of the program, save the updated lists to txt files
        with open("notes.txt", "w") as file:
            for notes in noteList:
                file.write(str(notes))
        with open("done_notes.txt", "w") as file:
            for notes in doneList:
                file.write(str(notes))
        exit()
    else:
        input("ERROR: Not a valid action, please try again...\Enter to continue")
    
#############################################
