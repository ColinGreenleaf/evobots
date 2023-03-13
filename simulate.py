import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import constants as c
import sys
from simulation import SIMULATION


directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.RUN()
simulation.Get_Fitness()


