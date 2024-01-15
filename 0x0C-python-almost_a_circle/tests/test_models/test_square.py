#!/usr/bin/python3
"""

Test Cases for models.base
This module utilises the unittest model to test models.base

"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_Square_attr(self):
        a = Square(1)
        self.assertEqual(a.size, 1)
        b = Square(5, 0, 5)
        self.assertEqual(b.x, 0)
        c = Square(7, 45)
        self.assertEqual(c.y, 0)
        self.assertEqual(c.area(), 49)
        self.assertIsInstance(c, Square)

    def test_Square_setters(self):
        with self.assertRaises(ValueError):
            b = Square(0, 0, 5)
        with self.assertRaises(ValueError):
            b = Square(-4, 5, 8)
        with self.assertRaises(ValueError):
            b = Square(5, 0, -5)
        with self.assertRaises(ValueError):
            b = Square(5, -5, 5)

        with self.assertRaises(TypeError):
            b = Square(0.5, 0, 5)
        with self.assertRaises(TypeError):
            b = Square(4, 0.5, 8)
        with self.assertRaises(TypeError):
            b = Square(5, 0, 0.5)
        with self.assertRaises(TypeError):
            b = Square('ob', 0, 5)
        with self.assertRaises(TypeError):
            b = Square(4, 'atu', 8)
        with self.assertRaises(TypeError):
            b = Square(5, 0, [5, 3, 7])

    def test_str_representation(self):
        a = Square(1, 5, 2)
        self.assertEqual(str(a), '[Square] (8) 5/2 - 1')


if __name__ == "__main__":
    unittest.main()
