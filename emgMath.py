import numpy as np

def processExgData(signal, samples = 12, ch2Offset = -0.3, trimN = 100, returnCompression = 1,
                   title = 'Blank', gainCh1 = 1, gainCh2 = 1):
    listOfArrays = convertDataToForce(signal = signal, samples = samples, ch2Offset= ch2Offset, gainCh1= gainCh1, gainCh2=gainCh2)
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

def convertDataToForce(signal, samples = 12, ch2Offset = -0.3, gainCh1 = 1, gainCh2 = 1):
    #Check data format
    if signal.shape[0]> signal.shape[1]:
        signal = signal.T
    avgData = getMovingAverage(signal, samples= samples)
    avgData[1,:] += ch2Offset
    avgData[0,:] *= gainCh1
    avgData[1,:] *= gainCh2
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
            #movingAverage[j,i] = (np.sum(newVector[j, i:i+samples])/samples)
            movingAverage[j,i] = np.sqrt(np.sum(newVector[j, i:i+samples])/samples)

    return movingAverage

def generateRandomVector(range, magnitude = 20):
    vector = magnitude*(np.random.rand(1,range)-0.5)
    key = np.arange(100)
    return vector, key

def generateGaussianCurve(length = 100, magnitude = 5, variance = 20):
    halfsize = length/2
    vector = np.arange(-halfsize, halfsize)
    vector2 = np.exp(-1/2*(vector/variance)**2)*magnitude
    return vector2

def integrateCurveFullT(curve, initialCondition = None):
    dataShape = curve.shape
    integral = np.zeros(shape=(dataShape))
    if len(dataShape)>1:
        return 1
    else:
        if initialCondition == None:
            initialCondition = 0
        integral[0] = initialCondition
        for i in range(1,len(curve[:])):
            integral[i] += integral[i-1] + curve[i-1]

    return integral

def integrateAccelTimeline(inputForce, initialVelocity = 0, initialPosition = 0, gravity = 0):
    #Create arrays
    dataShape = len(inputForce)+1
    accel = np.zeros(shape = dataShape)
    velocity = np.zeros(shape=dataShape)
    position = np.zeros(shape=dataShape)
    ##Set initial conditions
    accel[0:1] = inputForce[0] + gravity
    position[0:1] = initialPosition
    velocity[0:1] = initialVelocity
    if accel[0] < 0 and position[0] <=-5:
        accel[0:1] = 0
        velocity[0:1] = 0

    ##Advance Time
    for i in range(2,dataShape):
        #Calculate initial force
        accel[i] = inputForce[i-1] + gravity

        if accel[i] < 0 and position[i-1] <= -5:
            accel[i] = 0
            velocity[i] = 0

        velocity[i] = velocity[i-1]+accel[i-1]
        position[i] = position[i-1]+velocity[i-1]

    return accel[2:], velocity[2:], position[2:]