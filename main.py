from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

app = QApplication(sys.argv)

ui = MainWindow()
ui.printNotes()

ui.show()
app.exec()
