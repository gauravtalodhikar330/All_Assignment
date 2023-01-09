from unicodedata import name


a="Hello"
b="Python"
print(a+" "+b)

length = len(a)
print(length)

#To reverse the String
i=0 
for n in  range(-1,(-length-1),-1):
    print(a[i],"\t",a[n])
    i+=1

# more than one string print same 
print("Python " * 5)

#membership oprator in python string 

str1 = "Python"
str2 = "Python Program"
str3 = "user"

print('Examples in operator ')
print(str1 in str2)
print(str1 in str3)
print(str2 in  str3)

print()

print(str1 not in str2)
print(str1 not in str3)
print(str2 not in str3)

#String relation operator 
print("Relationship operator ")
# <, >, >=, <=, !=, 
print("Python"=="Python")
