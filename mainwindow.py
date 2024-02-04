################################################
# this file is created by me                   #
# to inherete the file generated by pyside-uic #
################################################

from PySide6.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow
import note_management as noteManager

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("NoteBook v2.0")
        self.printNotes()
        self.lineEdit.setText("Type your new note here")
        self.textBrowser.append("Welcome to Notebook Application!\nEnter a note to text line and hit 'New Note' button to add it.\nTo mark an existing note as done, select the note first, then hit the 'Mark as Done' button.\nTo edit an existing note, select the note first, then type your edited note in the text line, and hit the 'Edit Note' button.\nTo delete a note, select the note first, then hit the 'Delete Note' button.\nOnce your are all done, click on the save and exit button to save all changes onto your disk!")

        ########## signals and slots connections ##################################
        self.yourNotesListWidget.itemSelectionChanged.connect(self.onItemSelectionChanged) #
        self.newButton.clicked.connect(lambda: noteManager.newAction(self))       #
        self.doneButton.clicked.connect(lambda:noteManager.doneAction(self))      #
        self.editButton.clicked.connect(lambda: noteManager.editAction(self))     #
        self.deleteButton.clicked.connect(lambda: noteManager.deleteAction(self)) #
        self.exitButton.clicked.connect(noteManager.exitAction)                   #
        self.toggleListButton.clicked.connect(self.onToggleListButtonClicked)
        ###########################################################################

    def printNotes(self):
        self.yourNotesListWidget.clear()
        self.doneNotesListWidget.clear()

        noteIndex = 1
        for notes in noteManager.noteList:
            notes = str(noteIndex) + ") " + notes
            self.yourNotesListWidget.addItem(notes)
            noteIndex = noteIndex + 1

        noteIndex = 1
        for notes in noteManager.doneList:
            notes = str(noteIndex) + ") " + notes
            self.doneNotesListWidget.addItem(notes)
            noteIndex = noteIndex + 1

    def onItemSelectionChanged(self):
        self.newButton.setEnabled(False)
        self.doneButton.setEnabled(True)
        self.editButton.setEnabled(True)
        self.deleteButton.setEnabled(True)
        selectedItem = self.yourNotesListWidget.currentRow()
        self.lineEdit.setText(noteManager.noteList[selectedItem])

    def resetButtonStates(self):
        self.newButton.setEnabled(True)
        self.doneButton.setEnabled(False)
        self.editButton.setEnabled(False)
        self.deleteButton.setEnabled(False)

    def onToggleListButtonClicked(self):
        if self.stackedWidget.currentIndex() == 0:
            self.stackedWidget.setCurrentIndex(1)
            # disable all buttons since they are functional on the first page
            self.newButton.setEnabled(False)
            self.doneButton.setEnabled(False)
            self.editButton.setEnabled(False)
            self.deleteButton.setEnabled(False)
        elif self.stackedWidget.currentIndex() == 1:
            self.stackedWidget.setCurrentIndex(0)
            self.resetButtonStates()