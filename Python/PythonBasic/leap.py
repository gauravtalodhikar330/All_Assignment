year = int(input("Enter the  Year"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("Entered Year is Leap Year")
else:
    print("Entered year is Not a Leap Year")