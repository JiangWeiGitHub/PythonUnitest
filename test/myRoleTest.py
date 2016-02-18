import unittest

from source.myRole import myRole

class MyRoleTest(unittest.TestCase):

    def test_getName(self):
        d = myRole()
        self.assertEquals(d.name, 'john')
        
    def test_setName(self):
        d = myRole()
        d.setName('jiang')
        self.assertEquals(d.name, 'jiang')

    def test_getAge(self):
        d = myRole()
        self.assertEquals(d.age, 18)
        
    def test_setAge(self):
        d = myRole()
        d.setAge(21)
        self.assertEquals(d.age, 21)

    def test_setNameError(self):
        d = myRole()
        with self.assertRaises(TypeError):
            d.setName(99999)

    def test_setAgeError(self):
        d = myRole()
        with self.assertRaises(TypeError):
            d.setAge('hello')
