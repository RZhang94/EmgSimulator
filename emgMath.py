import numpy as np

def processExgData(signal, samples = 12, ch2Offset = -0.3, trimN = 100, returnCompression = 1,
                   title = 'Blank', gainCh1 = 1, gainCh2 = 1, type = 1):
    listOfArrays = convertDataToForce(signal = signal, samples = samples, ch2Offset= ch2Offset, gainCh1= gainCh1, gainCh2=gainCh2)
    trimmedArrays = trimListOfArraysColByFirstN(listOfArrays, trimN = trimN)
    originalSignal = trimmedArrays[0]

    avgSignal = trimmedArrays[1]
    diffForce = trimmedArrays[2]

    ##Filter force
    searchN = 6
    filtForce = np.zeros(shape = len(diffForce))
    filtForceExtended = np.zeros(shape = len(diffForce)+ searchN)
    filtForceExtended[:-searchN] = diffForce
    for i in range(searchN,len(diffForce)):
        filtForce[i] = max(filtForceExtended[i-searchN:i+searchN])
    filtForce = filtForce * type
    value = np.sign(filtForce)
    magnitude = np.power(np.power(filtForce,2), 1/8)
    filtForce = np.multiply(value, magnitude)
    # filtForce = low_pass_filter(diffForce)


    #Kinematic model, find 0
    gravityGuess = -0.7
    accel, velocity, position = integrateAccelTimeline(filtForce, gravity= gravityGuess)
    print(position[-1])
    # while position[-1]>max(position)*0.01:
    #     gravityGuess -= 0.005
    #     accel, velocity, position = integrateAccelTimeline(filtForce, gravity=gravityGuess)
    #     print(position[-1])

    if returnCompression:
        return [originalSignal, avgSignal, diffForce, filtForce, accel, velocity, position, title]
    else:
        return originalSignal, avgSignal, diffForce, filtForce, accel, velocity, position, title

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
    positiveSignal[positiveSignal<5] = 0
    lowPassSignal1 = low_pass_filter(positiveSignal[0,:], bandlimit= 32)
    lowPassSignal2 = low_pass_filter(positiveSignal[1,:], bandlimit= 32)
    signal2 = np.vstack((lowPassSignal1, lowPassSignal2))
    signal2[signal2<5] = 0

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(2,1)
    ax[0].plot(positiveSignal[0,:])
    ax[1].plot(signal2[0,:])
    plt.show()
    return signal2

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

def integrateAccelTimeline(inputForce, initialVelocity = 0, initialPosition = 0, gravity = 0, positionLimit = 0):
    #Create arrays
    dataShape = len(inputForce)+1
    accel = np.zeros(shape = dataShape)
    velocity = np.zeros(shape=dataShape)
    position = np.zeros(shape=dataShape)
    ##Set initial conditions
    accel[0:1] = inputForce[0] + gravity
    position[0:1] = initialPosition
    velocity[0:1] = initialVelocity
    if accel[0] < 0 and position[0] <= positionLimit:
        accel[0:1] = 0
        velocity[0:1] = 0
        position[0:1] = positionLimit

    ##Advance Time
    for i in range(2,dataShape):
        #Calculate initial force
        accel[i] = inputForce[i-1] + gravity
        velocity[i] = velocity[i-1]+accel[i-1]
        position[i] = position[i-1]+velocity[i-1]

        if accel[i] < 0 and position[i-1] <= positionLimit:
            accel[i] = 0
            velocity[i] = 0
            position[i] = positionLimit
        
        if position[i] < positionLimit:
            position[i] = positionLimit
        if position[i] < positionLimit:
            position[i] = positionLimit
            velocity[i] = 0
    return accel[2:], velocity[2:], position[2:]

def low_pass_filter(adata: np.ndarray, bandlimit: int = 8, sampling_rate: int = 125) -> np.ndarray:
    # translate bandlimit from Hz to dataindex according to sampling rate and data size
    bandlimit_index = int(bandlimit * adata.size / sampling_rate)
    fsig = np.fft.fft(adata)
    for i in range(bandlimit_index + 1, len(fsig) - bandlimit_index):
        fsig[i] = 0
    adata_filtered = np.fft.ifft(fsig)
    return np.real(adata_filtered)

