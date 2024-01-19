################################################
# this file is to manage note files and lists  #
################################################

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

def newAction(ui): # new note case, take input, append to the noteList
    newNote = ui.lineEdit.text() + '\n'
    ui.lineEdit.clear()
    noteList.append(newNote)
    ui.printNotes()

def doneAction(): # mark done case, take index, remove from the noteList and append to the doneList
    index = int(input("Enter the index of the note to mark it done: ")) - 1
    tempNote = noteList[index]             # keep it temporarily
    noteList.remove(noteList[index])        # first, remove from the noteList
    doneList.append(tempNote)              # then, append it to doneList

def editAction(ui): # edit note case, take index and input, remove old one, insert new one
    index = int(input("Enter the index of the note to be edited: ")) - 1        # convert the input to integer since noteList needs integer index. -1 is to offset index 1 to 0.
    newNote = input("Type your edited note and press Enter\n") + '\n'           # added \n to make the file ready for the next note.
    noteList.remove(noteList[index])
    noteList.insert(index, newNote)
    ui.printNotes()

def deleteAction(ui): # delete note case, take index, remove from the noteList
    index = int(input("Enter the index of the note to delete: ")) - 1
    noteList.remove(noteList[index])
    ui.printNotes()

def exitAction(): # quiting process of the program, save the updated lists to txt files
    with open("notes.txt", "w") as file:
        for notes in noteList:
            file.write(str(notes))
    with open("done_notes.txt", "w") as file:
        for notes in doneList:
            file.write(str(notes))
    exit()

### get saved notes from previous run ##
noteList = getNotes("notes.txt")       #
doneList = getNotes("done_notes.txt")  #
########################################