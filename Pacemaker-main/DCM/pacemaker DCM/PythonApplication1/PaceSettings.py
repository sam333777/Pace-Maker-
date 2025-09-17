from ast import Module
from dataclasses import *
from enum import Enum
import pickle
from pathlib import Path
from tempfile import tempdir
from types import NoneType
from TransmitableObject import Transmittable_Object

def dictFix(value,mappings):
    return field(default_factory=lambda:{"value":value,"mappings":mappings})

@dataclass
class Pace_Settings:
    #AOO, AAI, VOO, VVI, AOOR, AAIR, VOOR, VVIR, DDDR
    p_lowRateLimit: dict = dictFix(0.0,[1,1,1,1,1,1,1,1,1])
    p_upRateLimit: dict = dictFix(0.0,[1,1,1,1,1,1,1,1,1])
    p_maxSensorRate: dict = dictFix(0.0,[0,0,0,0,1,1,1,1,1])
    p_fixedAVDelay: dict = dictFix(0.0,[0,0,0,0,0,0,0,0,1])
    p_dynamicAVDelay: dict = dictFix(False,[0,0,0,0,0,0,0,0,1])
    p_sensedAVDelay: dict = dictFix(0.0,[0,0,0,0,0,0,0,0,1])
    p_sensAVdelOffset: dict = dictFix(0.0,[0,0,0,0,0,0,0,0,1])
    p_atrAmplitude: dict = dictFix(0.0,[1,1,0,0,1,1,0,0,1])
    p_ventAmp: dict = dictFix(0.0,[0,0,1,1,0,0,1,1,1])
    p_atrPulseWidth: dict = dictFix(0.0,[1,1,0,0,1,1,0,0,1])
    p_ventPulseWidth: dict = dictFix(0.0,[0,0,1,1,0,0,1,1,1])
    p_atrSensitivity: dict = dictFix(0.0,[0,1,0,0,0,1,0,0,1])
    p_ventSensitivity: dict = dictFix(0.0,[0,0,0,1,0,0,0,1,1])
    p_ventRefractPeriod: dict = dictFix(0.0,[0,0,0,1,0,0,0,1,1])
    p_atrRefractPeriod: dict = dictFix(0.0,[0,1,0,0,0,1,0,0,1])
    p_postVentARP: dict = dictFix(0.0,[0,1,0,0,0,1,0,0,1])
    p_PVARPExtension: dict = dictFix(0.0,[0,0,0,0,0,0,0,0,1])
    p_hysteresis: dict = dictFix(False,[0,1,0,1,0,1,0,1,1])
    p_rateSmooth: dict = dictFix(0.0,[0,1,0,1,0,1,0,1,1])
    p_ATRDuration: dict = dictFix(0.0,[0,0,0,0,0,0,0,0,1])
    p_ATRFallbackMode: dict = dictFix(False,[0,0,0,0,0,0,0,0,1])
    p_ATRFallbackTime: dict = dictFix(0.0,[0,0,0,0,0,0,0,0,1])
    p_ventBlank: dict = dictFix(0.0,[0,0,0,0,0,0,0,0,0])
    p_activeThreshold: dict = dictFix(0.0,[0,0,0,0,1,1,1,1,1])
    p_reactionTime: dict = dictFix(0.0,[0,0,0,0,1,1,1,1,1])
    p_responseFactor: dict = dictFix(0.0,[0,0,0,0,1,1,1,1,1])
    p_recovertTime: dict = dictFix(0.0,[0,0,0,0,1,1,1,1,1])

    def __post_init__(self): #Dataclasses overrite __init__. This serves the same function without conflict
        self._chambersPaced = Enum('O','A','V','D') #Define enums to hold each section of the pace mode
        self._chambersSensed = Enum('O','A','V','D')
        self._senseResponse = Enum('O','T','I','D')
        self._rateModulation = Enum('','R')
        self._paceMode = [self._chambersPaced, self._chambersSensed, self._senseResponse, self._rateModulation] #the pace mode is a list of these enums
        # self._patientName = str()
        # self._fileName = self._patientName + '.pace'

    def changeMode(self, paceEnum, senseEnum, responseEnum, modulEnum): #Change the pacing mode
        self._paceMode[0] = paceEnum
        self._paceMode[1] = senseEnum
        self._paceMode[2] = responseEnum
        self._paceMode[3] = modulEnum

    def getMode(self): #Returns the current pacing mode as a list of enums
        return self._paceMode

    def getModeAsStr(self): #Returns the current pacing mode as a minimal string
        pacedStr = str(self._paceMode[0]).strip("<enum\'>").replace(' \'','') #cast the enum to a string and remove the unecessary characters
        sensedStr = str(self._paceMode[1]).strip("<enum\'>").replace(' \'','')
        responseStr = str(self._paceMode[2]).strip("<enum\'>").replace(' \'','')
        modlStr = str(self._paceMode[3]).strip("<enum\'>").replace(' \'','')
        return pacedStr+sensedStr+responseStr+modlStr #contatenate all the strings together and return the result

    # def setName(self, newName): #Set the patient's name
    #     self._patientName = newName
    #     self._fileName = self._patientName + '.pace'

    # def _openSafe(self, mode): #Open the file if it exists. Used in loading
    #     path = Path("./" + self._fileName)
    #     if(path.is_file()):
    #         if(path.stat().st_size > 0):
    #             return open(self._fileName, mode)
    #     else: return False

    def getAttributes(self): #Returns a dictionary of all the programmable attributes of the class
        tempDict = {}
        for key,value in vars(self).items():
            if not callable(value) and not key.startswith("__") and not key.startswith("_") and key is not NoneType():
                tempDict[key]=value.get("value")
        return tempDict

    def getAttrsAndMaps(self):
        tempDict = {}
        for key,value in vars(self).items():
            if not callable(value) and not key.startswith("__") and not key.startswith("_") and key is not NoneType():
                tempDict[key]=value
        return tempDict

    # def save(self): #Serializes the programmable attributes of this class
    #     paceFile = open(self._fileName, "wb")
    #     pickle.dump(self.getAttributes(), paceFile)
    #     paceFile.close()

    # def load(self): #Deserializes the programmable attributes of this class
    #     paceFile = self._openSafe("rb")
    #     if(paceFile): 
    #         tempDict = pickle.load(paceFile)
    #         for key, value in tempDict.items():
    #             setattr(self,key,value)
    #     paceFile.close()

    def setSetting(self,key,value):
        associatedAttribute = getattr(self,key)
        associatedMappings = associatedAttribute.get("mappings")
        newAttr = {"value":value,"mappings":associatedMappings}
        setattr(self,key,newAttr)

    def setSettingAndMap(self,key,value,mapping):
        newAttr = {"value":value,"mappings":mapping}
        setattr(self,key,newAttr)
        
    def __hash__(self):
        thisHash = hash((vars(self),self._patientName))
        return thisHash

    def __eq__(self, other):
        return isinstance(other, Pace_Settings) and vars(self) == vars(other) and self._patientName == other._patientName


    #Make a subclass of pacesettings which only contains the necessary attributes per mode
    #Find a clean way (a matrix?) of assigning relevant parameters to modes
    #How about a dictionary of dictionaries: dict(parameter:dict(mode:bool))

