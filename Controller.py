from Player import *
from RammerAlien import *
from Bullet import *
import copy

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
		self.aliens = list()
		
		# Default rotation for camera
		self.theta = 50
		
		#Booleans for keys pressed
		self.leftUp = True
		self.rightUp = True
		self.Fire = False
		self.start = False
		
		#Setup default camera view
		self.view = viz.MainView
		mat = viz.Matrix()
		mat.postAxisAngle(1, 0, 0, self.theta)
		mat.postTrans(0, 0, 0)
		self.view.setMatrix(mat)
		
		#Spawn the player
		self.playerShip = Player()
		self.playerShip.setPosition(0, 0, -.6)
		
		# Start timers
		self.starttimer(1, .05, viz.FOREVER)
		self.starttimer(2, .05, viz.FOREVER)
		self.starttimer(3, .001, viz.FOREVER)
		self.starttimer(4, .5, viz.FOREVER) #Controls aliens
		self.addCoordinateAxes()
		self.spawnAliens()
		
	def spawnAliens(self):
		# Spawns 3x6 aliens
		x = -.6
		for i in range(0, 6):
			self.aliens.append(Alien())
			self.aliens[i].setPosition(x, 0, 1)
			x += .25
		
		x = -.6
		for i in range(6, 12):
			self.aliens.append(Alien())
			self.aliens[i].setPosition(x, 0, .75)
			x += .25
		x = -.6
		for i in range(12, 18):
			self.aliens.append(Alien())
			self.aliens[i].setPosition(x, 0, .5)
			x += .25		
		
	def onKeyDown(self, key):
		if key == 'a' or key == viz.KEY_LEFT:
			self.leftUp = False
		
		if key == 'd' or key == viz.KEY_RIGHT:
			self.rightUp = False
			
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
			
		if key == '0':
			self.start = True
		
		if key == " ":
			b = Bullet()
			b.setPosition(self.playerShip.getX(),self.playerShip.getY(),self.playerShip.getZ())
			self.bulletlist.append(b)
			
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
			for bullet in self.bulletlist:
				x = bullet.getX()
				vx = bullet.getVX()
				y = bullet.getY()
				vy = bullet.getVY()
				z = bullet.getZ()
				vz = bullet.getVZ()
				bullet.setPosition(x + vx, y + vy, z + vz)
				if(bullet.getZ() > 2):
					bullet.delete()
					self.bulletlist.remove(bullet)
					
				
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
				