from Player import *
from Alien import *
from Bullet import *
import random
import math

class Controller (viz.EventClass):

	# Constructor 
	def __init__(self):
		# base class constructor 
		viz.EventClass.__init__(self)
		
		self.callback(viz.KEYDOWN_EVENT, self.onKeyDown) # Callback for key press
		self.callback(viz.TIMER_EVENT, self.onTimer) # Callback for timers
		self.callback(viz.KEYUP_EVENT, self.onKeyUp)
		
		#Creates memory for bullets and alien spawns
		self.bulletlist = []
		self.aliens = [None for x in range(0, 18)]
		self.alienbullets = list()
		# Default rotation for camera
		self.theta = 50
		
		#Booleans for keys pressed
		self.leftUp = True
		self.rightUp = True
		self.Fire = False
		self.start = False
		self.pause = False
		
		#Setup default camera view
		self.view = viz.MainView
		mat = viz.Matrix()
		mat.postAxisAngle(1, 0, 0, self.theta)
		mat.postTrans(0, 0, 0)
		self.view.setMatrix(mat)
		
		#Spawn the player
		self.playerShip = Player()
		self.playerShip.setPosition(0, 0, -.6)
		
		self.power = 3
		self.speed = 1/self.power
		
		# Start timers
		self.starttimer(1, .05, viz.FOREVER)
		self.starttimer(2, .05, viz.FOREVER)
		self.starttimer(3, .001, viz.FOREVER)
		self.starttimer(4, self.speed, viz.FOREVER)
		self.starttimer(5, .5, viz.FOREVER)
		self.starttimer(6, .3, viz.FOREVER)
		self.addCoordinateAxes()
		self.spawnAliens()
		
	def spawnAliens(self):
		# Spawns 3x6 aliens
		bluemodel = 'blueAlien.dae'
		redmodel = 'redAlien.dae'
		purplemodel = 'tankAlien.dae'
		
		x = -.6
		for i in range(0, 6):
			num = random.randint(0, 2)
			if num == 0:
				self.aliens[i] = Alien(bluemodel, 'blue')
			elif num == 1:
				self.aliens[i] = Alien(redmodel, 'red')
			elif num == 2:
				self.aliens[i] = Alien(purplemodel, 'purple', hp=3)
			self.aliens[i].setPosition(x, 0, 1)
			x += .25
		
		x = -.6
		for i in range(6, 12):
			num = random.randint(0, 2)
			if num == 0:
				self.aliens[i] = Alien(bluemodel, 'blue')
			elif num == 1:
				self.aliens[i] = Alien(redmodel, 'red')
			elif num == 2:
				self.aliens[i] = Alien(purplemodel, 'purple', hp=3)
			self.aliens[i].setPosition(x, 0, .75)
			x += .25
			
		x = -.6
		for i in range(12, 18):
			num = random.randint(0, 2)
			if num == 0:
				self.aliens[i] = Alien(bluemodel, 'blue')
			elif num == 1:
				self.aliens[i] = Alien(redmodel, 'red')
			elif num == 2:
				self.aliens[i] = Alien(purplemodel, 'purple', hp=3)
			self.aliens[i].setPosition(x, 0, .5)
			x += .25
		
	def onKeyDown(self, key):
		if key == 'a' or key == viz.KEY_LEFT:
			self.leftUp = False
		
		if key == 'd' or key == viz.KEY_RIGHT:
			self.rightUp = False
			
		if key == "p":
			if self.pause:
				self.pause = False
			else:
				self.pause = True
			
		# Default Camera
		if key == '1':
			self.theta = 50
			mat = viz.Matrix()
			mat.postTrans(0, 0, -2)
			mat.postAxisAngle(1, 0, 0, self.theta)
			self.view.setMatrix(mat)
			
		# Top Down View
		if key == '2':
			self.theta = 90
			mat = viz.Matrix()
			mat.postAxisAngle(1, 0, 0, self.theta)
			mat.postTrans(0, 2, 0)
			self.view.setMatrix(mat)
			
		# Side View
		if key == '3':
			self.theta = 90
			mat = viz.Matrix()
			mat.postAxisAngle(0, 1, 0, self.theta)
			mat.postTrans(-1.5, 0, 0)
			self.view.setMatrix(mat)
			
		# Side View
		if key == '4':
			self.theta = 270
			mat = viz.Matrix()
			mat.postAxisAngle(0, 1, 0, self.theta)
			mat.postTrans(1.5, 0, 0)
			self.view.setMatrix(mat)
		
		if key == " " and self.Fire:
			b = Bullet('greenBullet.dae')
			b.setPosition(self.playerShip.getX()-.02,self.playerShip.getY()+.02,self.playerShip.getZ())
			self.bulletlist.append(b)
			self.Fire = False
			
	def onKeyUp(self, key):
		#Controls booleans for key presses, reactions are done by timers
		if key == "a" or key == viz.KEY_LEFT:
			self.leftUp = True
		if key == "d" or key == viz.KEY_RIGHT:
			self.rightUp = True
		if key == " ":
			self.fire = False
			
	def onTimer(self, num):
		if num == 1: # Moves the player left/right and controls the rotation of the ship
			if not self.leftUp and self.playerShip.canGoLeft(-0.25):
				self.playerShip.setPosition(self.playerShip.getX()-.025, self.playerShip.getY(), self.playerShip.getZ())
				if self.playerShip.theta < 45 or self.playerShip.theta >= 315:
					self.playerShip.rotate(9)
			if not self.rightUp and self.playerShip.canGoRight(0.25):
				self.playerShip.setPosition(self.playerShip.getX()+.025, self.playerShip.getY(), self.playerShip.getZ())
				if self.playerShip.theta > 315 and self.playerShip.theta <= 360 or self.playerShip.theta <= 45:
					self.playerShip.rotate(351)
		if num == 2: #Controls passive rotation for if the player is not actively pressing buttons
			if self.leftUp and self.rightUp:
				if self.playerShip.theta <= 45 and self.playerShip.theta >= 0:
					self.playerShip.rotate(351)
				if self.playerShip.theta >= 315:
					self.playerShip.rotate(9)
		
		if num == 3:
			#Move bullet
			for bullet in self.bulletlist:
				x = bullet.getX()
				vx = bullet.getVX()
				y = bullet.getY()
				vy = bullet.getVY()
				z = bullet.getZ()
				vz = bullet.getVZ()
				bullet.setPosition(x + vx, y + vy, z + vz)
				#Deallocate bullets
				if(bullet.getZ() > 2):
					bullet.delete()
					self.bulletlist.remove(bullet)
				# Check bullet to alien collison
				deadaliens = 0
				for alien in self.aliens:
					if alien != None:
						if bullet.getX() > alien.getX()-.1 and bullet.getX() < alien.getX()+.1 and bullet.getZ() > alien.getZ()-.1 and bullet.getZ() < alien.getZ()+.1:
							bullet.delete()
							self.bulletlist.remove(bullet)
							alien.damage()
							if alien.getHP() == 0:
								alien.delete()
								deadalien = self.aliens.index(alien)
								self.aliens[deadalien] = None
								deadaliens += 1
					else:
						deadaliens += 1
				if len(self.aliens) == deadaliens:
					self.power += 1
					self.speed = 1/self.power
					viz.killtimer(4)
					self.starttimer(4, self.speed, viz.FOREVER)
					self.spawnAliens()
							
							
			# TRANSLATE ALIEN BULLET
			for bullet in self.alienbullets:
				x = bullet.getX()
				vx = bullet.getVX()
				y = bullet.getY()
				vy = bullet.getVY()
				z = bullet.getZ()
				vz = bullet.getVZ()
				bullet.setPosition(x - vx, y - vy, z - vz)
				
				if(bullet.getZ() < -.8):
					bullet.delete()
					self.alienbullets.remove(bullet)
				if bullet.getX() > self.playerShip.getX()-.1 and bullet.getX() < self.playerShip.getX()+.1 and bullet.getZ() > self.playerShip.getZ()-.1 and bullet.getZ() < self.playerShip.getZ()+.1:
					bullet.delete()
					self.alienbullets.remove(bullet)
					self.playerShip.delete()
		
		
		if num == 4 and not self.pause:
			# Move aliens
			for alien in self.aliens:
				if alien != None:
					alien.setPosition(alien.getX(), alien.getY(), alien.getZ() - .001)
					if self.playerShip.getX()+.04 > alien.getX()-.1 and self.playerShip.getX()-.04 < alien.getX()+.1 and self.playerShip.getZ()+.06 > alien.getZ()-.1 and self.playerShip.getZ()-.06 < alien.getZ()+.1:
						self.playerShip.delete()
					if alien.isOffScreen():
						alien.setPosition(alien.getX(), alien.getY(), 1)
					
		
		if num == 5:
			for alien in self.aliens:
				if alien != None:
					if alien.getColor() == 'red': #Only red ships can fire
						index = self.aliens.index(alien) #Get the index of the current ship in our list
						#Checks for whether a ship exists in the two spots in front, False = No Ship, True = Ship Exists
						checkOne = False
						checkTwo = False
						if index < 6:
							if self.aliens[index+6] != None:
								checkOne = True
							if self.aliens[index+12] != None:
								checkTwo = True
						elif index < 12:
							if self.aliens[index+6] != None:
								checkOne = True
									# FIRES ALIEN BULLETS, THESE CHECKS ARE REQUIRED TO ALLOW A SHIP TO FIRE
						if not checkOne and not checkTwo and self.playerShip.getX() <= alien.getX()+.1 and self.playerShip.getX() >= alien.getX()-.1 and not self.pause:
							b = Bullet('redBullet.dae')
							b.setTheta(180)
							b.setPosition(alien.getX(), alien.getY(), alien.getZ())
							self.alienbullets.append(b)
			
		if num == 6:
			self.Fire = True
					
				
	def addCoordinateAxes(self):
		viz.startLayer(viz.LINES)
		viz.linewidth(7)
		viz.vertexColor( viz.RED )
		# positive y axis
		viz.vertex(0,0,0); 	   viz.vertex(0,20,0)
		#positive x axis
		viz.vertex(0,0,0); 	   viz.vertex(20,0,0)
		#positive z axis
		viz.vertex(0,0,0); 	   viz.vertex(0,0,20)
		#y=1 tick mark
		viz.vertex(-0.25,1,0); viz.vertex(0.25,1,0)
		#y=2 tick mark
		viz.vertex(-0.25,2,0); viz.vertex(0.25,2,0)
		#x=1 tick mark
		viz.vertex(1,0,-.25);  viz.vertex(1,0,.25)
		#x=2 tick mark
		viz.vertex(2,0,-.25);  viz.vertex(2,0,+.25)
		#z=1 tick mark
		viz.vertex(-.25,0,1);  viz.vertex(.25,0,1)
		#z=2 tick mark
		viz.vertex(-.25,0,2);  viz.vertex(.25,0,2)
		viz.endLayer()
				