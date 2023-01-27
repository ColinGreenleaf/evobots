import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="box", pos=[-5, +5, 0.5], size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 0.5], size=[length,width,height])
    pyrosim.Send_Joint(name="Torso_Leg", parent="Torso", child="Leg", type="revolute", position=[0.5, 0, 1.0])
    pyrosim.Send_Cube(name="Leg", pos=[1, 0, 1.5], size=[length,width,height])
    pyrosim.End()

if __name__ == "__main__":
    Create_World()
    Create_Robot()