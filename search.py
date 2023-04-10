import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
from solution import SOLUTION

solution = SOLUTION(0)
solution.Create_Body()

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best(True)

#remove any brain or fitness files
os.system("rm brain*.nndf")
os.system("rm fitness*.txt")