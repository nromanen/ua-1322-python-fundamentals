import unittest
from valid_password import valid_password


class TestValidPassword(unittest.TestCase):
    len_password = 'Must be at least 6 characters and no more than 16 characters.'
    lowercase = 'Must contain at least one lowercase letter.'
    uppercase = 'Must contain at least one uppercase letter.'
    digit = 'Must contain at least one digit.'
    character = 'Must contain at least one special character from [$#@].'
    valid = 'Password is valid'

    def test_invalid_password(self):
        """Testing of the invalid password"""
        test_data = [('fg', f"{self.len_password}\n{self.uppercase}\n{self.digit}\n{self.character}"),
                     ('FG', f"{self.len_password}\n{self.lowercase}\n{self.digit}\n{self.character}"),
                     ('12', f"{self.len_password}\n{self.lowercase}\n{self.uppercase}\n{self.character}"),
                     ('#@', f"{self.len_password}\n{self.lowercase}\n{self.uppercase}\n{self.digit}"),
                     ('FG12@#', f"{self.lowercase}"),
                     ('12fg@#', f"{self.uppercase}"),
                     ('fg@#FG', f"{self.digit}"),
                     ('fgFG12&^', f"{self.character}"),
                     ('fG1@', f'{self.len_password}'),
                     ('ffggFFGG1122@@##11', f'{self.len_password}')
                     ]
        for i in test_data:
            with self.subTest(data=i):
                self.assertEqual(valid_password(i[0]), i[1], f'For "{i[0]}" must be "{i[1]}" but now is '
                                                             f'"{valid_password(i[0])}"')

    def test_valid_password(self):
        """Testing of the valid password"""
        test_data = [('fgFG12@#', f'{self.valid}'),
                     ('FG12#fg', f'{self.valid}'),
                     ('jkfFGG124%$', f'{self.valid}'),
                     ('123$fggFGG', f'{self.valid}'),
                     ('Ihor@29', f'{self.valid}')
                     ]
        for i in test_data:
            with self.subTest(data=i):
                self.assertEqual(valid_password(i[0]), i[1], f' For "{i[0]}" must be "{i[1]}" but now is '
                                                             f'"{valid_password(i[0])}"')


if __name__ == '__main__':
    unittest.main()
