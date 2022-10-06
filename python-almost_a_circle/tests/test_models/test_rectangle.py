import unittest
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    def test_rectangle_assignments(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r4 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, 3, "4")
        r4 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)
            r1 = Rectangle(1, -2)
            r1 = Rectangle(0, 2)
            r1 = Rectangle(1, 0)
            r1 = Rectangle(1, 2, -3)
            r1 = Rectangle(1, 2, 3 ,-4)
    def test_rectangle_methods(self):
        pass
