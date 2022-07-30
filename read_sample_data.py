import numpy as np
import emgMath
import matplotlib.pyplot as plt

file_path = r'C:\Users\joyce\OneDrive\Documents\GitHub\EmgSimulator\Ray_Sample_data\Pull_fast_1.npz'
file_path2 = r'C:\Users\joyce\OneDrive\Documents\GitHub\EmgSimulator\Ray_Sample_data\Push_fast_1.npz'

sample_data = np.load(file_path, allow_pickle=True)
sample_data2 = np.load(file_path2, allow_pickle=True)

sample_data = sample_data['arr_0'].T
sample_data2 = sample_data2['arr_0'].T


sampleN = 25
sampleDataAvg = emgMath.getMovingAverage(sample_data, samples= sampleN)
sampleDataAvg2 = emgMath.getMovingAverage(sample_data2, samples= sampleN)

differentialForce1 = sampleDataAvg[0,:] - sampleDataAvg[1,:]
differentialForce2 = sampleDataAvg2[0,:] - sampleDataAvg2[1,:]


# plot the data
fig,ax = plt.subplots(4,2)
ax[0,0].set_title('Pull Raw Data')
ax[0,0].plot(sample_data[0,100:], label = 'bicep')
ax[0,0].plot(sample_data[1,100:], label = 'tricep')
ax[0,0].legend()


ax[1,0].set_title('Pull filtered Data')
ax[1, 0].plot(sampleDataAvg[0, 100:], label='bicep')
ax[1, 0].plot(sampleDataAvg[1, 100:], label='tricep')
ax[1,0].legend()

ax[2,0].set_title('Pull force differential')
ax[2, 0].plot(differentialForce1[ 100:])
#
# ax[3,0].set_title('Pull Speed')
# ax[3, 0].plot(speed1[ 100:])

ax[0,1].set_title('Push Raw Data')
ax[0,1].plot(sample_data2[0,100:], label = 'bicep')
ax[0,1].plot(sample_data2[1,100:], label = 'tricep')
ax[0,1].legend()

ax[1,1].set_title('Push filtered Data')
ax[1, 1].plot(sampleDataAvg2[0, 100:], label='bicep')
ax[1, 1].plot(sampleDataAvg2[1, 100:], label='tricep')
ax[1,1].legend()

ax[2,1].set_title('Push force differential')
ax[2, 1].plot(differentialForce2[ 100:])
#
# ax[3,1].set_title('Push Speed')
# ax[3, 1].plot(speed2[ 100:])
plt.show()

print('hi')