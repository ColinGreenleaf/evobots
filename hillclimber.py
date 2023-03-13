from solution import SOLUTION
import constants as c
import copy
class HILL_CLIMBER:

    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

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
        self.parent.Evaluate("GUI")
