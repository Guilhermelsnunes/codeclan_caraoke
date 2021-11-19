import unittest
from classes.guest import Guest 

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("John", 35)

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(35, self.guest.age)