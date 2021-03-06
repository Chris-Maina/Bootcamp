import unittest
from data_type import data_type
class DataTypeTestCase(unittest.TestCase):
  #test for string  supplied. 
  def test_str_type(self):
    self.assertEqual(6, data_type('andela'))
  #test for null input/none 
  def test_none_type(self):
    self.assertEqual('no value', data_type(None))
  #test for boolean 
  def test_small_booleans_type(self):
    self.assertEqual(True,data_type(True))
  #test for less than hundred data supplied
  def test_small_integer_type(self):
    self.assertEqual('less than 100',data_type(3))
  #test for more than hundred data supplied
  def test_large_integer_type(self):
    self.assertEqual('more than 100',data_type(200))
  #test for 3rd item in list
  def test_array_type(self):
    self.assertEqual(3,data_type([1,2,3]))
  #test for None in list
  def test_small_array_type(self):
    self.assertEqual(None,data_type([1,2]))