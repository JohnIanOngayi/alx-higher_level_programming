#!/usr/bin/python3
"""

Test Cases for models.base
This module utilises the unittest model to test models.base

"""
import unittest
from models.rectangle import Rectangle
import json
import csv


class TestSquare(unittest.TestCase):

    def setUp(self):
        self.rect = Rectangle(5, 10, 2, 3, 1)

    def test_Rectangle_attr(self):
        a = Rectangle(1, 1)
        self.assertEqual(a.width, 1)
        self.assertEqual(a.height, 1)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        b = Rectangle(5, 10, 5, 25, 456)
        self.assertEqual(b.id, 456)
        self.assertEqual(b.area(), 50)

    def test_Rectangle_setters(self):
        with self.assertRaises(ValueError):
            b = Rectangle(5, 0, 5, 25, 456)
        with self.assertRaises(ValueError):
            b = Rectangle(0, 5, 8, 25, 456)
        with self.assertRaises(ValueError):
            b = Rectangle(5, 0, -5, 25, 456)
        with self.assertRaises(ValueError):
            b = Rectangle(5, 10, 5, -5, 456)

        with self.assertRaises(TypeError):
            b = Rectangle(0.5, 10, 5)
        with self.assertRaises(TypeError):
            b = Rectangle(4, 0.5, 8)
        with self.assertRaises(TypeError):
            b = Rectangle(5, 10, 0.5)
        with self.assertRaises(TypeError):
            b = Rectangle('ob', 10, 5)
        with self.assertRaises(TypeError):
            b = Rectangle(4, 'atu', 8)
        with self.assertRaises(TypeError):
            b = Rectangle(5, 10, [5, 3, 7])

    def test_str_representation(self):
        self.assertEqual(str(self.rect), "[Rectangle] (1) 2/3 - 5/10")

    def test_to_dictionary_method(self):
        rect_dict = self.rect.to_dictionary()
        expected = {'x': 2, 'y': 3, 'id': 1, 'height': 10, 'width': 5}
        self.assertEqual(rect_dict, expected)

    def test_update_method_with_args(self):
        self.rect.update(2, 7, 14, 4, 6)
        self.assertEqual(self.rect.id, 2)
        self.assertEqual(self.rect.width, 7)
        self.assertEqual(self.rect.height, 14)
        self.assertEqual(self.rect.x, 4)
        self.assertEqual(self.rect.y, 6)

    def test_update_method_with_kwargs(self):
        updater = {'width': 8, 'height': 16, 'x': 3, 'y': 5, 'id': 3}
        self.rect.update(**updater)
        self.assertEqual(self.rect.id, 3)
        self.assertEqual(self.rect.width, 8)
        self.assertEqual(self.rect.height, 16)
        self.assertEqual(self.rect.x, 3)
        self.assertEqual(self.rect.y, 5)


if __name__ == '__main__':
    unittest.main()
