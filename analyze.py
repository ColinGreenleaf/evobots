import numpy as numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
print(backLegSensorValues)

plt.plot(backLegSensorValues)
plt.show()
