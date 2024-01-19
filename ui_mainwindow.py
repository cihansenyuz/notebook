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
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 605)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelListWidget = QLabel(self.centralwidget)
        self.labelListWidget.setObjectName(u"labelListWidget")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.labelListWidget.setFont(font)

        self.verticalLayout.addWidget(self.labelListWidget)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.labelTextBrowser = QLabel(self.centralwidget)
        self.labelTextBrowser.setObjectName(u"labelTextBrowser")
        font1 = QFont()
        font1.setPointSize(8)
        self.labelTextBrowser.setFont(font1)

        self.verticalLayout.addWidget(self.labelTextBrowser)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.labelLineEdit = QLabel(self.centralwidget)
        self.labelLineEdit.setObjectName(u"labelLineEdit")

        self.verticalLayout.addWidget(self.labelLineEdit)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.newButton = QPushButton(self.groupBox)
        self.newButton.setObjectName(u"newButton")

        self.horizontalLayout.addWidget(self.newButton)

        self.doneButton = QPushButton(self.groupBox)
        self.doneButton.setObjectName(u"doneButton")
        self.doneButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.doneButton)

        self.editButton = QPushButton(self.groupBox)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(self.groupBox)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.deleteButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.exitButton = QPushButton(self.groupBox)
        self.exitButton.setObjectName(u"exitButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        self.exitButton.setMinimumSize(QSize(125, 0))

        self.horizontalLayout_2.addWidget(self.exitButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelListWidget.setText(QCoreApplication.translate("MainWindow", u"YOUR NOTES", None))
        self.labelTextBrowser.setText(QCoreApplication.translate("MainWindow", u"MESSAGE HISTORY", None))
        self.labelLineEdit.setText(QCoreApplication.translate("MainWindow", u"TEXT LINE", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Action Buttons", None))
#if QT_CONFIG(statustip)
        self.newButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Save the note written as a new note", None))
#endif // QT_CONFIG(statustip)
        self.newButton.setText(QCoreApplication.translate("MainWindow", u"New Note", None))
#if QT_CONFIG(statustip)
        self.doneButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Mark the selected note as done", None))
#endif // QT_CONFIG(statustip)
        self.doneButton.setText(QCoreApplication.translate("MainWindow", u"Mark as Done", None))
#if QT_CONFIG(statustip)
        self.editButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Replace the selected note with the written one", None))
#endif // QT_CONFIG(statustip)
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"Edit Note", None))
#if QT_CONFIG(statustip)
        self.deleteButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Delete the selected note", None))
#endif // QT_CONFIG(statustip)
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete Note", None))
#if QT_CONFIG(statustip)
        self.exitButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Save the changes and exit program", None))
#endif // QT_CONFIG(statustip)
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"Save and Exit", None))
    # retranslateUi

