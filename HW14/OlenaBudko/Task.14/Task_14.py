import unittest
import functions as func
import functions_with_errors as func_err


class TestFunction(unittest.TestCase):

    def test_greeting_fun(self):
        test_data = ["lena", "olha1", "Olga_1", "1234", "123@"]
        for data in test_data:
            with self.subTest(name=data):
                self.assertEqual(func.greeting_by_name(data), f"Hello {data}!", "Failed")

    def test_greeting_fune(self):
        test_data = ["lena", "olha1", "Olga_1", "1234", "123@"]
        for data in test_data:
            with self.subTest(name=data):
                self.assertEqual(func_err.greeting_by_name(data), f"Hello {data}!", "Failed")

    def test_get_symbol_fun(self):
        test_data = [
            ["Roman", "rr", "Error! Symbol can be string with only one letter"],
            ["romman", "m", 3],
            ["Roman", "w", "Not found"]]
        for data in test_data:
            with self.subTest(text=data[0], symbol=data[1]):
                self.assertEqual(func.get_symbol_position(data[0], data[1]), data[2], "Failed")

    def test_get_symbol_fune(self):
        test_data = [
            ["Roman", "rr", "Error! Symbol can be string with only one letter"],
            ["romman", "m", 3],
            ["Roman", "w", "Not found"]]
        for data in test_data:
            with self.subTest(text=data[0], symbol=data[1]):
                self.assertEqual(func_err.get_symbol_position(data[0], data[1]), data[2], "Failed")

    def test_merge_fun(self):
        test_data = [
            [{"name": "Roman", "age": "25"}, {"position": "manager", "salary": "11200"}],
            [{"1": "2", "2": "4"}, {"3": "name", "4": "age"}]
        ]
        for data in test_data:
            with self.subTest(dict1=data[0], dict2=data[1]):
                self.assertLess(data[0].items(), func.merge(data[0], data[1]).items(), "Failed")

    def test_merge_fune(self):
        test_data = [
            [{"name": "Roman", "age": "25"}, {"position": "manager", "salary": "11200"}],
            [{"1": "2", "2": "4"}, {"3": "name", "4": "age"}]
        ]
        for data in test_data:
            with self.subTest(dict1=data[0], dict2=data[1]):
                self.assertLess(data[0].items(), func_err.merge(data[0], data[1]).items(), "Failed")


if __name__ == '__main__':
    unittest.main()
