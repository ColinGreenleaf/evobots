import os

from solution import SOLUTION
import numpy as np
import constants as c
import copy
class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        # self.data is a numpy matrix with c.populationSize rows and c.numberOfGenerations columns
        self.data = np.zeros((c.populationSize, c.numberOfGenerations))
        self.parents = {}
        self.nextAvailableID = 0
        # self.parent = SOLUTION()
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    def Evolve(self):
        self.Evaluate(self.parents, currentGeneration=0)
        currentGeneration = 0
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)
            currentGeneration += 1

    def Evolve_For_One_Generation(self, currgen):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children, currgen)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in range(0, c.populationSize):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for each in self.children:
            self.children[each].Mutate()

    def Select(self):
        for i in range(0, c.populationSize):
            if self.children[i].fitness < self.parents[i].fitness:
                self.parents[i] = self.children[i]
                # print("child is better than parent")
    def Print(self):
        print("")
        # print both fitnesses on one line rounded to 3 decimal places
        for i in range(0, c.populationSize):
            print("parent fitness: ", round(self.parents[i].fitness, 3), "child fitness: ", round(self.children[i].fitness, 3))

        print("")
    def Show_Best(self, eval):
        #find the parent with the best fitness
        bestParent = self.parents[0]
        for i in range(0, c.populationSize):
            if self.parents[i].fitness < bestParent.fitness:
                bestParent = self.parents[i]


        if os.path.exists("brain" + str(bestParent.myID) + ".nndf"):
            os.system("cp brain" + str(bestParent.myID) + ".nndf best/brain.nndf")
        # remove all brains
        os.system("rm brain*.nndf")

        if eval == True:
            bestParent.Evaluate("GUI")


    def Evaluate(self, solutions, currentGeneration):
        for i in range(0, c.populationSize):
            solutions[i].Start_Simulation("DIRECT")

        for i in range(0, c.populationSize):
            self.data[i, currentGeneration] = solutions[i].Wait_For_Simulation_To_End()

        self.Show_Best(False)

    def saveData(self):
        np.save("data.npy", self.data)

