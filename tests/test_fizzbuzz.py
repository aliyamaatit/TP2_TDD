import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_debut_et_frisbee(self):
        s = affiche()  # par défaut 1..100
        self.assertTrue(s.startswith("12Fizz4Buzz"))
        self.assertIn("FrisBee", s)  # 15 -> FrisBee

    def test_affiche_jusqua_n(self):
        attendu = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"
        self.assertEqual(affiche(15), attendu)

    def test_affiche_intervalle_5_10(self):
        self.assertEqual(affiche(5, 10), "BuzzFizz78FizzBuzz")

    def test_affiche_intervalle_10_16(self):
        self.assertEqual(affiche(10, 16), "Buzz11Fizz1314FrisBee16")
