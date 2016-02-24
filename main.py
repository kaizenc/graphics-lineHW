from display import *
from draw import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]

for x in range(500):
	if (x % 6) == 0:
		draw_line( screen, 0, 250, x, int(-100*math.sin(math.radians(x))) + 250, color )
	if x > 180:
		color = [255, 0, 0]
	if x > 360:
		color = [0, 0, 255]

display(screen)