# Average of in given list 

n=int(input("Enter the number of element to be insert "))
a=[]
for i in range(0,n):
    elem =int(input("Enter the element"))
    a.append(elem)
avg=sum(a)/n
print("Average of element in list is : ", (avg))