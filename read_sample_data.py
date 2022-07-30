import numpy as np
import emgMath

# load the data
# change your own path here
file_path = '/Users/a601081/Documents/GitHub/EmgSimulator/Ray_Sample_data/Pull_fast_1.npz'
file_path2 = '/Users/a601081/Documents/GitHub/EmgSimulator/Ray_Sample_data/Push_fast_1.npz'

sample_data = np.load(file_path, allow_pickle=True)
sample_data2 = np.load(file_path2, allow_pickle=True)

sample_data = sample_data['arr_0'].T
sample_data2 = sample_data2['arr_0'].T

rect_data = emgMath.rectification(sample_data)
rect_data2 = emgMath.rectification(sample_data2)

sampleNumber = 35
avg_data = emgMath.movingAverage(rect_data, samples=sampleNumber)
avg_data2 = emgMath.movingAverage(rect_data2, samples=sampleNumber)

# plot the data
import matplotlib.pyplot as plt
fig,ax = plt.subplots(3,2)
ax[0,0].plot(sample_data[:,100:])  
     # because the front 100 data is quite noisy/abnormal
ax[1,0].plot(rect_data[:,100:])
ax[2,0].plot(avg_data[:,100:])

ax[0,1].plot(sample_data2[100:,:])  
     # because the front 100 data is quite noisy/abnormal
ax[1,1].plot(rect_data2[100:,:])
ax[2,1].plot(avg_data2[100:,:])
plt.show()

print('hi')