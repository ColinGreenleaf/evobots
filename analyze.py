import numpy as numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
print(backLegSensorValues)

plt.plot(backLegSensorValues, label="back leg", linewidth=2)
plt.plot(frontLegSensorValues, label="front leg",)
plt.legend()
plt.show()
