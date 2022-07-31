# Importing Libraries
from multiprocessing.connection import wait
from random import sample
from tracemalloc import start
import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import os
import emgProcess

buffer_time = 6
sample_frequency = 125
num_Channels = 2
tao = 1/sample_frequency

# Experiment_name_list = ['Pull', 'Push', 'Rest']
Experiment_name_list = ['Rest']
Level_list = ['slow', 'fast']
# Level_list = ['fast']
Experiment_number_list = ['0', '1']

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


def read():
    data = arduino.readline()
    return data
# while 1:




def conduct_experiment(name, experiment_full_name, sample_frequency, buffer_time, num_Channels):

    raw_data_list = []
    read_lenth_list = []
    index = 0
    loop_time = 0
    # buffer_array = np.zeros([num_Channels, sample_frequency])
    buffer_array = np.zeros([sample_frequency*buffer_time, num_Channels])

    time.sleep(2)
    print("start")
    print("*"*30)
    start_time = time.time()
    while loop_time<buffer_time:
        
        value = read()
        loop_time += tao
        data = value.decode("utf-8")

        # set a function to parse the data
        try:
            Channel_1 = float(data.split(',')[0])
            Channel_2 = float(data.split(',')[1].replace('\r\n', ''))
        
        except:
            continue
        # buffer_array[0][index] = Channel_1
        # buffer_array[1][index] = Channel_2
        
        buffer_array[index][0] = Channel_1
        buffer_array[index][1] = Channel_2
        raw_data_list.append(data)


        read_lenth = len(data)
        read_lenth_list.append(read_lenth)
        index += 1
        

    # print
    end_time = time.time()
    interval_time = end_time - start_time
    print('Average Sample Time', interval_time/(sample_frequency) * 1000)
    # print(buffer_array)
    # print(raw_data_list)
    # print(len(data_list))
    # print(read_lenth_list)

    # plot the n-channel data
    save_folder = name + '_' + 'Sample_data'
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    np.savez(os.path.join(save_folder, '{}.npz'.format(experiment_full_name)), buffer_array)
    # plt.plot(buffer_array[100:,:])
    # plt.legend(['Bicep', 'Tricep'])
    # # plt.show()
    # plt.show(block=False)
    # # plt.pause(3)
    # plt.waitforbuttonpress(0)
    # plt.close()
    sampleN = 15
    ch2Offset = 0
    trimN = 100
    gainCh1 = 1
    gainCh2 = 1
    title = experiment_full_name
    emgProcess.ProcessData(buffer_array, title, sampleN=sampleN, ch2Offset=ch2Offset,trimN=trimN, gainCh1= gainCh1, gainCh2=gainCh2)
    print('done')

name = input('What is your name?\n')
for experiment_name in Experiment_name_list:
    if experiment_name == 'Rest':
        Level_list = ['normal']
    else:
        Level_list = ['slow', 'fast']
    for level in Level_list:
        for experiment_number in Experiment_number_list:
            experiment_full_name = name + '_' + experiment_name + '_' + level + '_' + experiment_number
            print('Expmeriment:  ', experiment_full_name)
            input('Enter to continue')
            print('\n'*10)
            arduino = serial.Serial(port='/dev/cu.usbmodem11101', baudrate=115200, timeout=tao)
            conduct_experiment(name, experiment_full_name,sample_frequency, buffer_time, num_Channels)
            # arduino.flushInput()
            # arduino.flushOutput()
            arduino.close()
        




print('Experiment Finished!!')