# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe()” method (which prints “name” and “kind” in a sentence).
# class Food:
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind

#     def describe(self):
#         print('I am of type {} and my name is {}'.format(self.kind, self.name))


# banana = Food('Banana', 'fruit')
# pork = Food('Pork', 'meat')
# banana.describe()
# pork.describe()
# 2) Try turning describe() from an instance method into a class and a static method. Change it back to an instance method thereafter.
# class Food:
#     name = 'X'
#     kind = 'Y'
#     # def __init__(self, name, kind):
#     #     self.name = name
#     #     self.kind = kind

#     @staticmethod
#     def describe(kind, name):
#         print('I am of type {} and my name is {}'.format(kind, name))


# Food.name = 'Banana'
# Food.kind = 'fruit'
# Food.describe('meat','Pork')
# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook()” method to “Meat” and “clean()” to “Fruit”.
class Food:
    name = 'X'
    kind = 'Y'
    # def __init__(self, name, kind):
    #     self.name = name
    #     self.kind = kind

    @staticmethod
    def describe(kind, name):
        print('I am of type {} and my name is {}'.format(kind, name))


Food.name = 'Banana'
Food.kind = 'fruit'
Food.describe('meat','Pork')

# 4) Overwrite a “dunder” method to be able to print your “Food” class.
