with open('text.txt', 'r') as f:

    # '''for line in  f:
    #     print(line, end='')
    # '''

    
    # f_contents = f.readlines()
    
    # f_contents = f.readline()
   
    # '''size_to_read = 30
    # f_contents = f.read(size_to_read)
    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)
    # '''

    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    f_contents = f.read(size_to_read)
    print(f_contents)