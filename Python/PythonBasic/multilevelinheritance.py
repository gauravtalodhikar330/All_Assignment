class Animal:
    def eat(self):
        print("Eating....")
class Dog(Animal):
    def bark(self):
        print("barking...")
class BabyDog(Dog):
    def  weep(self):
        print("weeping...")

d = BabyDog()
d.eat()
d.bark()
d.weep()
   