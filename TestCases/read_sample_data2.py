import numpy as np
import emgMath
import plotUtils

sampleN = int(125/5)
ch2Offset = 0
trimN = 100

filePath1 = r'C:\Users\joyce\OneDrive\Documents\GitHub\EmgSimulator\Ray_Sample_data\Rest_1.npz'
filePath2 = r'C:\Users\joyce\OneDrive\Documents\GitHub\EmgSimulator\Ray_Sample_data\Rest_2.npz'

data1 = np.load(filePath1, allow_pickle=True)
data2 = np.load(filePath2, allow_pickle=True)

data1 = data1['arr_0'].T
data2 = data2['arr_0'].T

title1= filePath1.split('\\')[-1].split('.')[0]
title2= filePath2.split('\\')[-1].split('.')[0]



signal1 = emgMath.processExgData(data1, samples = sampleN, ch2Offset = ch2Offset, trimN = trimN, title = title1)
signal2 = emgMath.processExgData(data2, samples = sampleN, ch2Offset = ch2Offset, trimN = trimN, title = title2)

plotUtils.PlotTwoExgData(signal1= signal1, signal2 = signal2)
