class Mychoco(type): # Inheriting from 'type' makes this a meta class
    def __new__(cls, name, bases, class_dict):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, class_dict)

# Using the meta class to create a new class
class MyClass (metaclass=Mychoco):
    pass
#2
class AutoAddMethodMeta (type):
    def __new__(cls, name, bases, class_dict):
        class_dict['greet'] = lambda self: "Hello from auto-added method!"
        return super().__new__(cls, name, bases, class_dict)

class Person(metaclass=AutoAddMethodMeta):
    pass

p = Person()
print(p.greet())

class Mychoco(type):  # Inheriting from 'type' makes this a meta class
    def __new__(cls, name, bases, class_dict):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, class_dict)

# Using the meta class to create a new class
class MyClass(metaclass=Mychoco):
    pass


class NBAClassMeta(type):  # Inheriting from 'type' makes this a meta class
    def __new__(cls, name, bases, class_dict):
        print(f"Drafting NBA Legend class: {name}")
        return super().__new__(cls, name, bases, class_dict)

# Using the meta class to create NBA legends
class NBAPlayer(metaclass=NBAClassMeta):
    pass

# Second meta class to auto-add a legendary move
class LegendaryMoveMeta(type):
    def __new__(cls, name, bases, class_dict):
        # Add a method for a signature move
        class_dict['signature_move'] = lambda self: "Unstoppable fadeaway!"
        return super().__new__(cls, name, bases, class_dict)

class MichaelJordan(metaclass=LegendaryMoveMeta):
    pass

class KobeBryant(metaclass=LegendaryMoveMeta):
    pass

mj = MichaelJordan()
kobe = KobeBryant()

print(mj.signature_move())  # Output: Unstoppable fadeaway!
print(kobe.signature_move())  # Output: Unstoppable fadeaway!
