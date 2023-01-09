from traceback import print_tb


def evenOdd(x):
    if(x%2 == 0):
        print("even")
    else :
        print("odd")

evenOdd(6)

def cube(x):
    y = x*x*x;
    return y

z = cube(5)
print(z)


def  emp_data(name, emp_id,age,company = "self employee"):
    print("Detail of : ",name)
    print("Emp_Id : ", emp_id)
    print("Age : ",age)
    print("Company : ",company)

emp_data("vishal",101,24,"abc Technology")

emp_data("Rakesh",102,26)


#Global & Local variable

x = 50
def print_data():
    x = 5
    y = 10
    print("(x,y):(",x,",",y,")")

print_data()
print("Global x : ",x)
#y is local variable that why its throws name error
print("Local y : ",y)
 