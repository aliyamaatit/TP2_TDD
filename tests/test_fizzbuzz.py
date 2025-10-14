import unittest
from fizzbuzz import affiche

class T(unittest.TestCase):
    def test_min(self):
        s = affiche()
        self.assertIsInstance(s, str)               # renvoie une chaîne
        self.assertTrue(s.startswith("12Fizz4Buzz"))# début 1..5 correct
        self.assertIn("FrisBee", s)                 # 15 = FrisBee

if __name__ == "__main__":
    unittest.main()
