import matplotlib.pyplot as plt
import numpy as np
import constants as c
import sys
import os


#plot the values stored in data8legs.npy
data = np.load('data8legs.npy')
# label the x and y axes
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.plot(data)
plt.show()



