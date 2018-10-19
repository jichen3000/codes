import subprocess, sys

# it will print to stdout, but will not return the result
# subprocess.call(["python", "test.py", "2"]).pp()

def run_with_print(cmds, buffer_size=1):
    process = subprocess.Popen(cmds, stdout=subprocess.PIPE)


    result = []
    # count = 0
    while True:
        # import ipdb; ipdb.set_trace()
        out = process.stdout.read(buffer_size)
        if out == b'' and process.poll() != None:
            # print("out:",out)
            break
        if out != b'':
            # count += 1
            cur = out.decode('utf-8')
            result += cur,
            sys.stdout.write(cur)
            sys.stdout.flush()
    # count.p()
    return "".join(result)

# run_with_print(["python", "test.py", "10", "2"])
if __name__ == '__main__':
    from minitest import *

    with test(run_with_print):
        run_with_print(["python", "test.py", "10", "2"]).pp()
