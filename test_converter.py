import unittest
from unittest import TestCase
from src.converter import Converter

class TestConverter(TestCase):

    def test_right_template_name(self):
        converter = Converter()
        result = converter.to_jinja("storage")
        self.assertEqual(result, "storage.j2")


if __name__ == '__main__':
    unittest.main()
