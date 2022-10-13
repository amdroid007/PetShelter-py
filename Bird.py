from Animal import Animal

"""
 * 
 * The Bird class as a subclass of Animal
 * 
 * @author arijitsengupta
 *
"""
class Bird(Animal):

    """
     * Constructor for bird
     * 
     * @param name name of bird
     * @param age  age of bird
     * @param color color of bird
     * @param wingspan wingspan of bird
    """
    def __init__(self, name, age, color, wingspan):
        super().__init__(name, age, color)
        self._wingspan = wingspan

    """
     * @return the wingspan
    """
    def getWingspan(self):
        return _wingspan

    """
     * @param wingspan the wingspan to set
    """
    def setWingspan(self, wingspan):
        self._wingspan = wingspan

    def __str__(self) -> str:
        return "{} with wingspan of {} ft.".format(super().__str__(), self._wingspan)
    
    def makeSound(self):
        print("{} says chirp!".format(self.getName()))
