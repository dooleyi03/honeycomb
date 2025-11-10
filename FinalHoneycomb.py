import turtle as t

from HoneyComb import HoneyComb

"""
1. You should complete all the python files, upload correct and complete python files (*.py) 
    and the screenshots of the outputs that consists shape(s) similar to the ones shown 
    in the sample output(s) (40 Points).
2. Title of your turtle screen should consist your full name (10 Points).
3. Your drawings should match the one attached herewith (50 Points).
4. Total number of files expected on D2L: at least 6 files
    (5 Python files and at least 1 screenshot of the Turtle screen, 50 Points).
5. You must complete Hexagon class and HoneyComb class. Please do not modify this file
    unless you want to add solution to the bonus problem (50 Points).
6. Your code must comply with DRY principle and use OOP approach (50 Points).
7. You must give meaningful names to classes, files, functions, variables, etc. (50 Points).
"""


def start():
    t.speed('fastest')
    t.title('Exam II - Isabel Dooley - Honey Combs')
    t.shape('turtle')
    myScreen = t.Screen()
    myScreen.setup(width=1.0, height=1.0)
    maxScreenWidth = myScreen.window_width()
    maxScreenHeight = myScreen.window_height()

    startXCor = -maxScreenHeight / 2
    startYCor = maxScreenHeight / 5

    # Your Code Starts Here
    honeyCombUnitSize = 50

    myHoneyComb = HoneyComb(xCor=startXCor, yCor=startYCor, unitSize=honeyCombUnitSize)
    myHoneyComb.moveTurtle()
    myHoneyComb.drawWithColor()

    t.forward(6 * myHoneyComb.getUnitSize())
    myHoneyComb.draw()

    # Bonus
    #for i in range(5):
     #   myHoneyComb.drawWithColor()
      #  t.forward(honeyCombUnitSize * 3)





if __name__ == '__main__':
    start()
    t.hideturtle()
    t.mainloop()
