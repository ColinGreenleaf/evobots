import time
import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import os

class SOLUTION:

    def __init__(self, id):
        self.myID = id
        # make a numpy 3 row x 2 column matrix
        self.weights = np.random.rand(3,2)
        self.weights = (self.weights * 2) - 1

    def Evaluate(self, directOrGUI):
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        # read in the fitness from the fitness.txt file
        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        print("fitness = ", self.fitness)
        f.close()

    def Start_Simulation(self, directOrGUI):
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        # read in the fitness from the fitness.txt file
        f = open(fitnessFileName, "r")
        tempfitness = f.read()
        if tempfitness == '':
            tempfitness = 1
        self.fitness = float(tempfitness)
        # print("fitness = ", self.fitness)
        f.close()
        if os.path.exists(fitnessFileName):
            os.system("rm fitness"+str(self.myID)+".txt")


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="box", pos=[-5, +5, 0.5], size=[c.cubeLength, c.cubeWidth, c.cubeHeight])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[c.cubeLength, c.cubeWidth, c.cubeHeight])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, c.cubeWidth, 0.2])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, c.cubeWidth, 0.2])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        # for loop that iterates through 0, 1, 2
        for currentRow in range(c.sensorNeurons):
            # for loop that iterates through 3, 4
            for currentColumn in range(c.motorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.sensorNeurons, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        # choose a random row from 0 to 2 (inclusive) and a random column from 0 to 1 (inclusive)
        randomRow = np.random.randint(0,3)
        randomColumn = np.random.randint(0,2)
        self.weights[randomRow][randomColumn] = np.random.random() * 2 - 1

    def Set_ID(self, id):
        self.myID = id
