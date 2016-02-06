# exceptions
# This is an exercise file from Python 3 Essential Training on lynda.com


try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)
except IOError as e:
    print("something bad happend ({})".format(e))

print("after badness")
