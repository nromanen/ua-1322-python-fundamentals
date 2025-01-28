import unittest
from pass_check_func import check
import random

class TestStringMethods(unittest.TestCase):
    def test_pass_positive(self):
        data_pos = ["abC123@", "Nnn@nnnn33!", "hahAha31$", "wanniG2@"]
        for test1 in data_pos:
            with self.subTest(paswd = test1):
                result1 = check(test1)
                self.assertFalse(result1, f"Should return Errrors!")

    def test_pass_negative(self):
        data_neg = ["@a", "aaaaaaaaaaAAAAAAaaaAAAAAAAA222222@@@@@@", "abc3332$", "HEELO$5", "SSSSSSSSSS@ssss", "@#!@%!@#!"]
        for test in data_neg:
            with self.subTest(paswd = test):
                result = check(test)
                self.assertTrue(result, f"Test returned False when it should have returned True!")

    def test_pass_random(self):
        data_rand = []
        [data_rand.append("".join(chr(random.randint(65, 122)) for x in range(random.randint(0,32)))) for x in range(50)]
        for test in data_rand:
            with self.subTest(paswd = test):
                result = check(test)
                self.assertTrue(result, f"Should return Errors!")


if __name__ == "__main__":
    unittest.main()