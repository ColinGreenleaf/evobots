import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5


pyrosim.Start_SDF("boxes.sdf")

for i in range(-2, 3):
    for j in range(-2, 3):
        l = 1
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x+i, y+j, z + k], size=[length * l, width * l, height * l])
            l *= 0.9




pyrosim.End()
