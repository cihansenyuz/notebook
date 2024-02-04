# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(850, 329)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.helpWelcomeLabel = QLabel(Dialog)
        self.helpWelcomeLabel.setObjectName(u"helpWelcomeLabel")
        font = QFont()
        font.setPointSize(18)
        self.helpWelcomeLabel.setFont(font)
        self.helpWelcomeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.helpWelcomeLabel)

        self.helpInstructionsLabel = QLabel(Dialog)
        self.helpInstructionsLabel.setObjectName(u"helpInstructionsLabel")
        font1 = QFont()
        font1.setPointSize(12)
        self.helpInstructionsLabel.setFont(font1)

        self.verticalLayout.addWidget(self.helpInstructionsLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ready2goButton = QPushButton(Dialog)
        self.ready2goButton.setObjectName(u"ready2goButton")
        self.ready2goButton.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.ready2goButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Instructions About Notebook Application", None))
        self.helpWelcomeLabel.setText(QCoreApplication.translate("Dialog", u"Welcome to Notebook Application!", None))
        self.helpInstructionsLabel.setText(QCoreApplication.translate("Dialog", u"Instructions:\n"
"\n"
"Enter a note to text line and hit 'New Note' button to add it\n"
"To mark an existing note as done, select the note first, then hit the 'Mark as Done' button.\n"
"To edit an existing note, select the note first, then type your edited note in the text line, and hit the 'Edit Note' button.\n"
"To delete a note, select the note first, then hit the 'Delete Note' button.\n"
"\n"
"To toggle between your current saved notes and old notes that are marked as done, hit the 'Toggle Note List' button\n"
"\n"
"Once your are all done, click on the save and exit button to save all changes onto your disk!", None))
        self.ready2goButton.setText(QCoreApplication.translate("Dialog", u"Ready to Go!", None))
    # retranslateUi

