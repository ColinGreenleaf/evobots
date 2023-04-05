import shutil
import time
import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import os

class SOLUTION:

    def __init__(self, id):
        self.myID = id
        self.weights = np.random.rand(c.sensorNeurons, c.motorNeurons)
        #make matrices of random weights for the neural network
        self.sensorToHiddenWeights = np.random.rand(c.sensorNeurons, c.hiddenNeurons)
        self.hiddenToMotorWeights = np.random.rand(c.hiddenNeurons, c.motorNeurons)
        self.sensorToHiddenWeights = (self.weights * 2) - 1
        self.hiddenToMotorWeights = (self.weights * 2) - 1

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
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                            position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="FrontLeg_LowerFrontLeg", parent="FrontLeg", child="LowerFrontLeg", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="BackLeg_LowerBackLeg", parent="BackLeg", child="LowerBackLeg", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="LeftLeg_LowerLeftLeg", parent="LeftLeg", child="LowerLeftLeg", type="revolute",
                            position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="RightLeg_LowerRightLeg", parent="RightLeg", child="LowerRightLeg", type="revolute",
                            position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])





        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        nameval = 0
        pyrosim.Send_Sensor_Neuron(name=nameval, linkName="Torso")
        nameval += 1
        pyrosim.Send_Sensor_Neuron(name=nameval, linkName="BackLeg")
        nameval += 1
        pyrosim.Send_Sensor_Neuron(name=nameval, linkName="FrontLeg")
        nameval += 1
        pyrosim.Send_Sensor_Neuron(name=nameval, linkName="LeftLeg")
        nameval += 1
        pyrosim.Send_Sensor_Neuron(name=nameval, linkName="RightLeg")
        nameval += 1
        pyrosim.Send_Sensor_Neuron(name=nameval, linkName="LowerFrontLeg")
        nameval += 1
        pyrosim.Send_Sensor_Neuron(name=nameval, linkName="LowerBackLeg")
        nameval += 1
        pyrosim.Send_Sensor_Neuron(name=nameval, linkName="LowerLeftLeg")
        nameval += 1
        pyrosim.Send_Sensor_Neuron(name=nameval, linkName="LowerRightLeg")
        nameval += 1

        for i in range(0, c.hiddenNeurons):
            pyrosim.Send_Hidden_Neuron(name=nameval)
            nameval += 1

        pyrosim.Send_Motor_Neuron(name=nameval, jointName="Torso_BackLeg")
        nameval += 1
        pyrosim.Send_Motor_Neuron(name=nameval, jointName="Torso_FrontLeg")
        nameval += 1
        pyrosim.Send_Motor_Neuron(name=nameval, jointName="Torso_LeftLeg")
        nameval += 1
        pyrosim.Send_Motor_Neuron(name=nameval, jointName="Torso_RightLeg")
        nameval += 1
        pyrosim.Send_Motor_Neuron(name=nameval, jointName="FrontLeg_LowerFrontLeg")
        nameval += 1
        pyrosim.Send_Motor_Neuron(name=nameval, jointName="BackLeg_LowerBackLeg")
        nameval += 1
        pyrosim.Send_Motor_Neuron(name=nameval, jointName="LeftLeg_LowerLeftLeg")
        nameval += 1
        pyrosim.Send_Motor_Neuron(name=nameval, jointName="RightLeg_LowerRightLeg")
        nameval += 1


        # for loop that iterates through sensor neurons
        for currentRow in range(c.sensorNeurons):
            # for loop that iterates through hidden neurons
            for currentColumn in range(c.hiddenNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.sensorNeurons, weight=self.sensorToHiddenWeights[currentRow][currentColumn])

        # for loop that iterates through hidden neurons
        for currentRow in range(c.hiddenNeurons):
            # for loop that iterates through motor neurons
            for currentColumn in range(c.motorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow+c.sensorNeurons, targetNeuronName=currentColumn+c.hiddenNeurons+c.sensorNeurons, weight=self.hiddenToMotorWeights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        # choose a random row from 0 to 2 (inclusive) and a random column from 0 to 1 (inclusive)
        randomRow = np.random.randint(0, c.sensorNeurons)
        randomColumn = np.random.randint(0, c.hiddenNeurons)
        self.sensorToHiddenWeights[randomRow][randomColumn] = np.random.random() * 2 - 1

        randomRow = np.random.randint(0, c.hiddenNeurons)
        randomColumn = np.random.randint(0, c.motorNeurons)
        self.hiddenToMotorWeights[randomRow][randomColumn] = np.random.random() * 2 - 1

    def Set_ID(self, id):
        self.myID = id



