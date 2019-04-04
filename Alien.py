from Model import *

class Alien():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0
		self.theta = 0
		self.alien = Model('alien.dae')
	
	# Move the alien around on x, y, z no rotation
	def setPosition(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		self.alien.setOrientation(self.x, self.y, self.z, .0025, 180, self.theta,0)
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def getZ(self):
		return self.z