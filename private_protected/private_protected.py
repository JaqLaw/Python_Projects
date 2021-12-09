
class Student:
    
    def __init__(self,name):
        self._name = name  # protected variable
        
    def __display(self):  # private method
        print('This is a private method.')

    def help(self):
        self.__display()




std = Student('Casey')  # create a student object

std._name = 'Cassie'  # changing a protected variable

# std.__display  # demonstrating that you can't call a private method in the traditional way

std._Student__display()  # demonstrating how to call a private method

std.help()  # demonstrating another way to call a private method (via another method)
