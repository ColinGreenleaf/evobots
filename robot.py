import pybullet as p

import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
import numpy as numpy


class ROBOT:
    def __init__(self):
        self.motors = {}
        self.sensors = {}
        self.robotID = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotID)
        self.Prepare_To_Act()
        self.Prepare_To_Sense()
        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)

    def Think(self):
        self.nn.Update()
        self.nn.Print()


    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for i in self.motors:
            self.motors[i].Set_Value(self, t)

