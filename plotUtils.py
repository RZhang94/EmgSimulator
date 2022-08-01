import numpy as np
import matplotlib.pyplot as plt

"""
Package for plotting the data
"""

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
    ax[0,0].set_title(title1 + ' Raw EMG Data')
    ax[0,0].plot(ogSignal1[0,:], label = 'bicep')
    ax[0,0].plot(ogSignal1[1,:], label = 'tricep')
    ax[0,0].legend()


    ax[1,0].set_title(title1 +' Filtered EMG Data')
    ax[1, 0].plot(avgSignal1[0, :], label='bicep')
    ax[1, 0].plot(avgSignal1[1,:], label='tricep')
    ax[1,0].legend()

    ax[2,0].set_title(title1 + ' Channel differential')
    ax[2, 0].plot(diffForce1)

    ax[3,0].set_title(title1 + ' Acceleration Approximation')
    ax[3, 0].plot(filtForce1)

    ax[4,0].set_title('Resultant Acceleration')
    ax[4, 0].plot(accel1)
    ax[5,0].set_title('Resultant Velocity')
    ax[5, 0].plot(velocity1)
    ax[6,0].set_title('Resultant Position')
    ax[6, 0].plot(position1)


    ax[0,1].set_title(title2 +' Raw EMG Data')
    ax[0,1].plot(ogSignal2[0,:], label = 'bicep')
    ax[0,1].plot(ogSignal2[1,:], label = 'tricep')
    ax[0,1].legend()

    ax[1,1].set_title(title2 +' Filtered EMG Data')
    ax[1, 1].plot(avgSignal2[0, :], label='bicep')
    ax[1, 1].plot(avgSignal2[1, :], label='tricep')
    ax[1,1].legend()

    ax[2,1].set_title(title2 + ' Channel Differential')
    ax[2, 1].plot(diffForce2[ :])

    ax[3,1].set_title(title2 + 'Acceleration Approximation')
    ax[3, 1].plot(filtForce2)

    ax[4,1].set_title('Resultant Acceleration')
    ax[4, 1].plot(accel2)
    ax[5,1].set_title('Resultant Velocity')
    ax[5, 1].plot(velocity2)
    ax[6,1].set_title('Resultant Position')
    ax[6, 1].plot(position2)

    plt.show()

    print('hi')

def PlotExgForce(signal, suptitle = 'Blank'):
    ogSignal1 = signal[0]
    avgSignal1 = signal[1]
    diffForce1 = signal[2]
    filtForce1 = signal[3]
    accel1 = signal[4]
    velocity1=signal[5]
    position1 = signal[6]
    title1 = signal[7]

    t= np.arange(0,3.20, 8e-3)
    tm1 = t[:-1]

    fig,ax = plt.subplots(7,1, figsize= (8,7))
    ax[0].set_title('Captured \n EMG Data', rotation='horizontal',x=-0.2,y=0.1, fontsize = 11)
    ax[0].set_ylabel('ADU')
    ax[0].set_ylim([-255,255])
    ax[0].tick_params(axis = 'y', labelsize = 9)
    ax[0].set_xticks([])
    ax[0].plot(t,ogSignal1[0,:], label = 'Bicep')
    ax[0].plot(t,ogSignal1[1,:], label = 'Tricep')
    ax[0].legend(loc = 1)


    ax[1].set_title(title1 +' Filtered \n EMG Data', rotation='horizontal',x=-0.2,y=0.1, fontsize = 11)
    ax[1].plot(t,avgSignal1[0, :], label='Bicep')
    ax[1].plot(t,avgSignal1[1,:], label='Tricep')
    ax[1].set_ylabel('EMG \n Units')
    ax[1].set_ylim([0,12])
    ax[1].tick_params(axis='y', labelsize=9)
    ax[1].set_xticks([])
    ax[1].legend()

    ax[2].set_title(title1 + ' Channel \n Differential', rotation='horizontal',x=-0.2,y=0.1, fontsize = 11)
    ax[2].set_ylabel('EMG \n Units')
    ax[2].set_ylim([-5,5])
    ax[2].tick_params(axis='y', labelsize=9)
    ax[2].set_xticks([])
    ax[2].plot(t, np.zeros(shape = t.shape), 'k:')
    ax[2].plot(t,diffForce1)

    ax[3].set_title(title1 + ' Acceleration \n Approximation', rotation='horizontal',x=-0.2,y=0.1, fontsize = 11)
    ax[3].tick_params(axis='y', labelsize=9)
    ax[3].set_xticks([])
    ax[3].plot(t,filtForce1)

    ax[4].set_title('Resultant \n Acceleration', rotation='horizontal',x=-0.2,y=0.1, fontsize = 11)
    ax[4].tick_params(axis='y', labelsize=9)
    ax[4].set_xticks([])
    ax[4].plot(tm1, np.zeros(shape = tm1.shape), 'k:')
    ax[4].plot(tm1, accel1)

    ax[5].set_title('Resultant \n Velocity', rotation='horizontal',x=-0.2,y=0.1, fontsize = 11)
    ax[5].plot(tm1, np.zeros(shape = tm1.shape), 'k:')
    ax[5].plot(tm1,velocity1)
    ax[5].tick_params(axis='y', labelsize=9)
    ax[5].set_xticks([])

    ax[6].set_title('Resultant \n Position', rotation='horizontal',x=-0.2,y=0.1, fontsize = 11)
    ax[6].plot(tm1,position1)
    ax[6].tick_params(axis='y', labelsize=9)
    ax[6].set_xlabel('Time (s)')

    plt.suptitle(suptitle, fontsize = 16)
    plt.subplots_adjust(left=0.236,
                        bottom=0.07,
                        right=1,
                        top=0.91,
                        wspace=0.2,
                        hspace=0.15)
    plt.show()

    print('hi')