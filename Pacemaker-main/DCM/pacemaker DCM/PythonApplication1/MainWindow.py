from os import access
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QPropertyAnimation)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from PyQt5 import QtWidgets
import sys
from PaceSettings import Pace_Setting_Interface
from PaceSettingsDialog import Pace_Settings_Template
from User import User, AccessType
from UserManagerDialog import User_Manager_Template

import pandas as pd
import pyqtgraph as pg

class Ui_MainWindow(object):
    def __init__(self):
        self._mainWindow = QMainWindow()
        self._curPaceProfile = Pace_Setting_Interface()
        self._curUser = User("", "", "")
        self.plotWidget1 = None
        self.plotWidget2 = None
        self.statusMenuVisible = False 
        self.connected = False  

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionManage_Users = QAction(MainWindow)
        self.actionManage_Users.setObjectName(u"actionManage_Users")
        self.actionPacemaker_Settings = QAction(MainWindow)
        self.actionPacemaker_Settings.setObjectName(u"actionPacemaker_Settings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.statusIndicator = QLabel(self.centralwidget)
        self.statusIndicator.setObjectName(u"statusIndicator")
        self.statusIndicator.setGeometry(QRect(680, 10, 10, 10))
        self.toggleStatusButton = QPushButton(self.centralwidget)
        self.toggleStatusButton.setObjectName(u"toggleStatusButton")
        self.toggleStatusButton.setGeometry(QRect(700, 10, 80, 30))
        self.statusGroupBox = QGroupBox(self.centralwidget)
        self.statusGroupBox.setObjectName(u"statusGroupBox")
        self.statusGroupBox.setGeometry(QRect(600, 50, 200, 491))
        self.connectionStatusLabel = QLabel(self.statusGroupBox)
        self.connectionStatusLabel.setObjectName(u"connectionStatusLabel")
        self.connectionStatusLabel.setGeometry(QRect(10, 20, 180, 16))
        self.loadStatusLabel = QLabel(self.statusGroupBox)
        self.loadStatusLabel.setObjectName(u"loadStatusLabel")
        self.loadStatusLabel.setGeometry(QRect(10, 50, 180, 16))
        self.loadProgressBar = QProgressBar(self.statusGroupBox)
        self.loadProgressBar.setObjectName(u"loadProgressBar")
        self.loadProgressBar.setGeometry(QRect(10, 80, 180, 23))
        self.loadProgressBar.setValue(24)
        self.optionsBox = QGroupBox(self.centralwidget)
        self.optionsBox.setObjectName(u"optionsBox")
        self.optionsBox.setGeometry(QRect(10, 50, 131, 491))
        self.paceNowButton = QPushButton(self.optionsBox)
        self.paceNowButton.setObjectName(u"paceNowButton")
        self.paceNowButton.setGeometry(QRect(10, 20, 101, 61))
        self.quitButton = QPushButton(self.optionsBox)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setGeometry(QRect(10, 450, 101, 31))
        self.setClockButton = QPushButton(self.optionsBox)
        self.setClockButton.setObjectName(u"setClockButton")
        self.setClockButton.setGeometry(QRect(10, 410, 101, 26))
        self.newPatientButton = QPushButton(self.optionsBox)
        self.newPatientButton.setObjectName(u"newPatientButton")
        self.newPatientButton.setGeometry(QRect(10, 340, 101, 31))
        self.electroGramBox = QGroupBox(self.centralwidget)
        self.electroGramBox.setObjectName(u"electroGramBox")
        self.electroGramBox.setGeometry(QRect(160, 50, 440, 491))
        self.ventricularBox = QGroupBox(self.electroGramBox)
        self.ventricularBox.setObjectName(u"ventricularBox")
        self.ventricularBox.setGeometry(QRect(10, 20, 410, 171))
        self.venPlotWidget = pg.PlotWidget(self.ventricularBox) #Changed QWidget to pg.PlotWidget
        self.venPlotWidget.setObjectName(u"venPlotWidget")
        self.venPlotWidget.setGeometry(QRect(10, 30, 390, 130))
        self.atrialBox = QGroupBox(self.electroGramBox)
        self.atrialBox.setObjectName(u"atrialBox")
        self.atrialBox.setGeometry(QRect(10, 200, 410, 161))
        self.atrPlotWidget = pg.PlotWidget(self.atrialBox) #Changed QWidget to pg.PlotWidget
        self.atrPlotWidget.setObjectName(u"atrPlotWidget")
        self.atrPlotWidget.setGeometry(QRect(10, 30, 390, 120))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSetup = QMenu(self.menubar)
        self.menuSetup.setObjectName(u"menuSetup")
        self.menuAdmin_tools = QMenu(self.menuSetup)
        self.menuAdmin_tools.setObjectName(u"menuAdmin_tools")
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuPacemaker = QMenu(self.menubar)
        self.menuPacemaker.setObjectName(u"menuPacemaker")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetup.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuPacemaker.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuSetup.addAction(self.menuAdmin_tools.menuAction())
        self.menuAdmin_tools.addAction(self.actionManage_Users)
        self.menuPacemaker.addAction(self.actionPacemaker_Settings)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        #Not auto-generated
        self._connectElements()
        self.loadAndPlotExcel()
        self.animation = QPropertyAnimation(self.statusGroupBox, b"geometry")
        self.animation.setDuration(300)
        self.animation.setStartValue(QRect(600, 50, 200, 491))
        self.animation.setEndValue(QRect(800, 50, 200, 491))
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionManage_Users.setText(QCoreApplication.translate("MainWindow", u"Manage Users", None))
        self.actionPacemaker_Settings.setText(QCoreApplication.translate("MainWindow", u"Pacemaker Settings", None))
        self.toggleStatusButton.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Status", None))
        self.connectionStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Pacemaker Connection: Disconnected", None))
        self.loadStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Loading Status", None))
        self.optionsBox.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.paceNowButton.setText(QCoreApplication.translate("MainWindow", u"Pace", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.setClockButton.setText(QCoreApplication.translate("MainWindow", u"Set Clock", None))
        self.newPatientButton.setText(QCoreApplication.translate("MainWindow", u"New Patient", None))
        self.electroGramBox.setTitle(QCoreApplication.translate("MainWindow", u"ElectroGram", None))
        self.ventricularBox.setTitle(QCoreApplication.translate("MainWindow", u"Ventricular", None))
        self.atrialBox.setTitle(QCoreApplication.translate("MainWindow", u"Atrial", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSetup.setTitle(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.menuAdmin_tools.setTitle(QCoreApplication.translate("MainWindow", u"Admin tools", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuPacemaker.setTitle(QCoreApplication.translate("MainWindow", u"Pacemaker", None))
    # retranslateUi


    def make(self, user): #Create and display this dialog to the user, for the appropriate User object
        self.setupUi(self._mainWindow)
        self._mainWindow.show()

        self._curUser = user
        if user.access in [AccessType.USER_ADMIN, AccessType.SYSTEM_ADMIN]: #Allow use of admin tools if the user is an admin account
            self.menuAdmin_tools.setEnabled(True)
        else:
            self.menuAdmin_tools.setEnabled(False)

    def _connectElements(self): #Connect all UI elements to their appropriate functions
        self.actionManage_Users.triggered.connect(self._openUserManager)
        self.actionPacemaker_Settings.triggered.connect(self._openPacemakerSettings)
        self.quitButton.clicked.connect(QCoreApplication.instance().quit)

    def toggleStatusMenu(self): #Collapse/expand the communication status menu
        if self.statusMenuVisible:
            self.animation.setDirection(QPropertyAnimation.Backward)
        else:
            self.animation.setDirection(QPropertyAnimation.Forward)
        self.animation.start() #Play the toggling animation
        self.statusMenuVisible = not self.statusMenuVisible

    def updateStatusIndicator(self): #Update indicator given the status of the board
        #Placeholder
        color = "green" if self.connected else "red"
        self.statusIndicator.setStyleSheet(f"background-color: {color}; border-radius: 5px;")

    def _openUserManager(self): #Open the user manager dialog
        self._usManager = User_Manager_Template()
        self._usManager.make()

    def _openPacemakerSettings(self): #Open the pacemaker settings dialog
        self._paceController = Pace_Settings_Template(self._curPaceProfile)
        self._paceController.make()

    def loadAndPlotExcel(self): #Load the egram data and plot it
        file_name = 'data.xlsx'
        data = pd.read_excel(file_name)

        x = data['x']
        y1 = data['y']
        y2 = data['y']

        self.venPlotWidget.clear()
        self.venPlotWidget.plot(x, y1, pen='r', name='Ventricular Plot')
        self.atrPlotWidget.clear()
        self.atrPlotWidget.plot(x, y2, pen='b', name='Atrial Plot')


