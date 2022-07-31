import emgProcess

sampleN = 15
ch2Offset = -1
trimN = 100
gainCh1 = 1.25
gainCh2 = 1

filePath1 = r'C:\Users\joyce\OneDrive\Documents\GitHub\EmgSimulator\JOSH_Sample_data\Josh_Pull_slow_0.npz'
filePath2 = r'C:\Users\joyce\OneDrive\Documents\GitHub\EmgSimulator\JOSH_Sample_data\Josh_Pull_slow_1.npz'

emgProcess.ProcessData(filePath1, filePath2, sampleN=sampleN, ch2Offset=ch2Offset,trimN=trimN, gainCh1= gainCh1, gainCh2=gainCh2)