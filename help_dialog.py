from ui_help_dialog import Ui_Dialog
from PySide6.QtWidgets import QDialog

class DialogWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ready2goButton.clicked.connect(self.onReady2GoButtonClicked)
        self.show()

    def onReady2GoButtonClicked(self):
        self.destroy()