import unittest
from models.rectangle import Rectangle
import os.path
import io 
import sys

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
        r1 = Rectangle(1, 1, 1, 1)
        output = io.StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n #\n")
        r2 = Rectangle(1, 1, 1)
        output = io.StringIO()
        sys.stdout = output
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), " #\n")
        r3 = Rectangle(1, 1)
        output = io.StringIO()
        sys.stdout = output
        r3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "#\n")
    def test_rectangle_to_dictionary(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(r1.to_dictionary(), {'x': 1, 'y': 1, 'id': 1, 'height': 1, 'width': 1})
    def test_rectangle_update(self):
        r1 = Rectangle(1, 1)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 1)
        self.assertEqual(r1.width, 1)
        r1.update(89, 1, 2)
        self.assertEqual(r1.height, 2)
        r1.update(89, 1, 2, 3)
        self.assertEqual(r1.x, 3)
        r1.update(89, 1, 2, 3, 4)
        self.assertEqual(r1.y, 4)
        r2 = Rectangle(1, 1)
        r2.update(**{ 'id': 89 })
        self.assertEqual(r2.id, 89)
        r2.update(**{ 'id': 89, 'width': 1 })
        self.assertEqual(r2.width, 1)
        r2.update(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(r2.height, 2)
        r2.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(r2.x, 3)
        r2.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(r2.y, 4)
    def test_rectangle_create(self):
        r1 = Rectangle.create(**{ 'id': 89 })
        self.assertEqual(r1.id, 89)
        r1 = Rectangle.create(**{ 'id': 89, 'width': 1 })
        self.assertEqual(r1.width, 1)
        r1 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(r1.height, 2)
        r1 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(r1.x, 3)
        r1 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(r1.y, 4)
    def test_rectangle_save_to_file(self):
        Rectangle.save_to_file(None)
        if not os.path.isfile("Rectangle.json"):
            raise AssertionError()
        Rectangle.save_to_file([])
        if not os.path.isfile("Rectangle.json"):
            raise AssertionError()
        Rectangle.save_to_file([Rectangle(1, 2)])
        if not os.path.isfile("Rectangle.json"):
            raise AssertionError()
    def test_rectangle_load_from_file(self):
        """
        loaded = Rectangle.load_from_file()
        self.assertEqual(loaded, [])
        Rectangle.save_to_file(Rectangle(1, 1, 1, 1, 1))
        loaded = Rectangle.load_from_file()
        self.assertEqual(loaded, {'x': 1, 'y': 1, 'id': 1, 'height': 1, 'width': 1})
        """
        pass
