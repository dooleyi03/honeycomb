import random

from Exams.Hexagon import Hexagon
from Shape import Shape
import turtle as t


class HoneyComb(Shape):
    def __init__(self, unitSize=50, xCor=0, yCor=0,
                 fillColor='yellow', borderColor='black',
                 borderThickness=5, nameOfShape='Honey Comb'):
        super().__init__(xCor, yCor, fillColor, borderColor, borderThickness, nameOfShape)
        self.unitSize = unitSize

    def setUnitSize(self, newSize):
        self.unitSize = newSize

    def getUnitSize(self):
        return self.unitSize

    def draw(self):
        partOfHoneyComb = Hexagon(_borderColor=self.borderColor,
                                  _size=self.unitSize, _borderThickness=self.borderThickness)

        # Your Code Starts Here
        for i in range(6):
            partOfHoneyComb.draw()
            t.forward(self.unitSize)
            t.left(60)

    def drawWithColor(self):
        t.fillcolor(self.fillColor)
        t.pencolor(self.borderColor)
        t.pensize(self.borderThickness)
        t.begin_fill()
        self.draw()
        t.end_fill()


if __name__ == '__main__':
    t.speed('normal')
    testObject = HoneyComb(fillColor='yellow')
    testObject.drawWithColor()

    # t.hideturtle()
    t.mainloop()
