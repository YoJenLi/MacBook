from django.db import models

# Create your models here.
from django.shortcuts import render
from pymongo import MongoClient
import sys
import pymongo

# class jobinfo(object):
# 	def __init__(self):
# 		self.client = MongoClient()

# 	def getOnejobInfo(self):
# 		db = self.cliet.mongodb
# 		collection = db.test123

# 		jobInfoList = []
# 		for info in collection.find():
# 			jobInfoList.append(info)
# 		return jobInfoList
		
# 		client.close()


class searchJob(object):
	def __init__(self):
		self.client = MongoClient('192.168.0.103',27017)
	
	def search(self,name):
		db = self.client.mongodb
		collection = db.test123
		
		result = []

		for post in collection.find({"name":{"$regex":name}}):
				
				result.append(post)
		return result
		client.close()








