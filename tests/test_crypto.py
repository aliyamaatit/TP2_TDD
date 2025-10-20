import unittest
from crypto import crypt

class TestCrypto(unittest.TestCase):
    def test_crypt_pas_1_sans_suffixe(self):
        # A) crypt(message)
        self.assertEqual(crypt("aZ9!"), 'b! "')

    def test_crypt_avec_pas_et_suffixe(self):
        # B) crypt(message, pas)
        self.assertEqual(crypt("abc", 3), "def3")

if __name__ == "__main__":
    unittest.main()
