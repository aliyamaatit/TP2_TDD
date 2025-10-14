import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche(self):
        s = affiche()
        self.assertTrue(s.startswith("12Fizz4Buzz"))
        self.assertIn("FrisBee", s)  # 15 -> FrisBee
