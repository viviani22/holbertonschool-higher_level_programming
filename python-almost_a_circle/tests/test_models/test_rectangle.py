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
        self.assertEqual(r4.id, 5)
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3 ,-4)
    def test_rectangle_area(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.area(), 1)
    def test_rectangle_str(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/1 - 1/1")
    def test_rectangle_display(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.display(), None)
        r2 = Rectangle(1, 1, 1)
        self.assertEqual(r2.display(), None)
        r3 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r3.display(), None)
