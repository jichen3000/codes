import time
def tail(file_path, interval_sec=1, from_what= 2):
    ''' 
        from_what: 
            0 measures from the beginning of the file,   
            1 uses the current file position, 
            2 uses the end of the file as the reference point.  
    '''

    with open(file_path) as file_:
        # Go to the end of file
        file_.seek(0, from_what)
        while True:
            # curr_position = file_.tell()
            line = file_.readline()
            if not line:
                # file_.seek(curr_position)
                time.sleep(interval_sec)
            else:
                yield line

if __name__ == '__main__':
    from minitest import *

    with test(tail):
        for line in tail("test.txt"):
            if line != "all *** end":
                print(line)
            else:
                break