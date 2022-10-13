from Animal import Animal
from Person import Person
from Employee import Employee

""""
 * This is the main Shelter class that has information on the Shelter
 * as well as the animals that it houses.
 * 
 * Includes a main method that runs the application
 * 
 * @author arijitsengupta
 *
"""
class Shelter:
    
    """
     * Constructor for Shelter - uses name, address, phone to create a shelter
     * initializes animals hashtable
     * 
     * @param name name of shelter
     * @param address address of shelter
     * @param phone phone number of shelter
    """
    def __init__(self, name, address, phone):
        self._name = name
        self._address = address
        self._phone = phone
        self._animals = {}
        self._employees = {}
    
    """
     * Get the number of available animals
     * @return the number of animals
    """
    def numAnimals(self):
        return len(self._animals)


    """
     * Find an animal by name
     * @param name name of animal to find
     * @return the Animal with that name
    """
    def findAnimal(self, name)-> Animal:
        return self._animals[name]

    """
     * Have all animals in the shelter make their sounds
    """
    def chorus(self):
        for beast in self._animals.values():
            beast.makeSound()

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
     * @return the address
    """
    def getAddress(self):
        return self._address

    """
     * @param address the address to set
    """
    def setAddress(self, address):
        self._address = address

    """
     * @return the phone
    """
    def getPhone(self):
        return self._phone

    """
     * @param phone the phone to set
    """
    def setPhone(self, phone):
        self._phone = phone


    """
     * Hire an employee into the shelter
     * @param employee the employee we are hiring
    """
    def hire(self, employee:Employee):
        self._employees[employee.getName()] = employee
        print("{} joined {} as {}".format(employee.getName(), self.getName(), employee.getPosition()))

    """
     * Process an Adoption
     * @param adopter the person who is adopting the animal
     * @param adoptee the animal that is getting adopted
    """
    def processAdoption(self, adopter: Person, adoptee: Animal):
        processedAnimal = self._animals.pop(adoptee.getName())
        adopter.adopt(processedAnimal)        
        print("{} adopted {}".format(adopter, adoptee))

    """
     * Receive an animal into the shelter
     * @param animal the animal that is received
     * @param employee the employee who is receiving the animal
    """
    def receive(self, animal: Animal, employee: Employee):
        print("{} received {}".format(employee.getName(), animal))
        self._animals[animal.getName()] = animal      

    """
     * @return a string representation of the shelter
    """
    def __str__(self) -> str:
        return "Shelter Information: \n\tName: {}\n\tAddress: {}\n\tPhone: {}".format(self.getName(), self.getAddress(), self.getPhone())        
