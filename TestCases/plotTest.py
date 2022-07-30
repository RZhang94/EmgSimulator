import numpy as np

import emgMath
import plotUtils

vector, key = emgMath.generateRandomVector(100)
rectifiedSignal = emgMath.rectification(vector)
movingAverage = emgMath.movingAverage(rectifiedSignal, samples = 5)
movingAverage2 = emgMath.movingAverage(rectifiedSignal, samples = 3)
plotUtils.PlotGraph(((rectifiedSignal, key, 'rectified signal')))

print('processarinod?')
