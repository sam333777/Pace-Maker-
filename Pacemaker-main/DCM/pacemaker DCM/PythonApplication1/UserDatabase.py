from os import access
import pickle
from User import User, AccessType
from pathlib import Path

fileName = "users.txt"

class User_Database():
    def __init__(self):
        self._db = set() #Initialize the set which will hold all the users
        self._db.add(self._getSysAdmin()) #Manually add the system admin account
        self._numUsers = len(self._db)

    def _getSysAdmin(self): #Returns a User representing the system admin
        admin = User("Administrator", "Admin5678", AccessType.SYSTEM_ADMIN) #Admin account is hardcoded for security
        return admin

    def _openSafe(self, mode): #Returns an open file if it exists, false otherwise
        path = Path(fileName)
        if(path.is_file()):
            if(path.stat().st_size > 0):
                return open(fileName, mode)
        else: return False

    def save(self): #Serializes _db
        dbfile = open(fileName, "wb")
        adminSet = set()
        adminSet.add(self._getSysAdmin()) #make a temporary set which only contains the system admin
        safeDb = self._db - adminSet - {self._getSysAdmin()} #Make a temporary "safe" set which contains everything except the system admin
        pickle.dump(safeDb,dbfile) #Serialize only the safe set
        dbfile.close()

    def load(self): #Deserializes _db
        dbfile = self._openSafe("rb")
        if(dbfile): 
            self._db = pickle.load(dbfile)
            self._db.add(self._getSysAdmin()) #The system admin must be manually re-added
            dbfile.close()
        self._numUsers = len(self._db)

    def addUser(self, name, password, access): #Create and adds a new user to the database
        if(access == AccessType.SYSTEM_ADMIN): #Only one admin account can exist
            return False
        if(self._numUsers == 10): #There cannot be more than 10 users
            return False
        for user in self._db: #No two usernames can match
            if(name == user.name):
                return False

        newUser = User(name, password, access)
        self._db.add(newUser)
        self._numUsers += 1
        return True

    def removeUser(self, name): #Removes a user from the database by name
        targetUser = User("","","") #Users must be initialized, so this temporary one has blank attributes
        for user in self._db:
            if user.name == name:
                targetUser = user
                break
        self._db.remove(targetUser) #Set.remove(item) cannot be used until any/all iterators are destroyed
        self._numUsers -= 1

    def getNumUsers(self): #Returns the current number of users, including the system admin
        return self._numUsers

    def getDbMatrix(self): #Returns a list of all [name][censored password][access level], excluding the system admin
        nameList = []
        passwordList = []
        accessList = []
        userMatrix = []
        for user in self._db:
            if(user.access != AccessType.SYSTEM_ADMIN):
                nameList.append(user.name)
                passwordList.append("*"*len(user.password)) #Passwords are censored as a series of '*' characters
                accessList.append(user.access)
        userMatrix.append(nameList)
        userMatrix.append(passwordList)
        userMatrix.append(accessList)
        return userMatrix