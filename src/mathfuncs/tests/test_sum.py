import unittest
from mathfuncs.sum import sum


class TestSum(unittest.TestCase):
    def test_sum(self):
        resultado = sum(2, 3)
        self.assertEqual(resultado, 5)

    def test_sum_error(self):
        with self.assertRaises(TypeError):
            sum(2, "3")
