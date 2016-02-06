# forloop

# read the lines from the file
fh = open('lines.txt')
for line in fh.readlines():
    print(line) # print(line, end='') will get rid of spaces
