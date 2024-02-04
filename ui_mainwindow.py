# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(636, 560)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.savedNotesPage = QWidget()
        self.savedNotesPage.setObjectName(u"savedNotesPage")
        self.verticalLayout_5 = QVBoxLayout(self.savedNotesPage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.yourNotesGroupBox = QGroupBox(self.savedNotesPage)
        self.yourNotesGroupBox.setObjectName(u"yourNotesGroupBox")
        font = QFont()
        font.setPointSize(12)
        self.yourNotesGroupBox.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.yourNotesGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.yourNotesListWidget = QListWidget(self.yourNotesGroupBox)
        self.yourNotesListWidget.setObjectName(u"yourNotesListWidget")

        self.verticalLayout_3.addWidget(self.yourNotesListWidget)


        self.verticalLayout_5.addWidget(self.yourNotesGroupBox)

        self.stackedWidget.addWidget(self.savedNotesPage)
        self.doneNotesPage = QWidget()
        self.doneNotesPage.setObjectName(u"doneNotesPage")
        self.verticalLayout_6 = QVBoxLayout(self.doneNotesPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.doneNotesGroupBox = QGroupBox(self.doneNotesPage)
        self.doneNotesGroupBox.setObjectName(u"doneNotesGroupBox")
        self.doneNotesGroupBox.setFont(font)
        self.verticalLayout_7 = QVBoxLayout(self.doneNotesGroupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.doneNotesListWidget = QListWidget(self.doneNotesGroupBox)
        self.doneNotesListWidget.setObjectName(u"doneNotesListWidget")

        self.verticalLayout_7.addWidget(self.doneNotesListWidget)


        self.verticalLayout_6.addWidget(self.doneNotesGroupBox)

        self.stackedWidget.addWidget(self.doneNotesPage)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textLineLabel = QLabel(self.centralwidget)
        self.textLineLabel.setObjectName(u"textLineLabel")
        font1 = QFont()
        font1.setPointSize(10)
        self.textLineLabel.setFont(font1)

        self.horizontalLayout_3.addWidget(self.textLineLabel)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.messageHistoryBox = QGroupBox(self.centralwidget)
        self.messageHistoryBox.setObjectName(u"messageHistoryBox")
        self.messageHistoryBox.setFont(font1)
        self.messageHistoryBox.setAutoFillBackground(False)
        self.messageHistoryBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.messageHistoryBox.setFlat(False)
        self.messageHistoryBox.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.messageHistoryBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(self.messageHistoryBox)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)


        self.horizontalLayout.addWidget(self.messageHistoryBox)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 25, -1, -1)
        self.newButton = QPushButton(self.centralwidget)
        self.newButton.setObjectName(u"newButton")

        self.verticalLayout_4.addWidget(self.newButton)

        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setEnabled(False)

        self.verticalLayout_4.addWidget(self.editButton)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setEnabled(False)

        self.verticalLayout_4.addWidget(self.deleteButton)

        self.doneButton = QPushButton(self.centralwidget)
        self.doneButton.setObjectName(u"doneButton")
        self.doneButton.setEnabled(False)

        self.verticalLayout_4.addWidget(self.doneButton)

        self.toggleListButton = QPushButton(self.centralwidget)
        self.toggleListButton.setObjectName(u"toggleListButton")

        self.verticalLayout_4.addWidget(self.toggleListButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.helpButton = QPushButton(self.centralwidget)
        self.helpButton.setObjectName(u"helpButton")

        self.horizontalLayout_2.addWidget(self.helpButton)

        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        self.exitButton.setMinimumSize(QSize(125, 0))

        self.horizontalLayout_2.addWidget(self.exitButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.yourNotesGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Your Notes", None))
#if QT_CONFIG(statustip)
        self.yourNotesListWidget.setStatusTip(QCoreApplication.translate("MainWindow", u"This is your notebook page which lists all your notes", None))
#endif // QT_CONFIG(statustip)
        self.doneNotesGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Your Notes Marked as Done", None))
#if QT_CONFIG(statustip)
        self.doneNotesListWidget.setStatusTip(QCoreApplication.translate("MainWindow", u"This is your notebook page which lists all your notes marked as done", None))
#endif // QT_CONFIG(statustip)
        self.textLineLabel.setText(QCoreApplication.translate("MainWindow", u"Text Line:", None))
#if QT_CONFIG(statustip)
        self.lineEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"This is where you type your notes", None))
#endif // QT_CONFIG(statustip)
        self.messageHistoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Message History", None))
#if QT_CONFIG(statustip)
        self.textBrowser.setStatusTip(QCoreApplication.translate("MainWindow", u"This is the window where you can see informative messages", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.newButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Save the note written as a new note", None))
#endif // QT_CONFIG(statustip)
        self.newButton.setText(QCoreApplication.translate("MainWindow", u"New Note", None))
#if QT_CONFIG(statustip)
        self.editButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Replace the selected note with the written one", None))
#endif // QT_CONFIG(statustip)
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"Edit Note", None))
#if QT_CONFIG(statustip)
        self.deleteButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Delete the selected note", None))
#endif // QT_CONFIG(statustip)
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete Note", None))
#if QT_CONFIG(statustip)
        self.doneButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Mark the selected note as done", None))
#endif // QT_CONFIG(statustip)
        self.doneButton.setText(QCoreApplication.translate("MainWindow", u"Mark as Done", None))
#if QT_CONFIG(statustip)
        self.toggleListButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Toggle between your notes and notes marked as done", None))
#endif // QT_CONFIG(statustip)
        self.toggleListButton.setText(QCoreApplication.translate("MainWindow", u"Toggle Note List", None))
        self.helpButton.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(statustip)
        self.exitButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Save the changes and exit program", None))
#endif // QT_CONFIG(statustip)
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"Save and Exit", None))
    # retranslateUi

