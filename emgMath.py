import numpy as np

def processExgData(signal, samples = 12, ch2Offset = -0.3, trimN = 100, returnCompression = 1, title = 'Blank'):
    listOfArrays = convertDataToForce(signal = signal, samples = samples, ch2Offset= ch2Offset)
    trimmedArrays = trimListOfArraysColByFirstN(listOfArrays, trimN = trimN)
    originalSignal = trimmedArrays[0]
    avgSignal = trimmedArrays[1]
    diffForce = trimmedArrays[2]
    if returnCompression:
        return [originalSignal, avgSignal, diffForce, title]
    else:
        return originalSignal, avgSignal, diffForce

def trimListOfArraysColByFirstN(listOfArrays, trimN= 100):
    trimmedArrays = []
    for i in range(len(listOfArrays)):
        data = listOfArrays[i]
        if len(data.shape)>1:
            trimmedArrays.append(data[:,trimN:])
        else:
            trimmedArrays.append(data[trimN:])
    return trimmedArrays

def convertDataToForce(signal, samples = 12, ch2Offset = -0.3):
    #Check data format
    if signal.shape[0]> signal.shape[1]:
        signal = signal.T
    avgData = getMovingAverage(signal, samples= samples)
    avgData[1,:] += ch2Offset
    diffForce = avgData[0,:] - avgData[1,:]
    return [signal, avgData, diffForce]
def getMovingAverage(signal, samples = 12):
    rectifiedData = rectification(signal)
    movingAvgData = movingAverage(rectifiedData, samples = samples)
    return movingAvgData
def rectification(signal):
    squaredSignal = np.power(signal, 2)
    positiveSignal = np.power(squaredSignal, 1/2)
    return positiveSignal

def movingAverage(signal, samples = 12):
    signalShape = signal.shape
    newShape = (signal.shape[0], signal.shape[1]+samples -1)
    newVector = np.zeros(shape=newShape)
    newVector[:,samples-1:] = signal
    movingAverage = np.zeros(shape=signalShape)
    for i in range(signalShape[1]):
        for j in range(signalShape[0]):
            movingAverage[j,i] = (np.sum(newVector[j, i:i+samples])/samples)
            # movingAverage[j,i] = np.sqrt(np.sum(newVector[j, i:i+samples])/samples)

    return movingAverage

def generateRandomVector(range, magnitude = 20):
    vector = magnitude*(np.random.rand(1,range)-0.5)
    key = np.arange(100)
    return vector, key