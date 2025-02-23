from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, Session
import re

engine = create_engine('sqlite:///database.db', echo=True)
s = Session(bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    decker = relationship('Decker', back_populates='user')

    def __repr__(self):
        return '({!r}, {!r}, {!r})'.format(self.name, self.email, self.password)


class Decker(Base):
    __tablename__ = 'decker'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='decker')
    card = relationship('Card', back_populates='decker')

    def __repr__(self):
        return '({!r}, {!r})'.format(self.name, self.user_id)


class Card(Base):
    __tablename__ = 'card'

    id = Column(Integer, primary_key=True)
    deck_id = Column(Integer, ForeignKey('decker.id'))
    word = Column(String)
    translation = Column(String)
    tip = Column(String)
    decker = relationship('Decker', back_populates='card')

    def __repr__(self):
        return '({!r}, {!r}, {!r}, {!r})'.format(self.deck_id, self.word, self.translation, self.tip)


Base.metadata.create_all(engine)


def user_create(name, email, password):
    user_one = User(name=name, email=email, password=password)
    s.add(user_one)
    s.commit()
    return User


def user_get_by_id(user_id):
    return s.query(User).filter_by(id=user_id).all()


def user_update_name(user_id, name):
    update_user = s.query(User).filter_by(id=user_id).first()
    update_user.name = name
    s.commit()
    return User


def user_change_password(user_id, old_password, new_password):
    update_password = s.query(User).filter_by(id=user_id).first()
    password = s.query(User.password).filter_by(id=user_id).first()
    if password[0] == old_password:
        update_password.password = new_password
        s.commit()
        return True
    else:
        return False


def user_delete_by_id(user_id):
    delete_user = s.query(User).filter_by(id=user_id).first()
    s.delete(delete_user)
    s.commit()
    return True if not s.query(User).filter_by(id=user_id).all() else False


def deck_create(name, user_id):
    deck_one = Decker(name=name, user_id=user_id)
    s.add(deck_one)
    s.commit()
    return Decker


def deck_get_by_id(deck_id):
    return s.query(Decker).filter_by(id=deck_id).all()


def deck_update(deck_id, name):
    update_deck = s.query(Decker).filter_by(id=deck_id).first()
    update_deck.name = name
    s.commit()
    return Decker


def deck_delete_by_id(deck_id):
    delete_deck = s.query(Decker).filter_by(id=deck_id).first()
    s.delete(delete_deck)
    s.commit()
    return True if not s.query(Decker).filter_by(id=deck_id).all() else False


def card_create(deck_id, word, translation, tip=None):
    card_one = Card(deck_id=deck_id, word=word, translation=translation, tip=tip)
    s.add(card_one)
    s.commit()
    return Card


def card_get_by_id(card_id):
    return s.query(Card).filter_by(id=card_id).all()


def card_filter(sub_word):
    result = list(s.query(Card).all())
    card_tulip = ()
    for row in result:
        if re.findall(f'{sub_word}+', str(row)):
            card_tulip += (row,)
    return card_tulip


def card_update(card_id, word=None, translation=None, tip=None):
    update_card = s.query(Card).filter_by(id=card_id).first()
    update_card.word = word
    update_card.translation = translation
    update_card.tip = tip
    s.commit()
    return Card


def card_delete_by_id(card_id):
    delete_card = s.query(Card).filter_by(id=card_id).first()
    s.delete(delete_card)
    s.commit()
    return True if not s.query(Card).filter_by(id=card_id).all() else False
