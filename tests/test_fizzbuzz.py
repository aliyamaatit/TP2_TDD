import unittest
from fizzbuzz.core import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_retourne_chaine(self):
        # test minimal : la fonction retourne une chaîne
        self.assertIsInstance(affiche(), str)

if __name__ == "__main__":
    unittest.main()
