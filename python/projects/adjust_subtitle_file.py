import re
import os

FRAME_IN_SEC = 30

def add_to_frame(frame_count, rate):
    '''
        Delay or hush seconds.
        The argument seconds allows first decimal. 
    '''
    # return seconds * FRAME_IN_SEC + frame_count
    return frame_count * rate

def get_rate_transfer_func(rate):
    def result_func(the_value):
        return int(add_to_frame(int(the_value), rate))
    return result_func

def get_rate_transfer_func2(rate):
    def result_func(the_value):
        return int(int(the_value) * 1.249 - 68.776)
    return result_func

def adjust_one_line(the_line, transfer_func):
    sub_format = re.compile("\{(\d+)\}\{(\d+)\}(.+)")
    def replace_func(m):
        start_frame = transfer_func(m.group(1))
        end_frame = transfer_func(m.group(2))
        return "{{{0}}}{{{1}}}{2}".format(start_frame, end_frame, m.group(3))
    return re.sub(sub_format, replace_func, the_line)

def adjust_file(file_path, transfer_func):
    with open(file_path) as the_file:
        return [adjust_one_line(the_line, transfer_func) for the_line in the_file]

def add_suffix(file_path, suffix):
    path_pre_part, path_ext_part = os.path.splitext(file_path)
    return path_pre_part + suffix + path_ext_part

def write_lines(file_path, lines):
    with open(file_path, 'w') as the_file:
        for the_line in lines:
            the_file.write(the_line)
    return len(lines)

if __name__ == '__main__':
    from minitest import *

    # with test(adjust_one_line):
    #     line1 = '{2778}{2842}Party hardy was tardy.'
    #     line2 = '{28869}{28914}Go, Dad!' 
    #     transfer_func = get_rate_transfer_func(1.22)
    #     adjust_one_line(line1, transfer_func).must_equal('{3389}{3467}Party hardy was tardy.')
    #     adjust_one_line(line2, transfer_func).must_equal('{35220}{35275}Go, Dad!')

    # with test(add_suffix):
    #     file_path = '/Users/colin/123.sub'
    #     add_suffix(file_path, '_changed').must_equal('/Users/colin/123_changed.sub')

    def main():
        file_path = '/Users/colin/Movies/Simpsons/The Simpsons - S02E04 - Treehouse Of Horror I.EN.sub'
        transfer_func = get_rate_transfer_func2(1.2465)
        lines = adjust_file(file_path, transfer_func)
        # changed_file_path = add_suffix(file_path, '_changed')
        changed_file_path = file_path
        write_lines(changed_file_path, lines)
        file_path.pl()
        "done".pl()
    main()


