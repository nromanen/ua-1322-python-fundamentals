import unittest
import functions as f
import functions_with_errors as fe

class TestStringMethods(unittest.TestCase):
    def test_greeting_f(self):
        print ("Testing greeting_by_name in functions.py")
        data = ["Jon", "Bob", "ISHMAIL", "carrot1234", "cathulu the destroyer"]
        for test in data:
            with self.subTest(name=test):
                self.assertEqual(f.greeting_by_name(test), f"Hello {test}!", "is Failed")
    
    def test_greeting_fe(self):
        print ("Testing greeting_by_name in functions_with_errors.py")
        data = ["Jon", "Bob", "ISHMAIL", "carrot1234", "cathulu the destroyer"]
        for test in data:
            with self.subTest(name=test):
                self.assertEqual(fe.greeting_by_name(test), f"Hello {test}!", "is Failed")

    def test_get_symbol_position_f(self):
        print ("Testing get_symbol_position in functions.py")
        data = [["Hello!", "!", 6], ["Bye", "@.", "Error! Symbol can be string with only one letter"],
                ["gmail.", "@", "Not found"], ["hot^dog", "^", 4]]
        for test in data:
            with self.subTest(text = test[0], symbol = test[1]):
                self.assertEqual(f.get_symbol_position(test[0], test[1]), test[2], f"with {test[2]} is Failed")

    def test_get_symbol_position_fe(self):
        print ("Testing get_symbol_position in functions_with_errors.py")
        data = [["Hello!", "!", 6], ["Bye", "@.", "Error! Symbol can be string with only one letter"],
                ["gmail.", "@", "Not found"], ["hot^dog", "^", 4]]
        for test in data:
            with self.subTest(text = test[0], symbol = test[1]):
                self.assertEqual(fe.get_symbol_position(test[0], test[1]), test[2], f"with {test[2]} is Failed")

    def test_merge_f(self):
        print ("Testing merge dict in functions.py")
        data = [({1: 3, 3: 4, 2: 6} , {6: 8, 2: 3, 3: 7}, {1: 3, 3: 7, 2: 3, 6: 8}), 
                ({5: 3, 3: 4}, {6: 8, 2: 3, 12: 7}, {5: 3, 3: 4, 6: 8, 2: 3, 12: 7})]
        
        for test in data:
            with self.subTest(dict1 = test[0], dict = test[1]):
                result = f.merge(test[0], test[1])
                self.assertIsNot(test[0], result, "Immutability Failed")

    def test_merge_fe(self):
        print ("Testing merge dict in functions_with_errors.py")
        data = [({1: 3, 3: 4, 2: 6} , {6: 8, 2: 3, 3: 7}, {1: 3, 3: 7, 2: 3, 6: 8}), 
                ({5: 3, 3: 4}, {6: 8, 2: 3, 12: 7}, {5: 3, 3: 4, 6: 8, 2: 3, 12: 7})]
        
        for test in data:
            with self.subTest(dict1 = test[0], dict = test[1]):
                result = fe.merge(test[0], test[1])
                self.assertIsNot(result, test[0], "Immutability Failed")





if __name__ == "__main__":
    unittest.main()