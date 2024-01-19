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

#### slot functions ####
def newAction(ui): # new note case, take input, append to the noteList
    newNote = ui.lineEdit.text() + '\n'
    ui.lineEdit.clear()
    noteList.append(newNote)
    ui.printNotes()

def doneAction(ui): # mark done case, take index, remove from the noteList and append to the doneList
    index = ui.listWidget.currentRow()
    tempNote = noteList[index]             # keep it temporarily
    noteList.remove(noteList[index])       # first, remove from the noteList
    doneList.append(tempNote)              # then, append it to doneList
    ui.printNotes()
    ui.resetButtonStates()

def editAction(ui): # edit note case, take index and input, remove old one, insert new one
    newNote = ui.lineEdit.text() + '\n'
    ui.lineEdit.clear()
    index = ui.listWidget.currentRow()
    noteList.remove(noteList[index])
    noteList.insert(index, newNote)
    ui.printNotes()
    ui.resetButtonStates()

def deleteAction(ui): # delete note case, take index, remove from the noteList
    index = ui.listWidget.currentRow()
    noteList.remove(noteList[index])
    ui.printNotes()
    ui.resetButtonStates()

def exitAction(): # quiting process of the program, save the updated lists to txt files
    with open("notes.txt", "w") as file:
        for notes in noteList:
            file.write(str(notes))
    with open("done_notes.txt", "w") as file:
        for notes in doneList:
            file.write(str(notes))
    exit()
###################

### get saved notes from previous run ##
noteList = getNotes("notes.txt")       #
doneList = getNotes("done_notes.txt")  #
########################################