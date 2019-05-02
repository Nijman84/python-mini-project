#!/usr/bin/python


class Animal(object):
    def __init__(self, moves, num_legs):
        self.moves = moves
        self.num_legs = num_legs

    def describe(self):
        print('Moves :{} , num_legs : {}'.format(self.moves, self.num_legs))


class Snake(Animal):
    def __init__(self, poisonous, *args, **kwds):
        self.poisonous = poisonous
        print('I am poisonous:{}'.format(self.poisonous))
        # This next line is key. You have to use *args , **kwds.
        # But here I have deliberately used the incorrect form,
        # `args` and `kwds`, and am suprised at what it does.
        super(Snake, self).__init__(args, kwds)


s1 = Snake(False, moves=True, num_legs=0)
s2 = Snake(poisonous=False, moves=True, num_legs=1)
s3 = Snake(False, True, 3)
s1.describe()
s2.describe()
s3.describe()
