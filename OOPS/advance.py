class Magic:
    def __init__(self, name):
        self.name = name  # Initialize with name

    def __str__(self):
        return f"Magic name: {self.name}"  # String representation

    def __repr__(self):
        return f"Magic({self.name!r})"  # Official representation

    def __add__(self, other):
        return Magic(f"{self.name} + {other.name}")  # Add two Magic objects

    def __eq__(self, other):
        return isinstance(other, Magic) and self.name == other.name  # Equality check

    def __lt__(self, other):
        return self.name < other.name  # Less than

    def __le__(self, other):
        return self.name <= other.name  # Less than or equal

    def __gt__(self, other):
        return self.name > other.name  # Greater than

    def __ge__(self, other):
        return self.name >= other.name  # Greater than or equal

    def __hash__(self):
        return hash(self.name)  # Hash for using in sets/dicts

    def __len__(self):
        return len(self.name)  # Length of name

    def __getitem__(self, key):
        return self.name[key]  # Get character at index

    def __setitem__(self, key, value):
        self.name = self.name[:key] + value + self.name[key+1:]  # Set character at index

    def __delitem__(self, key):
        self.name = self.name[:key] + self.name[key+1:]  # Delete character at index

    def __call__(self, *args, **kwargs):
        return f"Magic {self.name} called with {args} {kwargs}"  # Callable object

    def __bool__(self):
        return bool(self.name)  # Truthiness based on name

obj = Magic("Fireball")
obj2 = Magic("Lightning")

# print(obj + obj2)      # Uses __add__
# print(obj)             # Uses __str__
# print(repr(obj))       # Uses __repr__
# print(obj == obj2)     # Uses __eq__
# print(obj < obj2)      # Uses __lt__
# print(len(obj))        # Uses __len__
# print(obj[0])          # Uses __getitem__
# obj[0] = "X"           # Uses __setitem__
# print(obj)
# del obj[0]             # Uses __delitem__
# print(obj)
# print(obj())           # Uses __call__
# print(bool(obj))       # Uses __bool__


def decorate(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Decorated: {result}"
    return wrapper

class Animal:
    @decorate
    def show(self):
        print("Animal is showing")

# print(Animal().show())
# *args = [1, 2, 3]                 - Only multiple arguments
# **kwargs = {'a': 1, 'b': 2}       - Key and Value arguments


even_list = [i for i in range(10) if i % 2 == 0]
even_dict = {x: x*2 for x in range(10) if x % 2 == 0}
even_set = {x*x for x in range(10) if x % 2 == 0}
# print(even_list, even_dict, even_set)  # List, Dictionary, and Set comprehensions


addition = lambda a,b : a + b
evenCheck = lambda x : "Even" if x % 2 == 0 else "Odd"
# print(addition(10, 30))
# print(evenCheck(98))


