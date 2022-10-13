from Animal import Animal

"""
 * The Cat class as a subclass of Animal
 * 
 * @author arijitsengupta
 *
"""
class Cat(Animal):

    """
     * Base constructor of Cat
     * 
     * @param name name of cat
     * @param age age of cat (in months)
     * @param color color of cat
    """
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    def makeSound(self):
        print("{} says meow!".format(self.getName()))
