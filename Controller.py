﻿from Player import *

class Controller (viz.EventClass):

	# Constructor 
	def __init__(self):
		# base class constructor 
		viz.EventClass.__init__(self)
		
		self.callback(viz.KEYDOWN_EVENT, self.onKeyDown) # Callback for key press
		self.callback(viz.TIMER_EVENT, self.onTimer) # Callback for timers
		self.callback(viz.KEYUP_EVENT, self.onKeyUp)
		
		self.leftUp = True
		self.rightUp = True
		self.Fire = False
		
		view = viz.MainView
		mat = viz.Matrix()
		mat.postAxisAngle(1, 0, 0, 50)
		mat.postTrans(0, 0, 0)
		view.setMatrix(mat)
		self.playerShip = Player()
		self.playerShip.setPosition(0, 0, -.6)
		self.starttimer(1, .05, viz.FOREVER)
		self.starttimer(2, .05, viz.FOREVER)
		self.addCoordinateAxes()
		
	def onKeyDown(self, key):
		if key == 'a' or key == viz.KEY_LEFT:
			self.leftUp = False
		
		if key == 'd' or key == viz.KEY_RIGHT:
			self.rightUp = False
			
	def onKeyUp(self, key):
		if key == "a" or key == viz.KEY_LEFT:
			self.leftUp = True
		if key == "d" or key == viz.KEY_RIGHT:
			self.rightUp = True
		if key == " ":
			self.fire = False
			
	def onTimer(self, num):
		if num == 1:
			print(str(self.playerShip.theta))
			if not self.leftUp:
				self.playerShip.setPosition(self.playerShip.getX()-.025, self.playerShip.getY(), self.playerShip.getZ())
				if self.playerShip.theta < 45:
					self.playerShip.rotate(9)
			if not self.rightUp:
				self.playerShip.setPosition(self.playerShip.getX()+.025, self.playerShip.getY(), self.playerShip.getZ())
				if self.playerShip.theta > 315 and self.playerShip.theta <= 360 or self.playerShip.theta  == 0 :
					self.playerShip.rotate(351)
		if num == 2:
			if self.leftUp and self.rightUp:
				if self.playerShip.theta <= 45 and self.playerShip.theta >= 0:
					self.playerShip.rotate(351)
				if self.playerShip.theta >= 315:
					self.playerShip.rotate(9)
				
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
				