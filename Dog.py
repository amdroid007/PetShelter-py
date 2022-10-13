"""
 * 
 * Dog - a subclass of Animal representing dogs
 * 
 * @author arijitsengupta
 *
"""
from Animal import Animal

class Dog(Animal):

    """
     * Base constructor of Dog
     * 
     * @param name name of dog
     * @param age age of dog (in months)
     * @param color color of dog
    """
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    
    def makeSound(self):
        print("{} says woof!".format(self.getName()))
