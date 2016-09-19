from graphics import *
import math
import random

def main():
    win = GraphWin('Face', 100,100) # give title and dimensions
    #win.yUp() # make right side up coordinates!
    trials = 10000
    c = math.sqrt(3)/2;
    print('c = ',c)
    cx = [0.0, 1.0, 0.5]
    cy = [0.0, 0.0, c]
    x=0
    y=0


    for x in range(0,trials):
        r = random.randint(0,2)
        x = (((x + cx[r])/2.0))
        y = (((y + cy[r])/2.0)) 
        pt = Point(x,y)

        print('r='+ str(r) + ' [x='+ str(x) + ', y=' + str(y) + ']')
        pt.setFill("red")
        pt.draw(win)


    win.getMouse()
    win.close()

main()