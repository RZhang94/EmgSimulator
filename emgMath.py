import numpy as np

def rectification(signal):
    squaredSignal = np.power(signal, 2)
    positiveSignal = np.power(squaredSignal , 1/2)
    return positiveSignal

def movingAverage(signal, samples = 5):
    signalShape = signal.shape
    newShape = (signal.shape[0], signal.shape[1]+samples -1)
    newVector = np.zeros(shape=newShape)
    newVector[:,samples-1:] = signal
    movingAverage = np.zeros(shape=signalShape)
    for i in range(signalShape[1]):
        for j in range(signalShape[0]):
            movingAverage[j,i] = np.sqrt(np.sum(newVector[j, i:i+samples])/samples)

    return movingAverage

def generateRandomVector(range, magnitude = 20):
    vector = magnitude*(np.random.rand(1,range)-0.5)
    key = np.arange(100)
    return vector, key