class Pace_Setting_Interface(Transmittable_Object):
    def __init__(self):
        self._modeMapping = {"AOO":0,"AAI":1,"VOO":2,"VVI":3,"AOOR":4,"AAIR":5,"VOOR":6,"VVIR":7,"DDDR":8}
        self.rollbackSettings = Pace_Settings()
        self.curSettings = Pace_Settings()
        self.wipeCurSettings()
        self.changeMode("A","O","O","")
        

    def wipeCurSettings(self):
        attrDict = self.curSettings.getAttributes()
        for key in attrDict.keys():
            delattr(self.curSettings,key)

    def populateCurSettings(self,mode):
        attrDict = self.rollbackSettings.getAttrsAndMaps()
        mapIndex = self._modeMapping.get(mode)
        for key,value in attrDict.items():
            actualVal = value.get("value")
            mappings = value.get("mappings")
            if mappings[mapIndex]:
                self.curSettings.setSettingAndMap(key,actualVal,mappings)

    def setSetting(self,key,value):
        if hasattr(self.curSettings,key):
            self.curSettings.setSetting(key,value)
            self.rollbackSettings.setSetting(key,value)

    def changeMode(self, paceEnum, senseEnum, responseEnum, modulEnum):
        self.wipeCurSettings()
        self.rollbackSettings.changeMode(paceEnum,senseEnum,responseEnum,modulEnum)
        modeAsStr = self.rollbackSettings.getModeAsStr()
        self.curSettings.changeMode(paceEnum,senseEnum,responseEnum,modulEnum)
        self.populateCurSettings(modeAsStr)
        

    def encodeStrs(self):
        strList = []
        strList.append(self.curSettings.getModeAsStr())
        self.test2.get("value")
        #WIP

    def getModeAsStr(self):
        return self.rollbackSettings.getModeAsStr()

    def getAttributes(self):
        return self.curSettings.getAttributes()

    def getAllAttributes(self):
        return self.rollbackSettings.getAttributes()