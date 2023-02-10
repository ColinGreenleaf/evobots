from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import time

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()

        self.planeId = p.loadURDF("plane.urdf")
        # self.robotId = p.loadURDF("body.urdf")
        # p.loadSDF("world.sdf")


    def RUN(self):
        for t in range(c.loopAmt):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Act(t)
            time.sleep(1./1000.)
            print(t)

    def __del__(self):
        p.disconnect()
