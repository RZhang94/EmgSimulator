import numpy as np
import emgMath
import plotUtils

sampleN = 10
ch2Offset = 0
trimN = 100

filePath1 = r'C:\Users\joyce\OneDrive\Documents\GitHub\EmgSimulator\Ray_Sample_data\Pull_fast_1.npz'
filePath2 = r'C:\Users\joyce\OneDrive\Documents\GitHub\EmgSimulator\Ray_Sample_data\Push_fast_2.npz'

data1 = np.load(filePath1, allow_pickle=True)
data2 = np.load(filePath2, allow_pickle=True)

data1 = data1['arr_0'].T
data2 = data2['arr_0'].T

title1= filePath1.split('\\')[-1].split('.')[0]
title2= filePath2.split('\\')[-1].split('.')[0]

signal1 = emgMath.processExgData2(data1, samples = sampleN, ch2Offset = ch2Offset, trimN = trimN, title = '', type = 1)
signal2 = emgMath.processExgData2(data2, samples = sampleN, ch2Offset = ch2Offset, trimN = trimN, title = '', type = -1)

pullScale = 0.003142724588020949
pushScale = 0.0009736624838131844
signal1[4]*=pullScale
signal1[5]*=pullScale
signal1[6]*=pullScale
signal2[4]*=pushScale
signal2[5]*=pushScale
signal2[6]*=pushScale
plotUtils.PlotExgForce(signal= signal1, suptitle= "Bicep Pull")
plotUtils.PlotExgForce(signal= signal2, suptitle= "Tricep Push")



print('hello world')