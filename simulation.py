from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import time

class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.planeId = p.loadURDF("plane.urdf")
        self.robotId = p.loadURDF("body.urdf")
        p.loadSDF("world.sdf")

        pyrosim.Prepare_To_Simulate(self.robotId)
        self.robot.Prepare_To_Sense()

    def RUN(self):
        for i in range(c.loopAmt):
            p.stepSimulation()
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=robotId,
            #     jointName=b"Torso_BackLeg",
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=targetAnglesB[i],
            #     maxForce=c.motorForce)
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=robotId,
            #     jointName=b"Torso_FrontLeg",
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=targetAnglesF[i],
            #     maxForce=c.motorForce)
            time.sleep(1./1000.)
            print(i)

    def __del__(self):
        p.disconnect()
