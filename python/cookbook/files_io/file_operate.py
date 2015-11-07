with open('test.txt', 'rt') as f: 
    for line in f:
        print line

# print('ACME', 50, 91.5, sep=',')

# write to a file that doesn't already exist
# with open('test.txt', 'xt') as f: 
#     f.write("mm\n")
import os
import time
print time.ctime(os.path.getmtime('/etc/passwd'))