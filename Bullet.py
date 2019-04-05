from Model import *

class Bullet():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0
		self.theta = 0
		self.vx = 0
		self.vy = 0
		self.vz = .02
		self.bullet = Model('bullet.dae')
	
	def delete(self):
		self.bullet.remove()
		
	def setPosition(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		self.bullet.setOrientation(self.x, self.y, self.z, .005, 45, 0,theta)
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def getZ(self):
		return self.z
		
	def getVX(self):
		return self.vx
	#getter method 	
	def getVY(self):
		return self.vy
	
	def getVZ(self):
		return self.vz
	# setter method	
	def setVXVY(self,vx,vy,vz):
		self.vx = vx
		self.vy = vy
		self.vz = vz
		
	def setTheta(self,ang):
		self.theta += ang;
		
	