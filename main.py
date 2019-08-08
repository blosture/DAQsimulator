# Data API testing project.
# Author: Subrat Pathak

# This script simulates data generation by sensors 
# and imaging devices typically used in research 
# labs working with Deep Learning. 

# I have used EEG sensor data as  reference.

# Parameters:
# 1. Duration of data generation in seconds => timeDuration
# 2. Rate of data generation in kb/sec => dataRate

import sys
import numpy as np
import requests
import random
import sched, time
import datetime

import blosture as blos

# Multithreaded execution of listner will go to 
# Blosture's Library
from multiprocessing import Pool

timeDuration = sys.argv[1]
dataRate = sys.argv[2]

print "Time Duration: ", timeDuration
print "Data output rate: ", dataRate

sampleVariable = np.random.uniform(low=-100.000, high=100.000)
sampleVariableSize = sys.getsizeof(sampleVariable)

numerOfRandomVariables = int(dataRate)/sampleVariableSize
print "Number of random varibles to generate per second: ", numerOfRandomVariables

# Function to add given duration to current time, used for getting the stop time for the scheduler.
def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()

startTime = datetime.datetime.now().time()
print startTime
# stopTime = startTime + datetime.timedelta(10)
stopTime = addSecs(startTime, int(timeDuration))

s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    # Calculate a random vector
    vector = np.random.uniform(low=-100.000, high=100.000, size=(numerOfRandomVariables,))
    pool = Pool(processes=1)              # Start a worker processes.
    result = pool.apply_async(blos.listen, [vector], )
    # print vector
    if(datetime.datetime.now().time() > stopTime):
        blos.release_listener()
    	return
    s.enter(.1, 1, do_something, (sc,))

s.enter(.4, 1, do_something, (s,))
s.run()
