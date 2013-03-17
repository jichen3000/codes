

foo_file = open("foo.txt","r")

line = foo_file.readline()
print line

for line in foo_file:
    print line

