try:
    fh = open("text.txt", "w")
    fh.write("This is my Text File created with  python exception handling ")
except IOError:
    print("Can not find the file and can not reading the data ")
else:
    print("Content Written Succesfully")
    fh.close()