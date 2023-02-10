import numpy as numpy
from math import pi
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = numpy.zeros(c.loopAmt)
        self.Prepare_To_Act()


    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.phaseOffset = c.phaseOffset
        x = numpy.linspace(-pi, pi, c.loopAmt)
        self.motorValues = self.amplitude * numpy.sin(self.frequency * x + self.phaseOffset)

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot.robotID,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=c.motorForce)

    def Save_Values(self):
        numpy.save(self.jointName + "_motorValues", self.motorValues)

