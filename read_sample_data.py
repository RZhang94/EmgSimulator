import numpy as np


# load the data
# change your own path here
file_path = '/Users/zhangzhaoxiang/Documents/GitHub/EmgSimulator/Ray_Sample_data/Pull_fast_1.npz'
sample_data = np.load(file_path, allow_pickle=True)
sample_data = sample_data['arr_0']
print(sample_data.shape)

# plot the data
import matplotlib.pyplot as plt
plt.plot(sample_data[100:,:])       # because the front 100 data is quite noisy/abnormal
plt.show()
