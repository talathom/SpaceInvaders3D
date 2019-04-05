from Model import *

class Alien():
	def __init__(self, model, color):
		self.x = 0
		self.y = 0
		self.z = 0
		self.theta = 0
		self.color = color
		self.alien = Model(model)
		self.canFire = True
	
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
		
	def isOffScreen(self):
		if self.z < -.8:
			return True
		else:
			return False
			
	def delete(self):
		self.alien.remove()
		
	def getColor(self):
		return self.color
		
	def canFire(self):
		return self.canFire
		
	def fire(self):
		self.canFire = False
	
	def reload(self):
		self.canFire = True
		
	
			
	#HITBOX:  X = +- .2, Y = 0, 2, Z = Z+-.2 