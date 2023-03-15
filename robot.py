import os

import pybullet as p

import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
import numpy as numpy


class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.motors = {}
        self.sensors = {}
        self.robotID = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotID)
        self.Prepare_To_Act()
        self.Prepare_To_Sense()
        self.nn = NEURAL_NETWORK("brain"+solutionID+".nndf")
        # os.system("rm brain"+solutionID+".nndf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)

    def Think(self):
        self.nn.Update()
        # self.nn.Print()


    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName.encode("utf-8")].Set_Value(self, desiredAngle)

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotID, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        print(xCoordinateOfLinkZero)
        #write xCoordinateOfLinkZero to a file called fitness.txt
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        os.system("mv tmp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")
        exit()

