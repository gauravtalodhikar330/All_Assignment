

class Parrot:
    #Attribute
    species = "bird"
    #instance Attribute
    def _init_(self, name, age):
        self.name = name
        self.age = age

#instantiate the class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes  
print("blu is a {}".format(blu.__class__.species))
print("woo is also a {}".format(woo.__class__.species))

#Acces the instance Attributes 

print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))