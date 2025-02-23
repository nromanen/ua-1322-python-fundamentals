import linguist as lin

lin.user_create(name='Ihor', email='boigor95@gmail.com', password='12345')
lin.user_create(name='Olha', email='olha@gmail.com', password='987654')
lin.user_create(name='Petro', email='petro@gmail.com', password='123')
lin.deck_create('animals', 1)
lin.deck_create('family', 1)
lin.deck_create('home', 2)
lin.deck_create('nature', 2)
lin.deck_create('school', 2)
lin.card_create(1, 'dog', 'собака', 'гав')
lin.card_create(1, 'cat', 'кіт', 'мяу')
lin.card_create(2, 'sister', 'сестра', 'дівчина')
lin.card_create(2, 'brother', 'брат', 'хлопець')
lin.card_create(2, 'mother', 'мама')
lin.card_create(3, 'house', 'будинок', 'споруда')
lin.card_create(3, 'kitchen', 'кухня', 'їжа')
lin.card_create(5, 'pen', 'ручка', 'писати')
lin.card_create(5, 'subject', 'предмет')
lin.user_update_name(2, 'Ivan')
assert lin.user_change_password(2, '987654', '456789') is True
assert lin.user_delete_by_id(3) is True
lin.deck_update(5, 'study')
assert lin.deck_delete_by_id(4) is True
lin.card_update(9, 'lesson', 'урок', '45хв')
assert lin.card_delete_by_id(8) is True
assert str(lin.user_get_by_id(2)) == str([('Ivan', 'olha@gmail.com', '456789')])
assert str(lin.deck_get_by_id(2)) == str([('family', 1)])
assert str(lin.card_get_by_id(3)) == str([(2, 'sister', 'сестра', 'дівчина')])
assert str(lin.card_get_by_id(9)) == str([(5, 'lesson', 'урок', '45хв')])
assert str(lin.card_filter('oth')) == str(((2, 'brother', 'брат', 'хлопець'), (2, 'mother', 'мама', None)))
