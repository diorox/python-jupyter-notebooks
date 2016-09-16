from graphics import *


def main():
    win = GraphWin('Face', 800, 450) # give title and dimensions
    #win.yUp() # make right side up coordinates!
    for x in range(0,600,5):
        pt = Point(x,x)
        pt.setFill("red")
        pt.draw(win)

    for x in range(600,0,-5):
        pt = Point(600+x,x)
        pt.setFill("blue")
        pt.draw(win)

    win.getMouse()
    win.close()

main()