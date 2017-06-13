import unittest
from data_type import data_type
class DataTypeTestCase(unittest.TestCase):
  #test for string data supplied. 
  def test_str_type(self):
    self.assertEqual(6, data_type('andela'))