import numpy as numpy
import pyrosim.pyrosim as pyrosim
import constants as c


class SENSOR:
    def __init__(self, linkName):
        self.values = numpy.zeros(c.loopAmt)
        self.linkName = linkName

    def Get_Value(self, t):
        # set the tth value of self.values to the sensor value for the link
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        numpy.save(self.linkName + "_sensorValues", self.values)





