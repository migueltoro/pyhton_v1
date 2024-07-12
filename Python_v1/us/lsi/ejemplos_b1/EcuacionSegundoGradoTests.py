'''
Created on 6 jul 2024

@author: migueltoro
'''

import unittest
import pytest
from us.lsi.ejemplos_b1.Ejemplos_b1 import sol_ecuacion_segundo_grado

class SolEcuacionSegundoGradoTests(unittest.TestCase):
    def test_real_roots(self):
        roots = sol_ecuacion_segundo_grado(1, -3, 2)
        self.assertEqual(roots, (2.0, 1.0))

    def test_complex_roots(self):
        roots = sol_ecuacion_segundo_grado(1, 2, 5)
        self.assertEqual(roots, (complex(-1, 2), complex(-1, -2)))

    def test_zero_discriminant(self):
        roots = sol_ecuacion_segundo_grado(1, -2, 1)
        self.assertEqual(roots, (1.0, 1.0))

    def test_negative_a(self):
        with self.assertRaises(ValueError):
            sol_ecuacion_segundo_grado(-1, 2, 1)

if __name__ == '__main__':
    pytest.main()