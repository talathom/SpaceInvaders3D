import viz
import vizcam
from Controller import *

# set size (in pixels) and title of application window
viz.window.setSize( 640, 480 )
viz.window.setName( "Space Invaders 3D" )

# get graphics window
window = viz.MainWindow
# setup viewing volume

# set background color of window to blue 
viz.MainWindow.clearcolor( [0,0,0] ) 

c = Controller()
pivotNav = vizcam.PivotNavigate()

# render the scene in the window
viz.go()

