import io
import serial
from TransmitableObject import Transmittable_Object

class serialInterface:
    def __init__(self):
        self.serialObj = serial.Serial('COM1')
        
        self.serialObj.baudrate(9600)
        self.serialObj.bytesize(8)

    def transmit(self,obj):
        if not issubclass(type(obj),Transmittable_Object):
            raise Exception("Object is not transmitable")
        self.serialObj.open()
        for string in obj.encodeStrs():
            self.serialObj.write(string)
        self.serialObj.close()

    def __del__(self):
        self.SerialObj.close()