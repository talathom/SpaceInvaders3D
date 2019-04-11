from Model import *

class Alien():
	def __init__(self, color, modelLabel=None, model=None, hp=1):
		self.x = 0
		self.y = 0
		self.z = 0
		self.theta = 0
		self.hp = hp
		self.color = color
		self.scale = .0025
		if modelLabel != None:
			self.alien = Model(filename=modelLabel)
		elif model != None:
			self.alien = Model(node=model)
		self.canFire = True
		
	
	# Move the alien around on x, y, z no rotation
	def setPosition(self, x, y, z, scale=.0025):
		self.x = x
		self.y = y
		self.z = z
		self.scale = scale
		self.alien.setOrientation(self.x, self.y, self.z, self.scale, 180, self.theta,0)
		
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
		
	def getHP(self):
		return self.hp
		
	def damage(self):
		self.hp = self.hp - 1
		
	def clone(self):
		return self.alien.clone()
		
	def getScale(self):
		return self.scale
	
			
	#HITBOX:  X = +- .2, Y = 0, 2, Z = Z+-.2 