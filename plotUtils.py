import matplotlib.pyplot as plt

def PlotTwoExgData(signal1, signal2):
    signalSize = max(len(signal1), len(signal2))
    if signalSize == 8:
        PlotTwoExgForce(signal1, signal2)

def PlotTwoExgForce(signal1, signal2):
    ogSignal1 = signal1[0]
    avgSignal1 = signal1[1]
    diffForce1 = signal1[2]
    filtForce1 = signal1[3]
    accel1 = signal1[4]
    velocity1=signal1[5]
    position1 = signal1[6]
    title1 = signal1[7]

    ogSignal2 = signal2[0]
    avgSignal2 = signal2[1]
    diffForce2 = signal2[2]
    filtForce2 = signal2[3]
    accel2 = signal2[4]
    velocity2=signal2[5]
    position2 = signal2[6]
    title2 = signal2[7]

    fig,ax = plt.subplots(7,2)
    ax[0,0].set_title(title1 + ' Raw Data')
    ax[0,0].plot(ogSignal1[0,:], label = 'bicep')
    ax[0,0].plot(ogSignal1[1,:], label = 'tricep')
    ax[0,0].legend()


    ax[1,0].set_title(title1 +' Filtered Data')
    ax[1, 0].plot(avgSignal1[0, :], label='bicep')
    ax[1, 0].plot(avgSignal1[1,:], label='tricep')
    ax[1,0].legend()

    ax[2,0].set_title(title1 + ' Force differential')
    ax[2, 0].plot(diffForce1)

    ax[3,0].set_title(title1 + 'Filtered Force')
    ax[3, 0].plot(filtForce1)

    ax[4,0].set_title('Acceleration')
    ax[4, 0].plot(accel1)
    ax[5,0].set_title('Velocity')
    ax[5, 0].plot(velocity1)
    ax[6,0].set_title('Position')
    ax[6, 0].plot(position1)


    ax[0,1].set_title(title2 +' Raw Data')
    ax[0,1].plot(ogSignal2[0,:], label = 'bicep')
    ax[0,1].plot(ogSignal2[1,:], label = 'tricep')
    ax[0,1].legend()

    ax[1,1].set_title(title2 +' Filtered Data')
    ax[1, 1].plot(avgSignal2[0, :], label='bicep')
    ax[1, 1].plot(avgSignal2[1, :], label='tricep')
    ax[1,1].legend()

    ax[2,1].set_title(title2 + ' Force differential')
    ax[2, 1].plot(diffForce2[ :])

    ax[3,1].set_title(title2 + 'Filtered Force')
    ax[3, 1].plot(filtForce2)

    ax[4,1].set_title('Acceleration')
    ax[4, 1].plot(accel2)
    ax[5,1].set_title('Velocity')
    ax[5, 1].plot(velocity2)
    ax[6,1].set_title('Position')
    ax[6, 1].plot(position2)

    plt.show()

    print('hi')

