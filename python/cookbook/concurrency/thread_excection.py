from threading import Thread, current_thread
from time import sleep

class MyException(Exception):
    pass

def in_thread():
    print("in_thread")
    sleep(1)
    current_thread().has_error = True
    # raise MyException("somesome")


def main():
    cur_thread = Thread(target=in_thread)
    try:
        cur_thread.start()
        for i in range(4):
            if hasattr(cur_thread,"has_error"):
                break
            print(".")
            sleep(0.5)
    except Exception as e:
        print(e)
        return

main()
