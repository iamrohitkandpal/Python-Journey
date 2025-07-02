class FirstClass:
    a = 12
    
    def hello(self):
        print("Hello from FirstClass")
        
# FirstClass().hello()

class Factory:
    def __init__(self, material, zips, pocket):
        self.material = material
        self.zips = zips
        self.pocket = pocket

    def cost(self):
        m_cost = {
            "Spandax": 100,
            "Cotton": 150,
            "Polyester": 200,
            "Leather": 300
        }
        return (self.zips * 100) + (self.pocket * 50) + m_cost.get(self.material, 0)

pajama = Factory("Spandax", 2, 4)
jacket = Factory("Leather", 4, 2)

# print(f"Jacket cost: {jacket.cost()}")
# print(f"Pajama cost: {pajama.cost()}")

class Animal: 
    name: "Animal"
    
    def __init__(self, type):
        self.type = type
    
    def show(self):
        print(f"Animal type: {self.type}")
    
    @classmethod
    def sound(cls):
        print("Animal makes sound")
        
    @staticmethod
    def info():
        print("Humans are animals too")

lion = Animal("Carnivore")

# lion.show()
# Animal.sound()
# Animal.info()

class Papa:
    genetics = "Strong"
    def __init__(self, fname):
        self.fname = fname

    def show(self):
        print(f"Papa's name is {self.fname} and genetics are {self.genetics}")

class Child(Papa):
    def __init__(self, fname, name):
        super().__init__(fname)  # Properly call the parent constructor
        self.name = name

    def show(self):
        print(f"Child's name is {self.name}, Father: {self.fname}, Genetics: {self.genetics}")

p = Papa("John")
c = Child(p.fname, "Doe")
# p.show()
# c.show()


from abc import ABC, abstractmethod

class abstact(ABC):
    @abstractmethod
    def parameter(self):
        pass
    
    @abstractmethod
    def parameter2(self):
        pass
    
# Now if you inherit abstract class, you must implement the abstract methods

