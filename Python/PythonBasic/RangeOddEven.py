lower=int(input("Enter the Number : "))
upper=int(input("Enter Greatest Number : "))
for i in range(lower,upper+1):
    if(i%2!=0):
        print("Odd Number :", i)

for i in range(lower,upper+1):
    if(i%2==0):
        print("Even Number ", i)
