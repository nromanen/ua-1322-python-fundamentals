import unittest
from functions import greeting_by_name, get_symbol_position, merge
# We can also import the same functions from module 'functions_with_errors.py' to test them


class TestFunctions(unittest.TestCase):
    def test_greeting_by_name(self):
        """Testing the function 'greeting_by_name' in both modules"""
        self.assertEqual(greeting_by_name('Ihor'), 'Hello Ihor!', f'For "Ihor" must be "Hello Ihor!" but now is '
                                                                  f'"{greeting_by_name("Ihor")}"')

    def test_get_symbol_position(self):
        """Testing the function 'get_symbol_position' in both modules"""
        test_data = [('This is my test', 'my', 'Error! Symbol can be string with only one letter'),
                     ('This is my test', 'm', 9),
                     ('This is my test', 'a', 'Not found')
                     ]
        for i in test_data:
            with self.subTest(data=i):
                self.assertEqual(get_symbol_position(i[0], i[1]), i[2], f'For "{i[1]}" must be "{i[2]}" but now is '
                                                                        f'"{get_symbol_position(i[0], i[1])}"')

    def test_merge(self):
        """Testing the function 'merge' in both modules"""
        dicts = [{'key': 'value'}, {'key1': 'value1'}, {'key': 'value', 'key1': 'value1'}]
        for i in range(3):
            with self.subTest(data=i):
                dict1 = [{'key': 'value'}, {'key1': 'value1'}, {'key': 'value', 'key1': 'value1'}]
                merge(dict1[0], dict1[1])
                self.assertEqual(dict1[i], dicts[i], f'The meaning of the every dictionary in "dict1" must be the '
                                                     f'same after executing of the function as before. But now it is '
                                                     f'"{dict1[i]}')


if __name__ == '__main__':
    unittest.main()
