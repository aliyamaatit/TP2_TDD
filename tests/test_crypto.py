import unittest
from crypto import crypt

class TestCrypto(unittest.TestCase):
    def test_crypt_pas_1_sans_suffixe(self):
        self.assertEqual(crypt("aZ9!"), 'b! "')

if __name__ == "__main__":
    unittest.main()
