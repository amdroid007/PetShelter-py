from Person import Person

"""
 * 
 * An employee is a subclass of Person
 * 
 * @author arijitsengupta
 *
"""
class Employee(Person):

    """
     * @param name Name of the person
     * @param phonenumber phone number of person
     * @param position position of the person in the shelter
     * @param email email of the person
    """
    def __init__(self, name, phonenumber, position, email):
        super().__init__(name, phonenumber)
        self._position = position
        self._email = email

    """
     * @return the position
    """
    def getPosition(self):
        return self._position

    """
     * @param position the position to set
    """
    def setPosition(self, position):
        self._position = position

    """
     * @return the email
    """
    def getEmail(self):
        return self._email;

    """
     * @param email the email to set
    """
    def setEmail(self,  email):
        self._email = email
