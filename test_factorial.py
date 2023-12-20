import unittest
from factorial import factorial

class TestFactorialFunction(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_of_negative_number(self):
        try:
            factorial(-5)
        except ValueError as e:
            self.assertEqual(str(e), "Факторіал визначений тільки для невід'ємних чисел.")
        else:
            self.fail("Помилок не знайдено")

if __name__ == '__main__':
    unittest.main()