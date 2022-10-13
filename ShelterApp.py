from Animal import Animal
from Dog import Dog
from Cat import Cat
from Bird import Bird
from Shelter import Shelter
from Person import Person
from Employee import Employee

if __name__ == '__main__':
    print("The shelter story.")
        
    # Create a new Shelter
    
    myShelter = Shelter("Jit's Shelter", "Miami", "111-2222")
    print(myShelter)

    # Hire some people
    print("\nBuilding the team..")
    
    john = Employee("John", "555-1212", "owner", "john@shelter.org")
    shiela = Employee("Shiela", "555-3434", "admin", "shiela@shelter.org")
    myShelter.hire(john)
    myShelter.hire(shiela)
    
    
    # Receive some animals
    print("\nWe are getting some animals!")
    myShelter.receive(Dog("Bob", 24, "brown"), john)
    myShelter.receive(Cat("Roxie", 5, "tabbie"), shiela)
    myShelter.receive(Bird("Coco", 2, "red", 3), shiela)
    
    
    # Let all animals go crazy
    print("\n{} animals are making a big ruccus!".format(myShelter.numAnimals()))
    myShelter.chorus();
    
    print("\n");
    joe = Person("Joe", "123-456-78")
    myShelter.processAdoption(joe, myShelter.findAnimal("Bob"))
    
    print("Now we have {}  animals left.".format(myShelter.numAnimals()))
    