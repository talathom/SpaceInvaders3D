import viz
import vizshape
import vizcam
import math

# An instance of this class reads a model in from
# adds a file and adds it to the scene.  It keeps
# track of the models x,y,z location, scale, and
# rotation.
# 
class Model():

	# Constructor 
	def __init__(self, filename):
		# read model data from file and add to scene graph 
		self.node = viz.add(filename)
		# model's location in world
		self.x = 0
		self.y = 0
		self.z = 0
		# model's scale
		self.s = 1
		# model's rotation about the Y axis (in degrees)
		self.yrot = 0
		self.zrot = 0
		self.xrot = 0
		self.setTransMatrix()

	# setter for location of the model	
	def setLocation(self, x, y, z ):
		self.x = x
		self.y = y
		self.z = z
		self.setTransMatrix()
	
	# getters for the coordinates of the model's location
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def getZ(self):
		return self.z
		
	# setter and getter for the model's (uniform) scale
	def setScale(self, s ):
		self.s = s
		self.setTransMatrix()
	def getScale(self):
		return self.s
		
	# setter and getter for the model's rotation about Y axis
	# in degrees
	def setYRotation(self, yrot ):
		self.yrot = yrot
		self.setTransMatrix()
		
	def getYRotation(self):
		return self.yrot
		
	def setZRotation(self, zrot):
		self.zrot += zrot
		self.setTransMatrix()
		
	def getZRotation(self):
		return self.zrot
		
	def setXRotation(self, xrot):
		self.xrot += xrot
		self.setTransMatrix()
		
	def getXRotation(self):
		return self.xrot	
		
	# get the model's scene graph node
	def getNode(self):
		return self.node
		
	def remove(self):
		self.node.remove()
		
	# set model's x,y,z, scale and rotation
	def setOrientation(self,x,y,z,s,yrot,zrot,xrot):
		self.x = x
		self.y = y
		self.z = z
		self.s = s
		self.yrot = yrot
		self.zrot = zrot
		self.xrot = xrot
		self.setTransMatrix()
		
	def setTransMatrix(self):
		mat = viz.Matrix()
		mat.postScale(self.s,self.s,self.s)
		mat.postAxisAngle(0,1,0, self.yrot)
		mat.postAxisAngle(0,0,1, self.zrot)
		mat.postAxisAngle(1,0,0, self.xrot)
		mat.postTrans(self.x,self.y,self.z)
		self.node.setMatrix( mat )