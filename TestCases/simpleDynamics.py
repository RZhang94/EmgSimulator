import emgMath
import matplotlib.pyplot as plt
import numpy as np

gaussian = emgMath.generateGaussianCurve()
accel, velocity, position = emgMath.integrateAccelTimeline(inputForce = gaussian, gravity= -3.95, positionLimit= 0)

fig, ax = plt.subplots(3,1)
ax[0].plot(accel)
ax[0].set_title('acceleration')
ax[1].plot(velocity)
ax[1].set_title('velocity')
ax[2].plot(position)
ax[2].set_title('position')
plt.show()

print('hi')
