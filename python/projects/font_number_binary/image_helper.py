import numpy

IMG_SIZE = 32

def image_txt_to_lists(file_path, line_len=IMG_SIZE):
    with open(file_path) as the_file:
        result = [int(line[index]) for line in the_file 
            for index in range(line_len)]
    return result


if __name__ == '__main__':
    from minitest import *


    with test("image_txt_to_lists"):
        image_list = image_txt_to_lists(small_number_path)
        # image_list.p()
        image_list.size().must_equal(1024)
        image_list.count(1).must_equal(110)





