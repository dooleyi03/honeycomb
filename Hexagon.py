"""

    @ Author: Dr. Romas James Hada

"""
import turtle as t
from Shape import Shape


class Hexagon(Shape):
    def __init__(self, _xCor=0, _yCor=0, _size=50,
                 _fillColor='black', _borderColor='red', _borderThickness=3,
                 _nameOfShape='Hexagon'):
        super().__init__(_xCor, _yCor, _fillColor, _borderColor, _borderThickness, _nameOfShape)
        self.size = _size

    def setSize(self, newSize):
        self.size = newSize

    def getSize(self):
        return self.size

    def draw(self):
        numSides = 6
        t.pencolor(self.borderColor)
        t.pensize(self.borderThickness)

        t.pendown()
        # Your Code Stars Here
        for i in range(numSides):
            t.forward(self.size)
            t.right(60)
        t.penup()

    def drawWithColor(self):
        t.fillcolor(self.fillColor)
        t.begin_fill()
        self.draw()
        t.end_fill()


if __name__ == '__main__':
    # Testing
    myHexagon = Hexagon(_nameOfShape='This is my Hexagon.')
    myHexagon.draw()
    myHexagon.setXCor(-200)
    myHexagon.moveTurtle()
    myHexagon.drawWithColor()
    print(myHexagon.getName())
