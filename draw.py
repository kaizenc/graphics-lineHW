from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    #Makes sure lines go from left to right
    if x1 < x0:
        x0, x1 = x1, x0
        y0, y1 = y1, y0 
    if (y1 >= y0): #if positive slope
        dx = x1 - x0
        dy = y1 - y0
        if y1 - y0 > x1 - x0: #if slope > 1
            k = (dx * 2) - dy
            x = x0
            for y in range (y0, y1 + 1):
                if (k < 0):
                    k += (dx * 2)
                    plot(screen, color, x, y)
                else:
                    k += 2 * (dx - dy)
                    x += 1
                    plot(screen, color, x, y)
        else: #if slope <= 1
            k = (dy * 2) - dx
            y = y0
            for x in range (x0, x1 + 1):
                if (k < 0):
                    k += (dy * 2)
                    plot(screen, color, x, y)
                else:
                    k += 2 * (dy - dx)
                    y += 1
                    plot(screen, color, x, y)
    else: #negative slope
        y0, y1 = -1*y0, -1*y1
        dx = x1 - x0
        dy = y1 - y0
        if y0 - y1 > x1 - x0: #if slope > -1
            k = (dx * 2) - dy
            x = x0
            for y in range (y0, y1 + 1):
                if (k < 0):
                    k += (dx * 2)
                    plot(screen, color, x, -1*y)
                else:
                    k += 2 * (dx - dy)
                    x += 1
                    plot(screen, color, x, -1*y)
        else: #if slope < -1
            k = (dy * 2) - dx
            y = y0
            for x in range (x0, x1 + 1):
                if (k < 0):
                    k += dy * 2
                    plot(screen, color, x, -1*y)
                else:
                    k += 2 * (dy - dx)
                    y += 1
                    plot(screen, color, x, -1*y)
    save_ppm( screen, "Test1.ppm" )
