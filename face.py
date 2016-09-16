from graphics import *


def main():
    win = GraphWin('Face', 800, 650) # give title and dimensions
    #win.yUp() # make right side up coordinates!
    for x in range(0,600,5):
        pt = Point(600-x,x)
        pt.setFill("red")
        pt.draw(win)


    win.getMouse()
    win.close()

main()