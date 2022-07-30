import emgMath
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,1)
vector, key = emgMath.generateRandomVector(100)
ax[0].plot(key, vector[0,:])

rectifiedSignal = emgMath.rectification(vector)
ax[1].plot(key, rectifiedSignal[0,:])

movingAverage = emgMath.movingAverage(rectifiedSignal, samples = 5)
movingAverage2 = emgMath.movingAverage(rectifiedSignal, samples = 3)
ax[1].plot(key, movingAverage[0,:])
ax[1].plot(key, movingAverage2[0,:])
plt.show()

print('processarinod?')
