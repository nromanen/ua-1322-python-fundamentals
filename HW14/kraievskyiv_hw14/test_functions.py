import unittest
import functions as f

class TestFunctions(unittest.TestCase):
    def test_greeting(self):
        test_data = ["Frank", "Ronald", "Vladyslav", "aney17d"]
        for data in test_data:
            with self.subTest(f"Testing greeting for {data}"):
                self.assertEqual(f.greeting_by_name(data), f"Hello {data}!", 
                                 "Test greeting_by_name(name) is Failed")
    
    def test_symbol_position(self):
        test_data = [("Python", "t", 3), ("Homework", "l", "Not found"), ("SoftServe", "ft", "Error! Symbol can be string with only one letter")]
        for data in test_data:
            with self.subTest(f"Testing position of '{data[1]}' in '{data[0]}'"):
                self.assertEqual(f.get_symbol_position(data[0], data[1]), data[2])

    def test_merge(self):
        test_data = [{1:2, 3:4}, {5:6, 7:8}, {1:2, 3:4, 5:6, 7:8}]
        with self.subTest("Testing immutability of dictinaries"):
            merged = f.merge(test_data[0], test_data[1])
            self.assertNotEqual(test_data[0], merged, "dict1 immutability is failed")
            self.assertNotEqual(test_data[1], merged, "dict2 immutability is failed")

                
if __name__ == "__main__":
    unittest.main()