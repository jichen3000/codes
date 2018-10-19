import sys
import time

def main(count, interval_seconds = 1):
    for i in range(count):
        print("i: ", i)
        sys.stdout.flush()
        time.sleep(interval_seconds)


interval_seconds = int(sys.argv[2]) if len(sys.argv) > 2 else 1
main(int(sys.argv[1]))