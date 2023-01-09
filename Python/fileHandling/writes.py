# rb for read binary
# for image copy to the text file

with open('text.txt', 'r') as rf:
    # f.write('Test')
    with open('text_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# for copy the file in another file 

with open('image.jpg', 'rb') as rf:
    # f.write('Test')
    with open('image_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)

# Instide of line by line 
with open('text.txt', 'r') as rf:
    # f.write('Test')
    with open('text_copy1.txt', 'w') as wf:
        chunk_size = 2096
        rf_chunk = rf.read(chunk_size)
        