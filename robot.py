import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import constants as c
import numpy as numpy


class ROBOT:
    def __init__(self):
        self.motors = {}

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)

