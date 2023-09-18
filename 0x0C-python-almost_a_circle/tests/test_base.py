import unittest

from models.base import Base

class TestBaseClass(unittest.TestCase):

  def test_Base_init(self):
      b1 = Base()
      self.assertEqual(b1.id, 1)
      
#      #self.assertEqual('foo'.upper(), 'FOO')

  def test_id_given(self):
      b2 = Base(13)
      self.assertEqual(b2.id, 13)
#      #self.assertTrue('FOO'.isupper())
#      #self.assertFalse('Foo'.isupper())

#  def test_split(self):
#      #s = 'hello world'
#      #self.assertEqual(s.split(), ['hello', 'world'])
#      # check that s.split fails when the separator is not a string
#      #with self.assertRaises(TypeError):
#          #s.split(2)

if __name__ == '__main__':
    unittest.main()
