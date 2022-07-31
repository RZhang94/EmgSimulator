import sys
sys.path.append('/Users/zhangzhaoxiang/Documents/GitHub/EmgSimulator')


import emgMath
import matplotlib.pyplot as plt

constant = 2.4

gaussian = emgMath.generateGaussianCurve()
integral = emgMath.integrateCurveFullT(gaussian)
integral2 = emgMath.integrateCurveFullT(integral)

fig, ax = plt.subplots(3,2)
ax[0,0].plot(gaussian)
ax[1,0].plot(integral)
ax[2,0].plot(integral2)

gaussianMinus = gaussian - constant
integralMinus = emgMath.integrateCurveFullT(gaussianMinus)
integral2Minus = emgMath.integrateCurveFullT(integralMinus)
ax[0,1].plot(gaussianMinus)
ax[1,1].plot(integralMinus)
ax[2,1].plot(integral2Minus)
plt.show()

print('hi')
