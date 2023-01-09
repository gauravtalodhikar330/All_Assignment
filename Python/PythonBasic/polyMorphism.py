# Method Overloading 
# def product(a, b):
#     p = a * b
#     print(p)

# def cube(a, b, c):
#     p = a*b*c
#     print(p)

# Method Overriding 

class Parent:
    def  my_method(self):
        print("Calling the parent method")

class Child(Parent):
    def my_method(self):
        print('Calling from child')
c = Child()
c.my_method()