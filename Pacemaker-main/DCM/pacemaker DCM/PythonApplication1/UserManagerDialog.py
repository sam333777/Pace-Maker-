from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from User import AccessType
from UserDatabase import User_Database


class User_Manager_Template(object):
    def __init__(self):
        self._thisDialog = QtWidgets.QDialog()
        self._userDB = User_Database()
        self._userDB.load() #Load in all the user data

    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(401, 330)
        self.deleteUserButton = QPushButton(Dialog)
        self.deleteUserButton.setObjectName(u"deleteUserButton")
        self.deleteUserButton.setGeometry(QRect(100, 300, 93, 28))
        self.addUserButton = QPushButton(Dialog)
        self.addUserButton.setObjectName(u"addUserButton")
        self.addUserButton.setGeometry(QRect(0, 300, 93, 28))
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(200, 300, 192, 28))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.usersTable = QTableWidget(Dialog)
        if (self.usersTable.columnCount() < 3):
            self.usersTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.usersTable.rowCount() < 10):
            self.usersTable.setRowCount(10)
        self.usersTable.setObjectName(u"usersTable")
        self.usersTable.setGeometry(QRect(10, 10, 381, 251))
        self.usersTable.setRowCount(10)
        self.usersTable.setColumnCount(3)
        self.usersTable.horizontalHeader().setDefaultSectionSize(119)
        self.usersTable.verticalHeader().setMinimumSectionSize(15)
        self.usersTable.verticalHeader().setDefaultSectionSize(22)
        self.newUserEdit = QLineEdit(Dialog)
        self.newUserEdit.setObjectName(u"newUserEdit")
        self.newUserEdit.setGeometry(QRect(40, 270, 101, 20))
        self.newPasswordEdit = QLineEdit(Dialog)
        self.newPasswordEdit.setObjectName(u"newPasswordEdit")
        self.newPasswordEdit.setGeometry(QRect(160, 270, 101, 20))
        self.newAccessEdit = QLineEdit(Dialog)
        self.newAccessEdit.setObjectName(u"newAccessEdit")
        self.newAccessEdit.setGeometry(QRect(280, 270, 101, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

        #NOT AUTO GENERATED
        self.loadReloadTable()
        self.connectElements()

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.deleteUserButton.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.addUserButton.setText(QCoreApplication.translate("Dialog", u"Add User", None))
        ___qtablewidgetitem = self.usersTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Username", None));
        ___qtablewidgetitem1 = self.usersTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Password", None));
        ___qtablewidgetitem2 = self.usersTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Access Level", None));
    # retranslateUi



    def make(self): #Create and display this dialog to the user
        self.setupUi(self._thisDialog)
        self._thisDialog.show()

    def connectElements(self): #Connect all UI elements to their appropriate functions
        self.addUserButton.clicked.connect(self.addUser)
        self.deleteUserButton.clicked.connect(self.deleteUser)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.saveChangesAndQuit)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self._thisDialog.reject)

    def loadReloadTable(self): #Load and/or reload the users in the table
        userMatrix = self._userDB.getDbMatrix()
        numUsers = len(userMatrix[0]) #The appropriate number of users to display
        for row in range(0,10): #The maximum number of users is 10
            for column in range(0,3): #There are only 3 pieces of data per user
                textItem = QTableWidgetItem() #This item will be applied to the appropriate cell
                if(row < numUsers): #Iterate through the cells which need to contain users
                    proposedText = str(userMatrix[column][row])
                    if len(proposedText.split(".")) > 1: #If the text is class.value, only write the value
                        proposedText = proposedText.split(".")[1]
                    textItem.setText(proposedText)
                textItem.setFlags(QtCore.Qt.ItemIsEnabled) #This flag stops the cell from being editable by the user
                self.usersTable.setItem(row,column,textItem)
        self.usersTable.setCurrentCell(0,0) #make sure something is always selected. Prevents an exception

    def addUser(self): #Add a new user with the parameters the user has entered
        name = self.newUserEdit.text()
        password = self.newPasswordEdit.text()
        accessText = self.newAccessEdit.text()

        if accessText in AccessType.__members__: #Check if the text exists in the enum to prevent an exception
            access = AccessType[accessText] #Must cast to the enum type
        else:
            return False #Halt the operation if the check fails

        userMatrix = self._userDB.getDbMatrix()
        invalidNames = set({"","Administrator"}).union(userMatrix[0]) #Blacklist blank, Administrator, and all preexisting usernames
        validAccess = {AccessType.USER,AccessType.USER_ADMIN} #Whitelist only access types which can be set. SystemAdmin's cannot be created
        if(self._userDB.getNumUsers() < 10 and name not in invalidNames and password != "" and access in validAccess):
            additionSucceeded = self._userDB.addUser(name,password,access)

            #Reset all the editable text boxes
            self.newUserEdit.setText("")
            self.newPasswordEdit.setText("")
            self.newAccessEdit.setText("")

            self.loadReloadTable() #Reload the table

            return additionSucceeded


    def deleteUser(self): #Delete the currently selected user
        if(self._userDB.getNumUsers() > 1): #Check if there is at least 1 user to delete
            curRow = self.usersTable.currentRow()
            curName = self.usersTable.item(curRow,0).text()
            removalSucceeded = self._userDB.removeUser(curName)
            self.loadReloadTable()
            return removalSucceeded
        else:
            return False

    def saveChangesAndQuit(self): #Save the user database to a file and safely close this dialog
        self._userDB.save()
        self._thisDialog.accept()