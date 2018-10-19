# from subprocess import call

# it will not concurrence
# [ call(["python", "my_command.py"]) for i in range(10)]

# it will concurrence
import subprocess, os
# with open("1.log","w") as out:
#     p = [subprocess.Popen(["python", "my_command.py", str(i)], stdout=out,stderr=out) for i in range(10)]
# print p
# print "processs ok"

if __name__ == '__main__':
    from minitest import *

    with test(subprocess.check_output):
        subprocess.check_output(["echo", "Hello"]).must_equal(
            b"Hello\n")
        subprocess.check_output("echo Hello".split(" ")).must_equal(
            b"Hello\n")
        (lambda : subprocess.check_output("ls some".split(" "))).must_raise(
            subprocess.CalledProcessError,"Command '['ls', 'some']' returned non-zero exit status 1.")
        
        # shell=True, will cause command injection
        subprocess.check_output(
                "ls non_existent_file; exit 0",
                stderr=subprocess.STDOUT,
                shell=True).must_equal(
                b"ls: non_existent_file: No such file or directory\n")

        # best practice
        try:
            subprocess.check_output("ls some".split(" "),stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            e.returncode.must_equal(1)
            e.output.must_equal(b"ls: some: No such file or directory\n")        
        # result.p()
        # subprocess.check_output
        # subprocess.check_output("sudo iwconfig wlan0 rate 12Mb".split(" "))

    with test(subprocess.call):
        # directly output on 
        subprocess.call(["echo", "Hello"]).must_equal(0)
        subprocess.call("exit 1", shell=True).must_equal(1)

        # aa = subprocess.Popen(["echo", "Hello"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)