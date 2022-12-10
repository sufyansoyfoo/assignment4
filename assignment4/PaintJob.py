import math

class PaintJob:

    def __init__(self, height, width, length, canPrice, budget):
        # instance fields found by C++ to Python Converter:

        self.height = height
        self.width = width
        self.length = length
        self.canPrice = canPrice
        self.budget = budget

        self.area = 2.0 * ((self.height * self.width) + (self.width * self.length))


budget = int(input("Enter your budget: "))
height = int(input("Enter wall height (feet): "))
width = int(input("Enter wall width (feet): "))
length = int(input("Enter wall length (feet): "))
canPrice = int(input("Enter the price of a can of paint: "))

newPaintJob = PaintJob(height, width, height, length, budget)

area = newPaintJob.area

print("Wall area:", area, "ft^2")

for i in range(1, 4):

    paintNeeded = area * i / 100.0
    print("Amount of paint needed: {0:.2f} L\n".format(paintNeeded), end = '')

    numCans = math.ceil(paintNeeded / 3.7)
    print("Number of paint cans needed: {0} cans\n".format(numCans), end='')

    coatPrice = numCans * canPrice
    print("The price of {0} coat(s) of paint: {1} $\n".format(i, coatPrice, end=''))

    print("The amount of money left from the budget after {0} coat(s) of paint: {1} $\n".format(i, (budget - coatPrice)))








