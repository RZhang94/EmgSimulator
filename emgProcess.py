import numpy as np
import emgMath
import plotUtils

def ProcessData(filePath1, filePath2, saveName= None, sampleN = 15, ch2Offset = -0.3, trimN = 100, gainCh1 =1, gainCh2 = 2):
    data1 = np.load(filePath1, allow_pickle=True)
    data2 = np.load(filePath2, allow_pickle=True)

    data1 = data1['arr_0'].T
    data2 = data2['arr_0'].T

    title1= filePath1.split('\\')[-1].split('.')[0]
    title2= filePath2.split('\\')[-1].split('.')[0]

    signal1 = emgMath.processExgData(data1, samples = sampleN, ch2Offset = ch2Offset, trimN = trimN, title = title1, gainCh1= gainCh1, gainCh2 = gainCh2)
    signal2 = emgMath.processExgData(data2, samples = sampleN, ch2Offset = ch2Offset, trimN = trimN, title = title2, gainCh1= gainCh1, gainCh2 = gainCh2)

    plotUtils.PlotTwoExgData(signal1= signal1, signal2 = signal2)
