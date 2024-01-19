# this is my mainwindow class

from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("NoteBook v2.0")