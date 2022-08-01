# EmgSimulator

*Code implementation for virtual arm controlled by EMG signal*


## Requirements
Packages: matplotlib, pygame, numpy, pyserial 

Hardware: Arduino, BioEXG

## Hardware preparation
1. Connect the Arduino with the BioEXG
2. Place BioEXG electrods on Bicep and Tricep
3. Compile the .ino script on Arduino, get the hardware ready!

## Implementation

### Collection Data
'''
python ./Data_collection/Sample_Experiment.py
```
 and follow the instruction, data will be automatic stored
 
### (Option) Analyse Data
To perform filter, and generate force, velocity, position of the arm.
'''
python ./TestCases/read_sample_data2.py
'''

### Virtual Arm Movement
Directly run (after data collection)
'''
python ./Experiment_pipeline/armtest_withSignal_both.py
'''
  the movement of the virtual arm would be displayed
  
Have fun!!!


 
 
