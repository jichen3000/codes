import fileinput

def main(files=None):
    the_input = fileinput.input(files=files)
    line1 = the_input.next()
    line2 = the_input.next()
    count = int(line1)
    time_list = map(int, line2.split(" "))
    print time_list[465:]    

# test2.txt 465


if __name__ == '__main__':
    from minitest import *

    with test(main):
        main("test2.txt").p()