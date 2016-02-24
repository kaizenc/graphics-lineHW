from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
	#Makes sure lines go from left to right
	if x1 < x0:
        x0, x1 = x1, x0
        y0, y1 = y1, y0 
    if (y1 >= y0): #if positive slope
        if y1 - y0 > x1 - x0: #if slope > 1
            dx = x1 - x0
            dy = y1 - y0
            dxTimes2 = dx * 2
            dxTimes2MinusdyTimes2 = 2 * (dx - dy)
            k = (dx * 2) - dy
            x = x0
            for y in range (y0, y1 + 1):
                if (k < 0):
                    k += dxTimes2
                    plot(screen, color, x, y)
                else:
                    k += dxTimes2MinusdyTimes2
                    x += 1
                    plot(screen, color, x, y)
        else: #if slope <= 1
            dx = x1 - x0
            dy = y1 - y0
            dyTimes2 = dy * 2
            dyTimes2MinusdxTimes2 = 2 * (dy - dx)
            k = (dy * 2) - dx
            y = y0
            for x in range (x0, x1 + 1):
                if (k < 0):
                    k += dyTimes2
                    plot(screen, color, x, y)
                else:
                    k += dyTimes2MinusdxTimes2
                    y += 1
                    plot(screen, color, x, y)
    else: #negative slope
        if y0 - y1 > x1 - x0: #if slope > -1
            y0, y1 = -1*y0, -1*y1
            dx = x1 - x0
            dy = y1 - y0
            dxTimes2 = dx * 2
            dxTimes2MinusdyTimes2 = 2 * (dx - dy)
            k = (dx * 2) - dy
            x = x0
            for y in range (y0, y1 + 1):
                if (k < 0):
                    k += dxTimes2
                    plot(screen, color, x, -1*y)
                else:
                    k += dxTimes2MinusdyTimes2
                    x += 1
                    plot(screen, color, x, -1*y)
        else: #if slope < -1
            y0, y1 = -1*y0, -1*y1
            dx = x1 - x0
            dy = y1 - y0
            dyTimes2 = dy * 2
            dyTimes2MinusdxTimes2 = 2 * (dy - dx)
            k = (dy * 2) - dx
            y = y0
            for x in range (x0, x1 + 1):
                if (k < 0):
                    k += dyTimes2
                    plot(screen, color, x, -1*y)
                else:
                    k += dyTimes2MinusdxTimes2
                    y += 1
                    plot(screen, color, x, -1*y)
    save_ppm( screen, "Test1.ppm" )
