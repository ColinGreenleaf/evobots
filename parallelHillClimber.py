from solution import SOLUTION
import constants as c
import copy
class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        # self.parent = SOLUTION()
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    def Evolve(self):
        pass
        for i in range(0, c.populationSize):
            self.parents[i].Evaluate("GUI")
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child
            print("child is better than parent")

    def Print(self):
        # print both fitnesses on one line rounded to 3 decimal places
        print("parent fitness: ", round(self.parent.fitness, 3), "child fitness: ", round(self.child.fitness, 3))

    def Show_Best(self):
        pass
        # self.parent.Evaluate("GUI")
