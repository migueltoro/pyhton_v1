'''
Created on 7 jul 2024

@author: migueltoro
'''

import unittest
import pytest
from fractions import Fraction
from us.lsi.ejemplos_b2.Ejemplos_genericos import PolinomioF

class TestPolinomio2(unittest.TestCase):

    def test_polinomio_addition(self):
        p1 = PolinomioF.of(Fraction(1,1), Fraction(2,1))
        p2 = PolinomioF.of(Fraction(3,1), Fraction(4,1))
        result = p1 + p2
        expected = PolinomioF.of(Fraction(4,1), Fraction(6,1))
        self.assertEqual(result, expected)

    def test_polinomio_subtraction(self):
        p1 = PolinomioF.of(Fraction(1,1), Fraction(2,1))
        p2 = PolinomioF.of(Fraction(3,1), Fraction(4,1))
        result = p1 - p2
        expected = PolinomioF.of(Fraction(-2,1), Fraction(-2,1))
        self.assertEqual(result, expected)

    def test_polinomio_multiplication(self):
        p1 = PolinomioF.of(Fraction(1,1), Fraction(2,1))
        p2 = PolinomioF.of(Fraction(3,1), Fraction(4,1))
        result = p1 * p2
        expected = PolinomioF.of(Fraction(3,1), Fraction(10,1), Fraction(8,1))
        self.assertEqual(result, expected)

    def test_polinomio_power(self):
        p1 = PolinomioF.of(Fraction(1,1), Fraction(2,1))
        result = p1 ** 2
        expected = PolinomioF.of(Fraction(1,1), Fraction(4,1), Fraction(4,1))
        self.assertEqual(result, expected)

    def test_polinomio_derivative(self):
        p1 = PolinomioF.of(Fraction(1,1), Fraction(2,1), Fraction(3,1))
        result = p1.derivada
        expected = PolinomioF.of(Fraction(2,1), Fraction(6,1))
        self.assertEqual(result, expected)

    def test_polinomio_integral(self):
        p1 = PolinomioF.of(Fraction(1,1), Fraction(2,1), Fraction(3,1))
        result = p1.integral()
        expected = PolinomioF.of(Fraction(0,1), Fraction(1,1), Fraction(1,1), Fraction(1,1))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    pytest.main()