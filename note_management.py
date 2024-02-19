################################################
# this file is to manage note files and lists  #
################################################

def getNotes(sourceFileName: str) -> list:
    '''
    This function reads the file and creates a list from notes, returns the list

    Parameters:
    - sourceFileName (str): path to the file

    Return:
    list: list of the notes in the file
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
def newAction(ui):
    '''
    Slot method to handle click action on newButton (Adding a new note)

    Gets the content in lineEdit, appends it to noteList and updates QListWidgets

    Parameters:
    - ui: an instance of MainWindow that contains newButton
    '''
    newNote = ui.lineEdit.text() + '\n'
    ui.lineEdit.clear()
    noteList.append(newNote)
    ui.printNotes()
    ui.textBrowser.append("Action: New note is added.")

def doneAction(ui):
    '''
    Slot method to handle click action on doneButton (Marking a note as done)

    Takes current index of yourNotesListWidget, removes related note from the noteList,
    appends it to the doneList, and updates QListWidgets

    Parameters:
    - ui: an instance of MainWindow that contains newButton
    '''
    ui.lineEdit.clear()
    index = ui.yourNotesListWidget.currentRow()
    tempNote = noteList[index]             # keep it temporarily
    noteList.remove(noteList[index])       # first, remove from the noteList
    doneList.append(tempNote)              # then, append it to doneList
    ui.printNotes()
    ui.resetButtonStates()
    tempStr = "Action: " + str(index+1) + ". note is marked as 'done'."
    ui.textBrowser.append(tempStr)
    tempStr = str(len(doneList)) + " note(s) are saved as done..."
    ui.textBrowser.append(tempStr)

def editAction(ui):
    '''
    Slot method to handle click action on editButton (Editing an existing note)

    Takes current index of yourNotesListWidget and content of lineEdit,
    removes related note from the noteList, inserts new content to the list, and updates QListWidgets

    Parameters:
    - ui: an instance of MainWindow that contains newButton
    '''
    newNote = ui.lineEdit.text() + '\n'
    ui.lineEdit.clear()
    index = ui.yourNotesListWidget.currentRow()
    noteList.remove(noteList[index])
    noteList.insert(index, newNote)
    ui.printNotes()
    ui.resetButtonStates()
    tempStr = "Action: " + str(index+1) + ". note is edited."
    ui.textBrowser.append(tempStr)

def deleteAction(ui):
    '''
    Slot method to handle click action on deleteButton (Deleting existing note)

    Takes current index of QListWidget according to current page,
    removes related note from the noteList, and updates QListWidgets

    Parameters:
    - ui: an instance of MainWindow that contains newButton
    '''
    if ui.stackedWidget.currentIndex() == 0:
        index = ui.yourNotesListWidget.currentRow()
        noteList.remove(noteList[index])
        ui.printNotes()
        ui.resetButtonStates()
        tempStr = "Action: " + str(index+1) + ". note is deleted."
        ui.textBrowser.append(tempStr)
    elif ui.stackedWidget.currentIndex() == 1:
        index = ui.doneNotesListWidget.currentRow()
        doneList.remove(doneList[index])
        ui.printNotes()
        ui.deleteButton.setEnabled(False)
        tempStr = "Action: " + str(index+1) + ". note is deleted."
        ui.textBrowser.append(tempStr)

def exitAction(): # quiting process of the program, save the updated lists to txt files
    '''
    Slot method to handle click action on exitButton (Quiting the application)

    Opens txt files, writes both note lists into the file, and exits the program
    '''
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