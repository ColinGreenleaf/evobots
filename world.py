import pybullet


class WORLD:

    def __int__(self):
        pybullet.loadSDF("world.sdf")
        self.planeId = pybullet.loadURDF("plane.urdf")