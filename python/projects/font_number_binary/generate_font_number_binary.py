import cv2
import numpy
import cv2_helper

import os


BLACK = cv2_helper.BLACK
WHITE = cv2_helper.WHITE

IMG_SIZE = 32

def generate_number_images():
    font_families =["Antiqua", "Arial", "Blackletter", "Calibri", 
                    "Comic Sans", "Courier", "Cursive", "Decorative", 
                    "Fantasy", "Fraktur", "Frosty", "Garamond", 
                    "Georgia", "Helvetica", "Impact", "Minion", 
                    "Modern", "Monospace", "Palatino", "Roman", 
                    "Sans-serif", "Serif", "Script", "Swiss", 
                    "Times", "Times New Roman", "Verdana"]
    font_family_names =   ["antiqua", "arial", "blackletter", "calibri", 
                            "comic_sans", "courier", "cursive", "decorative", 
                            "fantasy", "fraktur", "frosty", "garamond", 
                            "georgia", "helvetica", "impact", "minion", 
                            "modern", "monospace", "palatino", "roman", 
                            "sans_serif", "serif", "script", "swiss", 
                            "times", "times_new_roman", "verdana"]
    # font_family_names =   ["verdana"]
    font_styles = ["normal", "italic"]
    font_weights = ["normal", "bold"]
    source_path = './images'
    source_suffix = '.png'
    target_path = './number_images'
    target_suffix = '.dataset'

    types = tuple(style+'_'+weight for style in font_styles for weight in font_weights)

    result_list = []
    for family_name in font_family_names:
        file_name = os.path.join(source_path, family_name+source_suffix)
        if os.path.isfile(file_name):
            gray_pic = cv2.imread(file_name, 0)
            number_binary_list = find_font_number_binary_ragions(gray_pic)
            result_list += save_binary_list(number_binary_list, 
                family_name, target_path, target_suffix, types)
    return result_list


def save_binary_list(number_binary_list, family_name, target_path, target_suffix, types):
    type_count = len(types)
    number_count = int(len(number_binary_list) / type_count)
    result_list = []
    for index, cur_type in enumerate(types):
        for num in range(number_count):
            num_file_name = os.path.join(target_path, 
                "_".join((str(num), cur_type, family_name))+target_suffix )
            cv2_helper.save_binary_pic_txt(
                num_file_name, number_binary_list[index*number_count + num])
            result_list.append(num_file_name)
    return result_list

def remove_border(pic_array):
    return cv2_helper.clip_array_by_x_y_count(pic_array, clip_x_count=2, clip_y_count=2)

def remove_margin(pic_array):
    new_rect = cv2_helper.cal_nonzero_rect_as_pic_ratio(pic_array)
    return cv2_helper.get_rect_ragion_with_rect(pic_array, new_rect)
    
def enlarge(pic_array):
    return cv2.resize(pic_array, (IMG_SIZE, IMG_SIZE), interpolation=cv2.INTER_CUBIC);


def check_size(pic_array):
    if pic_array.shape != (IMG_SIZE, IMG_SIZE):
        raise Exception("Wrong row and col count: %d, %d"%pic_array.shape)
    return True

def find_font_number_binary_ragions(pic_array):
    '''
    '''
    threshed_pic_array = cv2_helper.threshold_white_with_mean_percent(gray_pic)
    numbers_rectangles = find_numbers_rectangles(threshed_pic_array)
    numbers_rectangles = reversed(numbers_rectangles)

    binary_pic = cv2_helper.transfer_values(threshed_pic_array, {BLACK:0, WHITE:1})
    # numpy.count_nonzero(binary_pic).pp()

    number_binary_ragions = map(lambda c: cv2_helper.get_rect_ragion_with_contour(binary_pic, c),
        numbers_rectangles)

    number_binary_ragions = map(remove_border, number_binary_ragions)

    number_binary_ragions = map(remove_margin, number_binary_ragions)

    number_binary_ragions = map(enlarge, number_binary_ragions)

    map(check_size, number_binary_ragions)

    # number_binary_ragions[0].pp()
    return number_binary_ragions

def find_numbers_rectangles(threshed_pic_array):
    def is_numbers_rectangle(contour):
        return contour.shape[0] == 4 and cv2.arcLength(contour, True) > 40

    return cv2_helper.find_contours(threshed_pic_array, 
        filter_func=is_numbers_rectangle, accuracy_percent_with_perimeter=0.00001)


def main():
    generate_number_images()

if __name__ == '__main__':
    from minitest import *

    # main()

    ORIGINAL_IMAGE_NAME = './images/antiqua.png'
    gray_pic = cv2.imread(ORIGINAL_IMAGE_NAME, 0)
    color_pic = cv2.imread(ORIGINAL_IMAGE_NAME)

    with test("find_numbers_rectangles"):
        threshed_pic_array = cv2_helper.threshold_white_with_mean_percent(gray_pic)
        numbers_rectangles = find_numbers_rectangles(threshed_pic_array)
        numbers_rectangles.size().must_equal(40)

        # cv2_helper.show_contours_in_pic(color_pic,numbers_rectangles)

        # other_pic = cv2.imread('./images/verdana.png', 0)
        # number_binary_ragions = find_font_number_binary_ragions(other_pic)
        # threshed_pic_array = cv2_helper.threshold_white_with_mean_percent(gray_pic)
        # numbers_rectangles = find_numbers_rectangles(threshed_pic_array)
        # numbers_rectangles.size().must_equal(40)
        # cv2_helper.show_contours_in_pic(cv2.imread('./images/verdana.png'),numbers_rectangles)


    with test("find_font_number_binary_ragions"):
        test_file_path = 'test_resources/test.dataset'
        number_binary_ragions = find_font_number_binary_ragions(gray_pic)
        cv2_helper.save_binary_pic_txt(test_file_path, number_binary_ragions[0])
        numpy.savetxt(test_file_path, number_binary_ragions[0], fmt='%d', delimiter='')

        # other_pic = cv2.imread('./images/verdana.png', 0)
        # number_binary_ragions = find_font_number_binary_ragions(other_pic)
        # cv2_helper.save_binary_pic_txt(test_file_path, number_binary_ragions[0])
        pass

