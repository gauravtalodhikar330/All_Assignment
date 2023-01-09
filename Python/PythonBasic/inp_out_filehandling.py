# data =  open("data.txt", "wb")
# print("Name of the file: ",data.name)
# print("Closed or not: ",data.closed)
# print("Open mode: ", data.mode)
# data.close()

#Read and Writing file

data = open("data1.txt", "w")
data.write("Welcome to GS Lab")
print("done")
data.close()

#Read how much we want 

data = open("data3.txt", "r+")
file_data = data.read(18)
# full_data = data.read()
print(file_data)
# print(full_data)
data.close()


#Renaming and Deleting the file 

#for Rename
import os
# os.rename('data.txt', 'my_data.txt')

#for Removing the file
os.remove('my_data.txt')