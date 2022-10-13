from Animal import Animal

""""
 * The generic person class with contact information and pets
 * 
 * @author arijitsengupta
 *
"""

class Person:
    
    """
     * Basic constructor for Person
     * @param name name of person
     * @param phonenumber phone number of person
    """
    def __init__(self, name, phonenumber):
        self._name = name
        self._phonenumber = phonenumber
        self._pets = []

    """
     * @return the name
    """
    def getName(self):
        return self._name


    """
     * @param name the name to set
    """
    def setName(self, name):
        self._name = name

    """
     * @return the phonenumber
    """
    def getPhonenumber(self):
        return self._phonenumber

    """
     * @param phonenumber the phonenumber to set
    """
    def setPhonenumber(self, phonenumber):
        self._phonenumber = phonenumber

    """
     * Adopt an animal
     * @param processedAnimal the animal who the person is adopting
    """
    def adopt(self, processedAnimal:Animal):
        self._pets.append(processedAnimal)
    
    def __str__(self) -> str:
        return "{} (phone: {})".format(self._name, self._phonenumber)
