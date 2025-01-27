import random
class Ghost(object):
    def __init__(self):
        color_lst = ['white', 'yellow', 'purple', 'red']
        self.color = color_lst[random.randint(0,3)]