import unittest

from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):

  def test_Rectangle_init(self):
      r1 = Rectangle(10, 402)
      r2 = Rectangle(1, 5)
      print(f"r1's id : {r1.id}")
      print(f"r2's id : {r2.id}")
      self.assertEqual(r1.id, 1)
      self.assertEqual(r2.id, 2)
      
#      #self.assertEqual('foo'.upper(), 'FOO')

  def test_id_given(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
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
