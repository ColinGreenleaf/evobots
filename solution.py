import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c

class SOLUTION:

    def __init__(self):
        # make a numpy 3 row x 2 column matrix
        self.weights = np.random.rand(3,2)
        self.weights = (self.weights * 2) - 1

    def Evaluate(self):
        pass

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="box", pos=[-5, +5, 0.5], size=[c.cubeLength, c.cubeWidth, c.cubeHeight])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[c.cubeLength, c.cubeWidth, c.cubeHeight])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0.5, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[c.cubeLength, c.cubeWidth, c.cubeHeight])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[-0.5, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[c.cubeLength, c.cubeWidth, c.cubeHeight])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        # for loop that iterates through 0, 1, 2
        for i in range(3):
            # for loop that iterates through 3, 4
            for j in range(3, 5):
                pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j, weight=np.random.uniform(-1, 1))

        pyrosim.End()