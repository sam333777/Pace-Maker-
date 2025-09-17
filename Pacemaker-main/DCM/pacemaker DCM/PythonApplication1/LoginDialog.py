
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
from UserDatabase import User_Database
from pathlib import Path

class Login_Template(object):
    def __init__(self):
        self._thisDialog = QtWidgets.QDialog()
        self._mainWindowTemplate = Ui_MainWindow()
        self._userDb = User_Database()
        self._userDb.load() #Load in the user database from a file
        
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(824, 550)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(250, 190, 191, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.loginFailLabel = QLabel(self.verticalLayoutWidget)
        self.loginFailLabel.setObjectName(u"loginFailLabel")
        self.loginFailLabel.setEnabled(True)

        self.verticalLayout.addWidget(self.loginFailLabel)

        self.UsernameLayout = QHBoxLayout()
        self.UsernameLayout.setObjectName(u"UsernameLayout")
        self.UsernameLabel = QLabel(self.verticalLayoutWidget)
        self.UsernameLabel.setObjectName(u"UsernameLabel")

        self.UsernameLayout.addWidget(self.UsernameLabel)

        self.UsernameTextEdit = QLineEdit(self.verticalLayoutWidget)
        self.UsernameTextEdit.setObjectName(u"UsernameTextEdit")

        self.UsernameLayout.addWidget(self.UsernameTextEdit)


        self.verticalLayout.addLayout(self.UsernameLayout)

        self.PasswordLayout = QHBoxLayout()
        self.PasswordLayout.setObjectName(u"PasswordLayout")
        self.PasswordLabel = QLabel(self.verticalLayoutWidget)
        self.PasswordLabel.setObjectName(u"PasswordLabel")

        self.PasswordLayout.addWidget(self.PasswordLabel)

        self.PasswordTextEdit = QLineEdit(self.verticalLayoutWidget)
        self.PasswordTextEdit.setObjectName(u"PasswordTextEdit")
        self.PasswordTextEdit.setEchoMode(QLineEdit.Password)

        self.PasswordLayout.addWidget(self.PasswordTextEdit)


        self.verticalLayout.addLayout(self.PasswordLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelButton = QPushButton(self.verticalLayoutWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.LoginPushButton = QPushButton(self.verticalLayoutWidget)
        self.LoginPushButton.setObjectName(u"LoginPushButton")

        self.horizontalLayout.addWidget(self.LoginPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        self.LoginPushButton.setDefault(True)

        QMetaObject.connectSlotsByName(Dialog)


        #Not auto-generated
        self.loginFailLabel.hide()
        self.connectElements()
        # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome!</p>\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please log in</p></body></html>", None))
        self.loginFailLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">Incorrect username/password!</span></p></body></html>", None))
        self.UsernameLabel.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.PasswordLabel.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.LoginPushButton.setText(QCoreApplication.translate("Dialog", u"Login", None))

        

        # retranslateUi





    def connectElements(self): #Connect all UI elements to their appropriate functions
        self.LoginPushButton.clicked.connect(self.checkCredentials)
        self.cancelButton.clicked.connect(lambda: self._thisDialog.close())

    def make(self): #Create and display this dialog to the user
        self.setupUi(self._thisDialog)
        self._thisDialog.show()

    def checkCredentials(self): #Check the username and password entered by the user against all existing users
        nameIn = self.UsernameTextEdit.text() #The name the user entered
        pswdIn = self.PasswordTextEdit.text() #The password the user entered
        for user in self._userDb._db:
            if(user.name == nameIn and user.password == pswdIn):
                self.loginSuccess(user)
                return True

        #Triggers only in the even of login failure
        self.loginFailLabel.show() #This item warns the user that they failed a login
        return False

    
    def loginSuccess(self, user): #Create and display the main window, then destroy this dialog
        self._mainWindowTemplate.make(user)
        self._thisDialog.accept() #Closes the dialog with a signal of "success"
        