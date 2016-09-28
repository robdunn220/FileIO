from sys import argv

script, filename = argv

file_lines = open(filename)

count = 0

for i in file_lines:
    count += 1

print "There are %s lines in the text file" % (count)
