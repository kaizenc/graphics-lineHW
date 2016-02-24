from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    #Makes sure lines go from left to right
    if x1 < x0:
        x0, x1 = x1, x0
        y0, y1 = y1, y0 
        
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1

    if y1 > y0:
        d = 2 * A + B
        if -1 * B > A:
            while x < x1:  # Octant 1 / 5
                plot(screen, color, x, y)
                if d > 0:
                    y += 1
                    d += 2 * B
                x += 1
                d += 2 * A
        else:
            while y < y1:  # Octant 2 / 6
                plot(screen, color, x, y)
                if d < 0:
                    x += 1
                    d += 2 * A
                y += 1
                d += 2 * B
    else:
        d = 2 * A - B
        if A > B:
            while x < x1:  # Octant 4 / 8
                plot(screen, color, x, y)
                if d < 0:
                    y -= 1
                    d -= 2 * B
                x += 1
                d += 2 * A
        else:
            while y > y1:  # Octant 3 / 7
                plot(screen, color, x, y)
                if d > 0:
                    x += 1
                    d += 2 * A
                y -= 1
                d -= 2 * B
