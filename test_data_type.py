import unittest
from data_type import data_type
class DataTypeTestCase(unittest.TestCase):
  #test for string data supplied. 
  def test_str_type(self):
    self.assertEqual(6, data_type('andela'))
  #test for null input/none
  def test_none_type(self):
    self.assertEqual('no value', data_type(None))