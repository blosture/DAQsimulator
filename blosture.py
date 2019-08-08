# Data API testing project.
# Author: Subrat Pathak

# This library handles Data Acquisition through listners and 
# transfers the data to Blosture's Cloud infrastructure.

import sys
import numpy as np
import requests
import random
import sched, time
import datetime
import requests
import json
import util
import json
import os


endpoint = "http://localhost:4000/api/listen"
# endpoint = "http://ec2-18-217-87-55.us-east-2.compute.amazonaws.com:4000/api/listen"

localFileObj = open("blosData",'a')

def createPayload(dataObject):
	sizeOfDataObject = sys.getsizeof(dataObject)
	payload = {
		 'apiKey': '3cq7WFKNlW',
		 'dataSubset': 'Stimulus_02',
		 'projectName': 'EEG',
		 'timeStamp': str(datetime.datetime.now()),
		 'dataToStore': str(dataObject)
		}
	return payload

def create_chunk(dataObject):
	chunk = {
	'timeStamp':util.fetch_system_time(),
	'value':str(dataObject)
	}
	print chunk
	return str(chunk)


def sendPayload(payload):
	r = requests.post(endpoint, json=payload)
	return r

def listen(dataObject):
	if util.have_internet():
		response = sendPayload(createPayload(dataObject))
	else:
		localFileObj.write(create_chunk(dataObject))
		localFileObj.flush()
		# typically the above line would do. however this is used to ensure that the file is written
		os.fsync(localFileObj.fileno())
		print "Written to local file."

def release_listener():
	localFileObj.close()
	print "Done"