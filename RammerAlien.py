from Alien import *
class RammerAlien(Alien):
	def __init__(self):
		# Initialize model
		self.x = 0
		self.y = 0
		self.z = 0
		self.theta = 0
		self.alien = Model('alien.dae')
	