import shutil
import os



def mkdir_p(a_path):
    if (os.path.exists(a_path) and os.path.isdir(a_path)) or os.path.isfile(a_path):
        return
    return os.makedirs(a_path)
        

shutil.copy2(__file__, "d:\\share\\")
print 'second:'
shutil.copy2(__file__, "d:\\share\\")

print "mkdir_p"
file_path = "d:\\tmp\\"

mkdir_p(file_path)
mkdir_p(file_path)

print "ok"