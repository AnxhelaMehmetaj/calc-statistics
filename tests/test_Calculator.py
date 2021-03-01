import unittest

from Calculator.Calculator import Calculator
from CVS_Reader.Reader import Reader


class CalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_addition(self):
        file = Reader("testCases/Addition.csv").content
        print("TEST ADDITION\n")
        for row in file:
            result = float(row[2])
            self.assertEqual(self.calculator.add(row[0], row[1]), float(row[2]))
            self.assertEqual(self.calculator.result, result)


    def test_subtraction(self):
        file = Reader("testCases/Subtraction.csv").content
        print("TESTING SUBTRACTION\n")
        for row in file:
            self.assertEqual(self.calculator.subtract(row[0], row[1]), float(row[2]))


