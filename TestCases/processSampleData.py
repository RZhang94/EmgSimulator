import emgProcess

sampleN = 15
ch2Offset = 0
trimN = 100

filePath1 = r'C:\Users\joyce\OneDrive\Documents\GitHub\EmgSimulator\Ray_Sample_data\Pull_fast_1.npz'
filePath2 = r'C:\Users\joyce\OneDrive\Documents\GitHub\EmgSimulator\Ray_Sample_data\Pull_fast_2.npz'

emgProcess.ProcessData(filePath1, filePath2, sampleN=sampleN, ch2Offset=ch2Offset,trimN=trimN)