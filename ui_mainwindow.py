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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.newButton = QPushButton(self.centralwidget)
        self.newButton.setObjectName(u"newButton")

        self.horizontalLayout.addWidget(self.newButton)

        self.doneButton = QPushButton(self.centralwidget)
        self.doneButton.setObjectName(u"doneButton")
        self.doneButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.doneButton)

        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.deleteButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

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

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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

