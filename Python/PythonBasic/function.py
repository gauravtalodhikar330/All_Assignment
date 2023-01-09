from curses.ascii import isalpha


s = "HappyHoli"
print(s.capitalize())

print(s.count('e'))
print(s.index('i'))
print(s.find('n'))

#to check the string contatin only alphabatic character or not

print(s.isalpha())
print(s.isalnum())
print(s.isdigit())

#to check the cases are lower 
print(s.islower())
print(s.isnumeric())
print(s.isspace())

#lower and upper coversion

print(s.lower())
print(s.upper())

#maximum alphabetic charecter
print(max(s))

print(min(s))
print(s.replace('Happy', 'Hello'))