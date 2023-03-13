import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import constants as c
from simulation import SIMULATION


simulation = SIMULATION()
simulation.RUN()
simulation.Get_Fitness()


