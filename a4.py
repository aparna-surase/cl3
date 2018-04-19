import threading
import random
import time
from pymongo import MongoClient


class Philosophers(threading.Thread):
	running = True
	connection = MongoClient("mongodb://localhost:27017")

	@staticmethod
	def sendtoMongo(index,name):		#### to make mongodb feel useful
		db=Philosophers.connection.test.mycoll
		post={"phil_index":index,"time":time.ctime(),"phil_name":name}
		db.insert_one(post)

	def __init__(self,i,name,leftfork,rightfork):
		threading.Thread.__init__(self)
		self.index=i
		self.name=name
		self.leftfork=leftfork
		self.rightfork=rightfork

	def run(self):
		while(self.running):
			time.sleep(random.uniform(3,10))
			print(self.name,"is hungry")
			self.checkforks()

	def checkforks(self):
		fork1 , fork2 = self.leftfork, self.rightfork

		while(self.running):
			fork1.acquire(True)
			cond = fork2.acquire(False)
			if(cond):
				break 	###go to eat
			fork1.release()
			print(self.name,"swaps forks")
			fork1 , fork2 = fork2, fork1	### swap forks to change priority of fork picking
		else:			### else for while 	"""lol thats new"""
			return

		self.eat()
		fork2.release()
		fork1.release()

	def eat(self):
		print(self.name,"started eating")
		Philosophers.sendtoMongo(self.index,self.name)
		time.sleep(random.uniform(3,10))
		print(self.name,"stopped eating and is now thinking")


def DiningPhilosophers():
	forks = [threading.Lock() for i in range(5)]
	names=('A','B','C','D','E')
	philosophers = [(Philosophers(i,names[i],forks[i%5],forks[(i+1)%5])) for i in range(5)]

	random.seed(2493)
	Philosophers.running = True
	for i in philosophers:
		i.start()
	time.sleep(30)
	Philosophers.running=False

DiningPhilosophers()
