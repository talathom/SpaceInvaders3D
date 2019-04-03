import viz   
from Model import *

class Player():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0
		self.theta = 0
		self.playerShip = Model('playerShip.dae')
		
		# Deletes the ship
	def delete(self):
		pass
		
		#Moves the ship to a new center at x, y
	def setPosition(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		self.playerShip.setOrientation(self.x, self.y, self.z, 2, 180, self.theta,0)
		
	def rotate(self, zrot):
		self.theta += zrot
		if self.theta >= 360:
			self.theta -= 360
		self.playerShip.setZRotation(zrot)
		self.playerShip.setOrientation(self.x, self.y, self.z, 2, 180, self.theta,0)
		
	def canGoRight(self, rateOfMovement):
		if self.x  + rateOfMovement > 1:
			return False
		else: 
			return True
		
	def canGoLeft(self, rateOfMovement):
		if self.x  + rateOfMovement < -1:
			return False
		else: 
			return True
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def getZ(self):
		return self.z