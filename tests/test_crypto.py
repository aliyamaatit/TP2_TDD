import unittest
from crypto import crypt

class TestCrypto(unittest.TestCase):
    def test_crypt_pas_1_sans_suffixe(self):
        # A) crypt(message)
        self.assertEqual(crypt("aZ9!"), 'b! "')

    def test_crypt_avec_pas_et_suffixe(self):
        # B) crypt(message, pas)
        self.assertEqual(crypt("abc", 3), "def3")

    def test_decrypt_inverse_crypt(self):
        # crypt avec pas=2 ajoute le suffixe "2"
        chiffré = crypt("Hello!", 2)
        self.assertEqual(decrypt(chiffré), "Hello!")

    def test_decrypt_wrap(self):
        # vérifie le wrap-around aux extrémités de la table
        c = "~"              
        chiffré = crypt(c, 3)
        self.assertEqual(decrypt(chiffré), c)

if __name__ == "__main__":
    unittest.main()
