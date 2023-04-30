import unittest

from prime import is_prime

class Test(unittest.TestCase):
    def test1(self):
        """ Test 1 is prime """
        self.assertFalse(is_prime(1))

    def test2(self):
        """ Test 2 is prime """
        self.assertTrue(is_prime(2))

    def test3(self):
        """ Test 3 is prime """
        self.assertEqual(is_prime(3), True)

    def test5(self):
        """ Test 5 is prime """
        assert is_prime(5) == True

    def test7(self):
        """ Test 7 is prime """
        assert is_prime(7) == True

if __name__ == "__main__":
    unittest.main()