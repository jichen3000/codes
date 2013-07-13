from subprocess import call

# it will not concurrence
# [ call(["python", "my_command.py"]) for i in range(10)]

# it will concurrence
import subprocess, os
with open("1.log","w") as out:
    p = [subprocess.Popen(["python", "my_command.py", str(i)], stdout=out,stderr=out) for i in range(10)]
print p
print "processs ok"