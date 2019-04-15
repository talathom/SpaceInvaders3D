from Player import *
from Alien import *
from Bullet import *
import random
import math
import viz

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
		self.start = False #Checks whether the game has started
		
		self.title = True
		self.playerSpeed = .05
		
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
		self.level = 1
		self.speed = 1/self.power
		
		
		# Start timers
		
		self.starttimer(1, .05, viz.FOREVER)
		self.starttimer(2, .05, viz.FOREVER)
		self.starttimer(3, .001, viz.FOREVER)
		self.starttimer(4, self.speed, viz.FOREVER)
		self.starttimer(5, .5, viz.FOREVER)
		self.starttimer(6, .3, viz.FOREVER)
		
		#Initialize these models far off screen so they can be copied, thus these models only load once
		self.firstRed = Alien('red', modelLabel='redAlien.dae')
		self.firstRed.setPosition(0, 2000, 0)
		self.firstBlue = Alien('blue', modelLabel='blueAlien.dae')
		self.firstBlue.setPosition(0, 2000, 0)
		self.firstPurple = Alien('purple', modelLabel='tankAlien.dae')
		self.firstPurple.setPosition(0, 2000, 0)
		self.redbullet = Bullet(modelLabel='redBullet.dae')
		self.redbullet.setPosition(0, 2000, 0)
		self.greenbullet = Bullet(modelLabel='greenBullet.dae')
		self.greenbullet.setPosition(0, 2000, 0)
		self.firstOrange = Alien('orange', modelLabel = 'powerupAlien.dae')
		self.firstOrange.setPosition(0, 2000, 0)
		self.firstYellow = Alien('yellow', modelLabel = 'yellowAlien.dae')
		self.firstYellow.setPosition(0, 2000, 0)
		
		self.boss = None
		self.bossRight = False
		self.bossLeft = True
		
		self.levelText = None
		self.levelMsg = "Level: 1"
		self.hpText = None
		self.hpMsg = "HP: 1"
		self.scoreText = None
		self.scoreMsg = "Score: 0"
		self.score = 0
		
		self.titleScreen()
		
	def spawnAliens(self):
		# Spawns 3x6 aliens
		
		print("LEVEL: "+ str(self.power))
		if self.power % 6 == 0:
			self.boss = Alien('yellow', model=self.firstYellow.clone(), hp=self.power*6)
			self.boss.setPosition(0, 0, 1, scale=.0025*3)
			self.speed = 1/(self.power/2)
		else:
			x = -.6
			for i in range(0, 6):
				num = random.randint(0, 3)
				if num == 0:
					self.aliens[i] = Alien('blue', model=self.firstBlue.clone(), hp=3)
				elif num == 1:
					self.aliens[i] = Alien('red', model=self.firstRed.clone())
				elif num == 2:
					self.aliens[i] = Alien('purple', model=self.firstPurple.clone(), hp=3)
				elif num == 3:
					self.aliens[i] = Alien('orange', model=self.firstOrange.clone(), hp=2)
				self.aliens[i].setPosition(x, 0, 1)
				x += .25
			
			x = -.6
			for i in range(6, 12):
				num = random.randint(0, 3)
				if num == 0:
					self.aliens[i] = Alien('blue', model=self.firstBlue.clone(), hp=3)
				elif num == 1:
					self.aliens[i] = Alien('red', model=self.firstRed.clone())
				elif num == 2:
					self.aliens[i] = Alien('purple', model=self.firstPurple.clone(), hp=3)
				elif num == 3:
					self.aliens[i] = Alien('orange', model=self.firstOrange.clone(), hp=2)
				self.aliens[i].setPosition(x, 0, .75)
				x += .25
				
			x = -.6
			for i in range(12, 18):
				num = random.randint(0, 3)
				if num == 0:
					self.aliens[i] = Alien('blue', model=self.firstBlue.clone(), hp=3)
				elif num == 1:
					self.aliens[i] = Alien('red', model=self.firstRed.clone())
				elif num == 2:
					self.aliens[i] = Alien('purple', model=self.firstPurple.clone(), hp=3)
				elif num == 3:
					self.aliens[i] = Alien('orange', model=self.firstOrange.clone(), hp=2)
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
			b = Bullet(model=self.greenbullet.clone())
			b.setPosition(self.playerShip.getX()-.02,self.playerShip.getY()+.02,self.playerShip.getZ())
			self.bulletlist.append(b)
			self.Fire = False
		
		if key == 'q':
			self.title = False
			print (self.title)
			
		if key == viz.KEY_RETURN:
			if not self.start:
				self.start = True
				self.description.remove()
				self.spawnAliens()
				self.levelMsg = "Level: 1"
				self.levelText = viz.addText(self.levelMsg,viz.SCREEN,pos = [0,.9,0])
				self.hpText = viz.addText(self.hpMsg,viz.SCREEN,pos = [.3,.9,0])
				self.scoreText = viz.addText(self.scoreMsg,viz.SCREEN,pos = [.55,.9,0])
			
			
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
				self.playerShip.setPosition(self.playerShip.getX()-self.playerSpeed, self.playerShip.getY(), self.playerShip.getZ())
				if self.playerShip.theta < 45 or self.playerShip.theta >= 315:
					self.playerShip.rotate(9)
			if not self.rightUp and self.playerShip.canGoRight(0.25):
				self.playerShip.setPosition(self.playerShip.getX()+self.playerSpeed, self.playerShip.getY(), self.playerShip.getZ())
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
							if alien.getHP() <= 0:
								alien.delete()
								deadalien = self.aliens.index(alien)
								self.aliens[deadalien] = None
								deadaliens += 1
								if alien.getColor() == 'orange':
									self.playerShip.powerUp()
									self.updateHPText()
							self.score += 100
							self.updateScoreText()
							
					else:
						deadaliens += 1
				if self.boss != None:
					if bullet.getX() > self.boss.getX()-.3 and bullet.getX() < self.boss.getX()+.3 and bullet.getZ() > self.boss.getZ()-.3 and bullet.getZ() < self.boss.getZ()+.3:
							bullet.delete()
							self.bulletlist.remove(bullet)
							self.boss.damage()
							if self.boss.getHP() <= 0:
								self.boss.delete()
								self.boss = None
							self.score += 100
							self.updateScoreText()
				
				if len(self.aliens) == deadaliens and self.boss == None:
					self.power += 1
					self.level += 1
					self.updateLevelText()
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
					self.playerShip.damage(math.floor(self.power/2))
					if self.playerShip.getHP() <= 0:
						self.playerShip.delete()
					self.updateHPText()
		
		
		if num == 4 and not self.pause:
			# Move aliens
			for alien in self.aliens:
				if alien != None:
					alien.setPosition(alien.getX(), alien.getY(), alien.getZ() - .001, alien.getScale())
					if self.playerShip.getX()+.04 > alien.getX()-.1 and self.playerShip.getX()-.04 < alien.getX()+.1 and self.playerShip.getZ()+.06 > alien.getZ()-.1 and self.playerShip.getZ()-.06 < alien.getZ()+.1:
						self.playerShip.damage(1)
						if self.playerShip.getHP() <= 0:
							self.playerShip.delete()
						self.updateHPText()
					if alien.isOffScreen():
						alien.setPosition(alien.getX(), alien.getY(), 1, alien.getScale())
						
			if self.boss != None:
				if self.boss.getX() > -1 and self.bossLeft:
					self.boss.setPosition(self.boss.getX() - .001, self.boss.getY(), self.boss.getZ(), self.boss.getScale())
				else:
					self.bossLeft = False
				if self.boss.getX() < 1 and not self.bossLeft:
					self.boss.setPosition(self.boss.getX() + .001, self.boss.getY(), self.boss.getZ(), self.boss.getScale())
				else:
					self.bossLeft = True
				if self.playerShip.getX()+.04 > self.boss.getX()-.1 and self.playerShip.getX()-.04 < self.boss.getX()+.1 and self.playerShip.getZ()+.06 > self.boss.getZ()-.1 and self.playerShip.getZ()-.06 < self.boss.getZ()+.1:
					self.playerShip.damage(1)
					if self.playerShip.getHP() <= 0:
						self.playerShip.delete()
					self.updateHPText()
				if self.boss.isOffScreen():
					self.boss.setPosition(self.boss.getX(), self.boss.getY(), 1, self.boss.getScale())
		
		if num == 5:
			for alien in self.aliens:
				if alien != None:
					if alien.getColor() == 'red' or alien.getColor() == 'purple' or alien.getColor() == 'yellow': #Only red and purple ships can fire
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
							b = Bullet(model=self.redbullet.clone())
							b.setTheta(180)
							b.setPosition(alien.getX(), alien.getY(), alien.getZ())
							self.alienbullets.append(b)
							
			if self.boss != None:
				#if self.playerShip.getX() <= self.boss.getX()+.4 and self.playerShip.getX() >= self.boss.getX()-.4 and not self.pause:
				b = Bullet(model=self.redbullet.clone())
				b.setTheta(180)
				b.setPosition(self.boss.getX(), self.boss.getY(), self.boss.getZ(), 0)
				self.alienbullets.append(b)
				b = Bullet(model=self.redbullet.clone())
				b.setTheta(180)
				b.setVXVY(.02, 0, .02)
				b.setPosition(self.boss.getX(), self.boss.getY(), self.boss.getZ())
				self.alienbullets.append(b)
				b = Bullet(model=self.redbullet.clone())
				b.setTheta(180)
				b.setVXVY(-.02, 0, .02)
				b.setPosition(self.boss.getX(), self.boss.getY(), self.boss.getZ(), 90)
				self.alienbullets.append(b)
				
			
		if num == 6:
			self.Fire = True
			
	def updateHPText(self):
		self.hpMsg = "HP: "+ str(int(self.playerShip.getHP()))
		self.hpText.remove()
		self.hpText = viz.addText(self.hpMsg,viz.SCREEN,pos = [.3,.9,0])
		
	def updateLevelText(self):
		self.levelText.remove()
		self.levelMsg = "Level: "+ str(self.level)
		self.levelText = viz.addText(self.levelMsg ,viz.SCREEN,pos = [0,.9,0])
		
	def updateScoreText(self):
		self.scoreText.remove()
		self.scoreMsg = "Score: "+ str(self.score)
		self.scoreText = viz.addText(self.scoreMsg,viz.SCREEN,pos = [.55,.9,0])
		
	def titleScreen(self):
		 
		
#		self.text = viz.addText3D('Alien Invasion')
#		self.text.font('impact')
#		mat = viz.Matrix()
#		mat.postScale(.1,.1,.1) 
#		mat.postAxisAngle(1, 0, 0, self.theta)
#		mat.postTrans(-.28, .4, .1)
#		self.text.setMatrix(mat)
		
		self.description = viz.addText3D('Make a last stand against an endless alien attack \n\n'
										 +'Use the A and D keys or left and right keys to move ship and the spacebar to fire \n\n'
										 +'There are 5 different types of aliens, Red: Shoots back at player, Blue: Tank takes 3 hits to kill \n\n'
										 +'Purple: Has both the Blue and Red alien abilities\n\n' 
										 +'Orange: Gives players an extra hitpoint when hit,\n Green: Boss alien which will be a challenge to defeat\n\n'
										 +'Press enter when you are ready to begin!')
										
										
		self.description.font('Comic Sans MS')
		self.description.alignment(viz.ALIGN_CENTER)
		mat = viz.Matrix()
		mat.postScale(.05,.05,.05) 
		mat.postAxisAngle(1, 0, 0, self.theta)
		mat.postTrans(0, .4, -.1)
		self.description.setMatrix(mat)
		
				
	