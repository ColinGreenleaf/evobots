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
        short = 0.2
        long = 1
        uplen = 0.8
        lowlen = 0.8
        upoff = uplen / 2
        lowoff = lowlen / 2
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[c.cubeLength*2, c.cubeWidth, c.cubeHeight*0.5])
        # ----------------- Right Side ----------------- #
        # Right Front Leg
        pyrosim.Send_Joint(name="Torso_RightFrontLeg", parent="Torso", child="RightFrontLeg", type="revolute",
                           position=[-1, 0.5, 1], jointAxis="1 0 1")
        pyrosim.Send_Cube(name="RightFrontLeg", pos=[0, upoff, 0], size=[0.2, uplen, 0.2])
        pyrosim.Send_Joint(name="RightFrontLeg_LowerRightFrontLeg", parent="RightFrontLeg", child="LowerRightFrontLeg",
                            type="revolute", position=[0, uplen, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerRightFrontLeg", pos=[0, 0, -lowoff], size=[0.2, 0.2, lowlen])

        # Right Mid Leg
        pyrosim.Send_Joint(name="Torso_RightMidLeg", parent="Torso", child="RightMidLeg", type="revolute",
                           position=[0, 0.5, 1], jointAxis="1 0 1")
        pyrosim.Send_Cube(name="RightMidLeg", pos=[0, upoff, 0], size=[0.2, uplen, 0.2])
        pyrosim.Send_Joint(name="RightMidLeg_LowerRightMidLeg", parent="RightMidLeg", child="LowerRightMidLeg",
                            type="revolute", position=[0, uplen, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerRightMidLeg", pos=[0, 0, -lowoff], size=[0.2, 0.2, lowlen])

        # Right Back Leg
        pyrosim.Send_Joint(name="Torso_RightBackLeg", parent="Torso", child="RightBackLeg", type="revolute",
                           position=[1, 0.5, 1], jointAxis="1 0 1")
        pyrosim.Send_Cube(name="RightBackLeg", pos=[0, upoff, 0], size=[0.2, uplen, 0.2])
        pyrosim.Send_Joint(name="RightBackLeg_LowerRightBackLeg", parent="RightBackLeg", child="LowerRightBackLeg",
                            type="revolute", position=[0, uplen, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerRightBackLeg", pos=[0, 0, -lowoff], size=[0.2, 0.2, lowlen])

        # ----------------- Left Side ----------------- #
        # Left Front Leg
        pyrosim.Send_Joint(name="Torso_LeftFrontLeg", parent="Torso", child="LeftFrontLeg", type="revolute",
                           position=[-1, -0.5, 1], jointAxis="1 0 1")
        pyrosim.Send_Cube(name="LeftFrontLeg", pos=[0, -upoff, 0], size=[0.2, uplen, 0.2])
        pyrosim.Send_Joint(name="LeftFrontLeg_LowerLeftFrontLeg", parent="LeftFrontLeg", child="LowerLeftFrontLeg",
                            type="revolute", position=[0, -uplen, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerLeftFrontLeg", pos=[0, 0, -lowoff], size=[0.2, 0.2, lowlen])

        # Left Mid Leg
        pyrosim.Send_Joint(name="Torso_LeftMidLeg", parent="Torso", child="LeftMidLeg", type="revolute",
                           position=[0, -0.5, 1], jointAxis="1 0 1")
        pyrosim.Send_Cube(name="LeftMidLeg", pos=[0, -upoff, 0], size=[0.2, uplen, 0.2])
        pyrosim.Send_Joint(name="LeftMidLeg_LowerLeftMidLeg", parent="LeftMidLeg", child="LowerLeftMidLeg",
                            type="revolute", position=[0, -uplen, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerLeftMidLeg", pos=[0, 0, -lowoff], size=[0.2, 0.2, lowlen])

        # Left Back Leg
        pyrosim.Send_Joint(name="Torso_LeftBackLeg", parent="Torso", child="LeftBackLeg", type="revolute",
                            position=[1, -0.5, 1], jointAxis="1 0 1")
        pyrosim.Send_Cube(name="LeftBackLeg", pos=[0, -upoff, 0], size=[0.2, uplen, 0.2])
        pyrosim.Send_Joint(name="LeftBackLeg_LowerLeftBackLeg", parent="LeftBackLeg", child="LowerLeftBackLeg",
                            type="revolute", position=[0, -uplen, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerLeftBackLeg", pos=[0, 0, -lowoff], size=[0.2, 0.2, lowlen])

        pyrosim.End()

    def Create_Brain(self):
        linkNames = ["Torso", "RightFrontLeg", "RightMidLeg", "RightBackLeg", "LeftFrontLeg", "LeftMidLeg", "LeftBackLeg", "LowerRightFrontLeg", "LowerRightMidLeg", "LowerRightBackLeg", "LowerLeftFrontLeg", "LowerLeftMidLeg", "LowerLeftBackLeg"]
        jointnames = ["Torso_RightFrontLeg", "Torso_RightMidLeg", "Torso_RightBackLeg", "Torso_LeftFrontLeg", "Torso_LeftMidLeg", "Torso_LeftBackLeg", "RightFrontLeg_LowerRightFrontLeg", "RightMidLeg_LowerRightMidLeg", "RightBackLeg_LowerRightBackLeg", "LeftFrontLeg_LowerLeftFrontLeg", "LeftMidLeg_LowerLeftMidLeg", "LeftBackLeg_LowerLeftBackLeg"]

        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        nameval = 0
        for name in linkNames:
            pyrosim.Send_Sensor_Neuron(name=nameval, linkName=name)
            nameval += 1

        for i in range(0, c.hiddenNeurons):
            pyrosim.Send_Hidden_Neuron(name=nameval)
            nameval += 1

        for name in jointnames:
            pyrosim.Send_Motor_Neuron(name=nameval, jointName=name)
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



