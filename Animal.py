"""
 * The base Animal Class - includes basic information on animals
 * 
 * @author arijitsengupta
 *
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    
    def __init__ (self, name, age, color):
        self._name = name
        self._age = age
        self._color = color
    
    """
     * Make a sound
    """
    @abstractmethod
    def makeSound(self):
        pass
    
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
     * @return the age
    """
    def getAge(self):
        return self._age
    
    """
     * @param age the age to set
    """
    def setAge(self, age):
        self._age = age
    
    """
     * @return the color
    """
    def getColor(self):
        return self._color
    
    """
     * @param color the color to set
    """
    def setColor(self, color):
        self._color = color
    
    
    def __str__(self) -> str:
        return "a {} named {} (age: {} months, color: {})".format(type(self).__name__, self._name, self._age, self._color)

