# Data API testing project.
# Author: Subrat Pathak

# This library handles Data Acquisition through listners and 
# transfers the data to Blosture's Cloud infrastructure.

import sys
import numpy as np
import requests
import random
import time
import datetime
import json
import util
import os

endpoint = "http://localhost:4000/api/listen"
# endpoint = "http://ec2-18-217-87-55.us-east-2.compute.amazonaws.com:4000/api/listen"

session = requests.Session()

class firescale:
	apiKey = "apiKey"
	apiEndpoint = "http://localhost:4000/api/listen"
	localFileObj = ""
	projectId = "projectId"
	pushedData = ""
	timeStamp = ""
	payload = ""

	def __init__(self,apiKey,projectId):
		self.apiKey = apiKey
		self.projectId = projectId
		self.localFileObj = open("blosData3",'a')
		self.pushedData = "START"
		print "Obj creeated"

	def push(self,dataValue):
		self.pushedData = str(dataValue)
		self.timeStamp = util.fetch_system_time()
		if False: #check for internet connection here. Remove True
			self.createPayload()
			session.post(self.apiEndpoint, json=self.payload)#Send payload with HTTP using requests library.
		else:
			self.localFileObj.write(self.create_chunk())
			self.localFileObj.flush()
			os.fsync(self.localFileObj.fileno())#Ensure that the file is written

	def create_chunk(self):
		chunk = {
		'timeStamp':self.timeStamp,
		'dataToStore':self.pushedData,
		'projectId':self.projectId
		}
		return str(chunk)

	def release(self):
		self.localFileObj.close()
		print "Done"

	def createPayload(self):
		self.payload = {
			 'apiKey': self.apiKey,
			 'dataSubset': self.projectId,
			 'projectName': self.projectId,
			 'timeStamp': self.timeStamp,
			 'dataToStore': self.pushedData
			}

	# def listen(self,serialObject):
	# 	self.ser = serial.Serial()
	# 	if self.ser.isOpen():
	# 		return (self.ser.readline())

	# def createPayload(self,dataObject):
	# 	sizeOfDataObject = sys.getsizeof(dataObject)
	# 	payload = {
	# 		 'apiKey': '3cq7WFKNlW',
	# 		 'dataSubset': 'Stimulus_02',
	# 		 'projectName': 'EEG',
	# 		 'timeStamp': str(datetime.datetime.now()),
	# 		 'dataToStore': str(dataObject)
	# 		}
	# 	return payload