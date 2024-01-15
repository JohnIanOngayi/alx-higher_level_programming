#!/usr/bin/python3
"""

Test Cases for models.base
This module utilises the unittest model to test models.base

"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_Base_id(self):
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        c = Base()
        self.assertEqual(c.id, 3)
        d = Base(89)
        self.assertEqual(d.id, 89)
        e = Base(0)
        self.assertEqual(e.id, 0)
        f = Base(-25)
        self.assertEqual(f.id, -25)


if __name__ == "__main__":
    unittest.main()
