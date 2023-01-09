class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"i am{self.name} and i am {self.age} years old")
    def speak(self):
        print("I don't know what I say")
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    
    def speak(self): 
        print("Bark")
    
class Fish(Pet):
    pass
p = Pet("Monty", 12)
p.show()

c = Cat("Billa", 10, "Brown")
c.show()

d = Dog("jimmy",22)
d.speak()

# f = Fish("Bubbles", 13)
# f.speak()