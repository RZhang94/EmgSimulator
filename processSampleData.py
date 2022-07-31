import emgProcess

sampleN = 15
ch2Offset = 0
trimN = 100

name = 'Jingxuan'
filePath1 = '/Users/zhangzhaoxiang/Documents/GitHub/EmgSimulator/{}_Sample_data/{}_Rest_normal_0.npz'.format(name, name)
filePath2 = '/Users/zhangzhaoxiang/Documents/GitHub/EmgSimulator/{}_Sample_data/{}_Rest_normal_1.npz'.format(name, name)

emgProcess.ProcessData(filePath1, filePath2, sampleN=sampleN, ch2Offset=ch2Offset,trimN=trimN)