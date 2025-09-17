import sys
from tkinter import dialog
import MainWindow, LoginDialog
from LoginDialog import Login_Template
from PyQt5 import QtCore, QtGui, QtWidgets, QtWidgets
import sys

def main():
    #Create the all-important but rarely relevant 'app' object
    app = QtWidgets.QApplication(sys.argv)
    

    
    loginUI = Login_Template()
    loginUI.make() #Make the login UI
    
    
    sys.exit(app.exec_()) #Safely terminate the program when finished
 


if __name__ == "__main__":
    main() #Make main() run automatically
