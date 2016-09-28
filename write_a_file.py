my_file = open('my_file.txt', 'w')


for i in range(10):
    txt_to_add = raw_input("Please enter something to add to the file: ")
    my_file.write(txt_to_add + "\n")

my_file.close()
