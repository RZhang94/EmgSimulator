import matplotlib.pyplot as plt

def PlotTwoExgData(signal1, signal2):
    signalSize = max(len(signal1), len(signal2))
    if signalSize == 4:
        PlotTwoExgForce(signal1, signal2)

def PlotTwoExgForce(signal1, signal2):
    ogSignal1 = signal1[0]
    avgSignal1 = signal1[1]
    diffForce1 = signal1[2]
    title1 = signal1[3]

    ogSignal2 = signal2[0]
    avgSignal2 = signal2[1]
    diffForce2 = signal2[2]
    title2 = signal2[3]

    fig,ax = plt.subplots(3,2)
    ax[0,0].set_title(title1 + ' Raw Data')
    ax[0,0].plot(ogSignal1[0,:], label = 'bicep')
    ax[0,0].plot(ogSignal1[1,:], label = 'tricep')
    ax[0,0].legend()


    ax[1,0].set_title(title1 +' filtered Data')
    ax[1, 0].plot(avgSignal1[0, :], label='bicep')
    ax[1, 0].plot(avgSignal1[1,:], label='tricep')
    ax[1,0].legend()

    ax[2,0].set_title(title1 + ' force differential')
    ax[2, 0].plot(diffForce1[:])
    #
    # ax[3,0].set_title('Pull Speed')
    # ax[3, 0].plot(speed1[ 100:])

    ax[0,1].set_title(title2 +' Raw Data')
    ax[0,1].plot(ogSignal2[0,:], label = 'bicep')
    ax[0,1].plot(ogSignal2[1,:], label = 'tricep')
    ax[0,1].legend()

    ax[1,1].set_title(title2 +' filtered Data')
    ax[1, 1].plot(avgSignal2[0, :], label='bicep')
    ax[1, 1].plot(avgSignal2[1, :], label='tricep')
    ax[1,1].legend()

    ax[2,1].set_title(title2 + ' force differential')
    ax[2, 1].plot(diffForce2[ :])
    #
    # ax[3,1].set_title('Push Speed')
    # ax[3, 1].plot(speed2[ 100:])
    plt.show()

