import numpy as np
import matplotlib.pylab as plt

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
targetAnglesF = np.load("data/targetAnglesF.npy")
targetAnglesB = np.load("data/targetAnglesB.npy")
# print(backLegSensorValues)
#
# plt.plot(backLegSensorValues, label="back leg", linewidth=2)
# plt.plot(frontLegSensorValues, label="front leg",)
# plt.legend()
# plt.show()

plt.plot(targetAnglesF, label="target", linewidth=2)
plt.plot(targetAnglesB, label="target", linewidth=1)


plt.axis('tight')
plt.show()
