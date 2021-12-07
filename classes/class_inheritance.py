
# Parent class with a function
class Animal:
    species = 'No species name provided'
    color = 'No color provided'
    age = 0

    def escape(self):
        print('The animal has escaped!')


# child class with polymorphism
class Dog(Animal):
    breed = 'No breed provided'
    name = 'No name provided'
    trained = False

    # utilizing polymorphism
    def escape(self):
        print('The dog has escaped')

    
# child class with polymorphism
class Cat(Animal):
    breed = 'No breed provided'
    name = 'No name provided'
    feral = False

    # utilizing polymorphism, different messages for feral and not feral cats
    def escape(self):
        if self.feral == False:
            print('Your pet escaped!')
        if self.feral == True:
            print('The feral cat escaped!')


# child class with polymorphism
class Panda(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def panda_roll(self):
        print('Panda rolls down the hill!')

    # utilizing polymorphism, different messages for baby or adult panda
    def escape(self):
        if self.age < 2:
            print('The baby panda has escaped!')
        else:
            print('The adult panda has escaped!')

        




if __name__ == "__main__":

    # check classes and functions
    
    # make a dog & check function
    dog = Dog()
    dog.escape()

    # make a pet cat(not feral) and check function
    cat_pet = Cat()
    cat_pet.escape()
    
    # make a wild cat(feral) and check function
    cat_wild = Cat()
    cat_wild.feral = True
    cat_wild.escape()

    # make an adult panda and check attributes and functions
    panda1 = Panda('Ling Ling', 5)
    print(panda1.name)
    print(panda1.age)
    panda1.panda_roll()
    panda1.escape()

    # make a baby panda and check function
    panda2 = Panda('Mei', 1)
    panda2.escape()
