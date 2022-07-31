import emgMath
import matplotlib.pyplot as plt

gaussian = emgMath.generateGaussianCurve()
accel, velocity, position = emgMath.integrateAccelTimeline(inputForce = gaussian, gravity= -3.95)

fig, ax = plt.subplots(3,1)
ax[0].plot(accel)
ax[1].plot(velocity)
ax[2].plot(position)

plt.show()

print('hi')
