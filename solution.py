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
        return self.fitness


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="box", pos=[-5, +5, 0.5], size=[c.cubeLength, c.cubeWidth, c.cubeHeight])
        pyrosim.End()

    def Create_Body(self):
        uplen = 0.8 # upper leg length
        lowlen = 0.7 # lower leg length
        upoff = uplen / 2
        lowoff = lowlen / 2
        sidedist = 0.6 # distance between side legs (kinda)
        enddist = 0.35 # distance between end legs (kinda)
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[c.cubeLength*2, c.cubeWidth, c.cubeHeight*0.5])

        # ----------------- Right Side ----------------- #
        # Right Front Leg
        pyrosim.Send_Joint(name="Torso_RightFrontLeg", parent="Torso", child="RightFrontLeg", type="revolute",
                           position=[-sidedist, 0.5, 1], jointAxis="1 0 1")
        pyrosim.Send_Cube(name="RightFrontLeg", pos=[0, upoff, 0], size=[0.2, uplen, 0.2])
        pyrosim.Send_Joint(name="RightFrontLeg_LowerRightFrontLeg", parent="RightFrontLeg", child="LowerRightFrontLeg",
                            type="revolute", position=[0, uplen, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerRightFrontLeg", pos=[0, 0, -lowoff], size=[0.2, 0.2, lowlen])

        # Right Back Leg
        pyrosim.Send_Joint(name="Torso_RightBackLeg", parent="Torso", child="RightBackLeg", type="revolute",
                           position=[sidedist, 0.5, 1], jointAxis="1 0 1")
        pyrosim.Send_Cube(name="RightBackLeg", pos=[0, upoff, 0], size=[0.2, uplen, 0.2])
        pyrosim.Send_Joint(name="RightBackLeg_LowerRightBackLeg", parent="RightBackLeg", child="LowerRightBackLeg",
                            type="revolute", position=[0, uplen, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerRightBackLeg", pos=[0, 0, -lowoff], size=[0.2, 0.2, lowlen])

        # ----------------- Left Side ----------------- #
        # Left Front Leg
        pyrosim.Send_Joint(name="Torso_LeftFrontLeg", parent="Torso", child="LeftFrontLeg", type="revolute",
                           position=[-sidedist, -0.5, 1], jointAxis="1 0 1")
        pyrosim.Send_Cube(name="LeftFrontLeg", pos=[0, -upoff, 0], size=[0.2, uplen, 0.2])
        pyrosim.Send_Joint(name="LeftFrontLeg_LowerLeftFrontLeg", parent="LeftFrontLeg", child="LowerLeftFrontLeg",
                            type="revolute", position=[0, -uplen, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerLeftFrontLeg", pos=[0, 0, -lowoff], size=[0.2, 0.2, lowlen])

        # Left Back Leg
        pyrosim.Send_Joint(name="Torso_LeftBackLeg", parent="Torso", child="LeftBackLeg", type="revolute",
                            position=[sidedist, -0.5, 1], jointAxis="1 0 1")
        pyrosim.Send_Cube(name="LeftBackLeg", pos=[0, -upoff, 0], size=[0.2, uplen, 0.2])
        pyrosim.Send_Joint(name="LeftBackLeg_LowerLeftBackLeg", parent="LeftBackLeg", child="LowerLeftBackLeg",
                            type="revolute", position=[0, -uplen, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerLeftBackLeg", pos=[0, 0, -lowoff], size=[0.2, 0.2, lowlen])

       # ----------------- Head (Front) Legs ----------------- #
        # Head Left Leg
        pyrosim.Send_Joint(name="Torso_HeadLeftLeg", parent="Torso", child="HeadLeftLeg", type="revolute",
                            position=[-1, -enddist, 1], jointAxis="0 1 1")
        pyrosim.Send_Cube(name="HeadLeftLeg", pos=[-upoff, 0, 0], size=[uplen, 0.2, 0.2])
        pyrosim.Send_Joint(name="HeadLeftLeg_LowerHeadLeftLeg", parent="HeadLeftLeg", child="LowerHeadLeftLeg",
                            type="revolute", position=[-uplen, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerHeadLeftLeg", pos=[0, 0, -lowoff], size=[0.2, 0.2, lowlen])

        pyrosim.Send_Joint(name="Torso_HeadRightLeg", parent="Torso", child="HeadRightLeg", type="revolute",
                           position=[-1, enddist, 1], jointAxis="0 1 1")
        pyrosim.Send_Cube(name="HeadRightLeg", pos=[-upoff, 0, 0], size=[uplen, 0.2, 0.2])
        pyrosim.Send_Joint(name="HeadRightLeg_LowerHeadRightLeg", parent="HeadRightLeg", child="LowerHeadRightLeg",
                           type="revolute", position=[-uplen, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerHeadRightLeg", pos=[0, 0, -lowoff], size=[0.2, 0.2, lowlen])


        # ----------------- Tail (Back) Legs ----------------- #
        # Tail Left Leg
        pyrosim.Send_Joint(name="Torso_TailLeftLeg", parent="Torso", child="TailLeftLeg", type="revolute",
                           position=[1, -enddist, 1], jointAxis="0 1 1")
        pyrosim.Send_Cube(name="TailLeftLeg", pos=[upoff, 0, 0], size=[uplen, 0.2, 0.2])
        pyrosim.Send_Joint(name="TailLeftLeg_LowerTailLeftLeg", parent="TailLeftLeg", child="LowerTailLeftLeg",
                           type="revolute", position=[uplen, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerTailLeftLeg", pos=[0, 0, -lowoff], size=[0.2, 0.2, lowlen])

        # Tail Right Leg
        pyrosim.Send_Joint(name="Torso_TailRightLeg", parent="Torso", child="TailRightLeg", type="revolute",
                           position=[1, enddist, 1], jointAxis="0 1 1")
        pyrosim.Send_Cube(name="TailRightLeg", pos=[upoff, 0, 0], size=[uplen, 0.2, 0.2])
        pyrosim.Send_Joint(name="TailRightLeg_LowerTailRightLeg", parent="TailRightLeg", child="LowerTailRightLeg",
                           type="revolute", position=[uplen, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerTailRightLeg", pos=[0, 0, -lowoff], size=[0.2, 0.2, lowlen])

        pyrosim.End()

    def Create_Brain(self):

        linkNames = ["Torso", "RightFrontLeg", "RightBackLeg", "LeftFrontLeg", "LeftBackLeg", "LowerRightFrontLeg", "LowerRightBackLeg", "LowerLeftFrontLeg",
                     "LowerLeftBackLeg", "HeadLeftLeg", "LowerHeadLeftLeg", "HeadRightLeg", "LowerHeadRightLeg", "TailLeftLeg", "LowerTailLeftLeg", "TailRightLeg", "LowerTailRightLeg"]
        jointnames = ["Torso_RightFrontLeg", "Torso_RightBackLeg", "Torso_LeftFrontLeg", "Torso_LeftBackLeg", "RightFrontLeg_LowerRightFrontLeg",
                      "RightBackLeg_LowerRightBackLeg", "LeftFrontLeg_LowerLeftFrontLeg", "LeftBackLeg_LowerLeftBackLeg", "Torso_HeadLeftLeg", "HeadLeftLeg_LowerHeadLeftLeg",
                      "Torso_HeadRightLeg", "HeadRightLeg_LowerHeadRightLeg", "Torso_TailLeftLeg", "TailLeftLeg_LowerTailLeftLeg", "Torso_TailRightLeg", "TailRightLeg_LowerTailRightLeg"]

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
        # mutate 3 synapses
        for i in range(0, 3):
            # choose a random synapse in the sensor to hidden layer
            randomRow = np.random.randint(0, c.sensorNeurons)
            randomColumn = np.random.randint(0, c.hiddenNeurons)
            # randomize the weight of the synapse
            self.sensorToHiddenWeights[randomRow][randomColumn] = np.random.random() * 2 - 1

            # choose a random synapse in the hidden to motor layer
            randomRow = np.random.randint(0, c.hiddenNeurons)
            randomColumn = np.random.randint(0, c.motorNeurons)
            # randomize the weight of the synapse
            self.hiddenToMotorWeights[randomRow][randomColumn] = np.random.random() * 2 - 1

    def Set_ID(self, id):
        self.myID = id



