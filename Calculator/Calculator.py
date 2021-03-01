from Calculator.Subtract import subtract
from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.multiply import multiply



class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtract(a, b)
        return self.result


    def multiply(self, x, y):
        self.result = multiply(x, y)
        return self.result

    def divide(self, x, y):
        self.result = round(division (x, y), 9)
        return self.result

