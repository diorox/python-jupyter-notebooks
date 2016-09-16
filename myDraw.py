from graphics import *


def main():
    win = GraphWin('Face', 400, 400) # give title and dimensions
    #win.yUp() # make right side up coordinates!

    head = Circle(Point(40,100), 25) # set center and radius
    head.setFill("yellow")
    head.draw(win)

    win.getMouse()
    win.close()

main()