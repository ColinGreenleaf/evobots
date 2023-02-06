import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import constants as c
from simulation import SIMULATION


simulation = SIMULATION()
simulation.RUN()

# x = numpy.linspace(1, c.loopAmt, c.loopAmt)
# targetAnglesF = c.amplitudeF * numpy.sin(c.frequencyF * c.modToFit * x + c.phaseOffsetF)
# targetAnglesB = c.amplitudeB * numpy.sin(c.frequencyB * c.modToFit * x + c.phaseOffsetB)
#
# # numpy.save("data/targetAnglesF.npy", targetAnglesF)
# # numpy.save("data/targetAnglesB.npy", targetAnglesB)
# #
# # exit()
#
#
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,-9.8)
#
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
#
# pyrosim.Prepare_To_Simulate(robotId)
# backLegSensorValues = numpy.zeros(c.loopAmt)
# frontLegSensorValues = numpy.zeros(c.loopAmt)
#
# for i in range(c.loopAmt):
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotId,
#         jointName=b"Torso_BackLeg",
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=targetAnglesB[i],
#         maxForce=c.motorForce)
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotId,
#         jointName=b"Torso_FrontLeg",
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=targetAnglesF[i],
#         maxForce=c.motorForce)
#     time.sleep(1./1000.)
#     print(i)
# numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
# numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
# p.disconnect()

