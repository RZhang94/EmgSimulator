import numpy as np
import emgMath_data
import plotUtils_data

def ProcessData(data1, title, saveName= None, sampleN = 15, ch2Offset = -0.3, trimN = 100, gainCh1 =1, gainCh2 = 2):
    data1 = data1.T
    title1 = title
    signal1 = emgMath_data.processExgData(data1, samples = sampleN, ch2Offset = ch2Offset, trimN = trimN, title = title1, gainCh1= gainCh1, gainCh2 = gainCh2)
    plotUtils_data.PlotTwoExgData(signal1= signal1)
