﻿import viz   
from Model import *

class Player():
	def __init__(self, hp=1):
		self.x = 0
		self.y = 0
		self.z = 0
		self.theta = 0
		self.hp = hp
		self.playerShip = Model(filename='playerShip.dae')
		
		# Deletes the ship
	def delete(self):
		self.playerShip.remove()
		
		#Moves the ship to a new center at x, y, no rotation
	def setPosition(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		self.playerShip.setOrientation(self.x, self.y, self.z, 2, 180, self.theta,0)
		
		# Rotates the player on the Z axis
	def rotate(self, zrot):
		self.theta += zrot
		if self.theta >= 360:
			self.theta -= 360
		self.playerShip.setZRotation(zrot)
		self.playerShip.setOrientation(self.x, self.y, self.z, 2, 180, self.theta,0)
		
		# Boolean, Checks if the player can move right
	def canGoRight(self, rateOfMovement):
		if self.x  + rateOfMovement > 1:
			return False
		else: 
			return True
		# Boolean, checks if the player cna move left
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
	
	def delete(self):
		self.playerShip.remove()
		
	def getHP(self):
		return self.hp
		
	def damage(self, damage):
		self.hp -= damage
		
	def powerUp(self):
		self.hp += 1
		
	#Hitbox: .05 = X, Z= .09