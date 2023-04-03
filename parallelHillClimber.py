import os

from solution import SOLUTION
import constants as c
import copy
class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        # self.parent = SOLUTION()
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
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
    def Show_Best(self):
        #find the parent with the best fitness
        bestParent = self.parents[0]
        for i in range(0, c.populationSize):
            if self.parents[i].fitness < bestParent.fitness:
                bestParent = self.parents[i]
        bestParent.Evaluate("GUI")


    def Evaluate(self, solutions):
        for i in range(0, c.populationSize):
            solutions[i].Start_Simulation("DIRECT")

        for i in range(0, c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()

