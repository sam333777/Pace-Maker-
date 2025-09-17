from types import NoneType
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

from PaceSettings import Pace_Setting_Interface

class Pace_Settings_Template(object):
    def __init__(self, paceSettings):
        self._thisDialog = QtWidgets.QDialog()
        self._settingDisplayList = [] #Declare the list which will hold all settings that need to be displayed
        self.paceSettings = paceSettings
        self.validPaceModes = ["AOO","VOO","VVI","AAI","AOOR","VOOR","AAIR","VVIR","DDDR"] #A whitelist of legal pace modes


    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(748, 653)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(100, 100))
        self.verticalLayoutWidget_2 = QWidget(Dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(70, 30, 402, 333))
        self.outerVerticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.outerVerticalLayout.setObjectName(u"outerVerticalLayout")
        self.outerVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(400, 300))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 398, 298))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollVerticalLayout = QVBoxLayout()
        self.scrollVerticalLayout.setObjectName(u"scrollVerticalLayout")
        self.pacemodeHorizontalLayout = QHBoxLayout()
        self.pacemodeHorizontalLayout.setObjectName(u"pacemodeHorizontalLayout")
        self.pacemodeHorizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.paceModeLabel = QLabel(self.scrollAreaWidgetContents)
        self.paceModeLabel.setObjectName(u"paceModeLabel")

        self.pacemodeHorizontalLayout.addWidget(self.paceModeLabel)

        self.paceModeComboBox = QComboBox(self.scrollAreaWidgetContents)
        self.paceModeComboBox.setObjectName(u"paceModeComboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.paceModeComboBox.sizePolicy().hasHeightForWidth())
        self.paceModeComboBox.setSizePolicy(sizePolicy3)

        self.pacemodeHorizontalLayout.addWidget(self.paceModeComboBox)

        self.curPaceModeLabel = QLabel(self.scrollAreaWidgetContents)
        self.curPaceModeLabel.setObjectName(u"curPaceModeLabel")

        self.pacemodeHorizontalLayout.addWidget(self.curPaceModeLabel)


        self.scrollVerticalLayout.addLayout(self.pacemodeHorizontalLayout)


        self.verticalLayout_3.addLayout(self.scrollVerticalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.outerVerticalLayout.addWidget(self.scrollArea)

        self.buttonsHorizontalLayout = QHBoxLayout()
        self.buttonsHorizontalLayout.setSpacing(6)
        self.buttonsHorizontalLayout.setObjectName(u"buttonsHorizontalLayout")
        self.buttonsHorizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.syncToBoardButton = QPushButton(self.verticalLayoutWidget_2)
        self.syncToBoardButton.setObjectName(u"syncToBoardButton")

        self.buttonsHorizontalLayout.addWidget(self.syncToBoardButton)

        self.refreshButton = QPushButton(self.verticalLayoutWidget_2)
        self.refreshButton.setObjectName(u"refreshButton")

        self.buttonsHorizontalLayout.addWidget(self.refreshButton)

        self.buttonBox = QDialogButtonBox(self.verticalLayoutWidget_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.buttonsHorizontalLayout.addWidget(self.buttonBox)


        self.outerVerticalLayout.addLayout(self.buttonsHorizontalLayout)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

        #NOT AUTO GENERATED
        self.connectElements()
        self.autofillElements()


    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.paceModeLabel.setText(QCoreApplication.translate("Dialog", u"paceMode", None))
        self.paceModeComboBox.setCurrentText("")
        self.curPaceModeLabel.setText(QCoreApplication.translate("Dialog", u"()", None))
        self.syncToBoardButton.setText(QCoreApplication.translate("Dialog", u"Sync to Board", None))
        self.refreshButton.setText(QCoreApplication.translate("Dialog", u"Refresh", None))
    # retranslateU       


    def make(self): #Create and display this dialog to the user
        self.setupUi(self._thisDialog)
        self._thisDialog.show()

    def autofillElements(self): #Display a set of widgets for each programmable attribute in paceSettings
        self.paceModeComboBox.addItems(self.validPaceModes) #paceMode is added manually because it requires a combobox, not a line edit
        self.curPaceModeLabel.setText('('+self.paceSettings.getModeAsStr()+')')
        for key,value in self.paceSettings.getAllAttributes().items():
            newSettingDisplay = singleSettingDisplay(self.verticalLayoutWidget_2,key,value)
            self._settingDisplayList.append(newSettingDisplay) #Add the setting's widgets to a list for future reference
            self.scrollVerticalLayout.addWidget(newSettingDisplay.horizontalLayoutWidget) #Add the widgets to the scroll area display

    def connectElements(self): #Connect all UI elements to their appropriate functions
        self.scrollArea.setWidgetResizable(True)
        self.syncToBoardButton.clicked.connect(self.syncToBoard)
        self.refreshButton.clicked.connect(self.refresh)

    def findSettingDisplay(self,key): #Return the widgets associated with a particular setting
        for settingDisplay in self._settingDisplayList:
            if key == settingDisplay.settingName:
                return settingDisplay

    def hideAll(self):
        for settingDisplay in self._settingDisplayList:
            settingDisplay.hide()

    def refresh(self): #Refresh all of the "current values"
        self.curPaceModeLabel.setText('('+self.paceSettings.getModeAsStr()+')')
        self.hideAll()
        for key,value in self.paceSettings.getAttributes().items():
            associatedDisplay = self.findSettingDisplay(key)
            associatedDisplay.changeCurVal(value)
            associatedDisplay.show()

    def syncToBoard(self): #Sync the current value of each setting to the board
        modeText = self.paceModeComboBox.currentText()
        if len(modeText) < 4: #'' is a valid value for rate modulation, but will not be included in modeText, so it has to be handled specially
            self.paceSettings.changeMode(modeText[0],modeText[1],modeText[2],'') #Change the pace setting for rate modulation = ''
        else:
            self.paceSettings.changeMode(modeText[0],modeText[1],modeText[2],modeText[3]) #Change the pace setting for rate modulation != ''

        for key,value in self.paceSettings.getAttributes().items(): #Iterate through each setting
            associatedDisplay = self.findSettingDisplay(key) #Get the widget associated with the setting
            if associatedDisplay.hidden: continue
            associatedEditValue = associatedDisplay.SettingEdit.text() #Get the text entered by the user for the setting
            castEditValue = 0.0
            try:
                castEditValue = type(value)(associatedEditValue) #Try to cast the editValue to the appropriate type
            except (TypeError, ValueError):
                self.paceSettings.setSetting(key,castEditValue)
            else:
                if type(value) == bool:
                    if associatedEditValue == 'True': #Bools are not cast properly and must be handled manually
                        castEditValue = True
                        self.paceSettings.setSetting(key,castEditValue)
                    elif associatedEditValue == 'False':
                        castEditValue = False
                        self.paceSettings.setSetting(key,castEditValue)
                else:
                    self.paceSettings.setSetting(key,castEditValue)
        self.refresh()
        

class singleSettingDisplay(object): #A helper class which contains the widgets necessary for displaying a single setting
    def __init__(self,parent,key,value):
        self.parentObject = parent #The parent which PyQt will bind this object to
        self.settingName = key
        self.settingValue = value
        self.setupUI()
        self.retranslateUi()
        self.hidden = False

    def setupUI(self):
        self.horizontalLayoutWidget = QWidget(self.parentObject)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 351, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.settingNameLabel = QLabel(self.horizontalLayoutWidget)
        self.settingNameLabel.setObjectName(u"settingNameLabel")

        self.horizontalLayout.addWidget(self.settingNameLabel)

        self.SettingEdit = QLineEdit(self.horizontalLayoutWidget)
        self.SettingEdit.setObjectName(u"SettingEdit")

        self.horizontalLayout.addWidget(self.SettingEdit)

        self.settingCurValLabel = QLabel(self.horizontalLayoutWidget)
        self.settingCurValLabel.setObjectName(u"settingCurValLabel")

        self.horizontalLayout.addWidget(self.settingCurValLabel)

    def retranslateUi(self):
        strippedSettingName = self.settingName.split('_')[1]
        valueInBrackets = "(" + str(self.settingValue) + ")"
        self.settingNameLabel.setText(QCoreApplication.translate("Dialog", strippedSettingName, None))
        self.settingCurValLabel.setText(QCoreApplication.translate("Dialog", valueInBrackets, None))

    def changeCurVal(self,newVal): #Change the "current value" display
        newValueInBrackets = "(" + str(newVal) + ")" #Brackets are added around the value for prettiness
        self.settingCurValLabel.setText(QCoreApplication.translate("Dialog", newValueInBrackets, None)) #Set the relevant text

    def hide(self):
        self.settingCurValLabel.hide()
        self.SettingEdit.hide()
        self.settingCurValLabel.hide()
        self.hidden = True


    def show(self):
        self.settingCurValLabel.show()
        self.SettingEdit.show()
        self.settingCurValLabel.show()
        self.hidden = False