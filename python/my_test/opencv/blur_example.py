import cv2
import numpy

from picture_sudoku.helpers import cv2_helper

MAX_KERNEL_LENGTH = 31

''' 
    the methods which name starts with "__blur_by_" will be invoked when trackbar changes.
    And when you add this type method, the app will show a image for you.
    The __controle__ is the control trackbar.

'''

BLUR_PREFIX = '__blur_by_'
CONTROL_NAME = '__controle__'

def __blur_by_median(the_image, point_value):
    return cv2.medianBlur(the_image, point_value, 0)

def __blur_by_simple(the_image, point_value):
    return cv2.blur(the_image, (point_value,point_value))

def __blur_by_gaussian(the_image, point_value):
    return cv2.GaussianBlur(the_image, (point_value,point_value), 0)

def __blur_by_bilateralFilter(the_image, point_value):
    return cv2.bilateralFilter(the_image, point_value, point_value*2, point_value/2)

def __controle__(the_position, the_image, control_window_name):
    all_names = filter(lambda name: name.startswith(BLUR_PREFIX), globals())
    for index, name in enumerate(all_names):
        window_name = name[len(BLUR_PREFIX):]
        method = globals()[name]
        cv2.setTrackbarPos('blur', window_name, the_position)
        refresh_image(the_position, the_image, window_name, method)

    point_value = get_odd_value(the_position)
    draw_text(the_image, 'blurring value: '+str(point_value))
    cv2.imshow(control_window_name, the_image)



def refresh_image(the_position, the_image, window_name, blurring_func):
    point_value = get_odd_value(the_position)
    blured_image = blurring_func(the_image, point_value)
    draw_text(blured_image, 'blurring value: '+str(point_value))
    cv2.imshow(window_name, blured_image)


def show_blurring(the_image, window_name, index, blurring_func, control_func=None):
    cv2.namedWindow(window_name)
    window_name.pp()
    if control_func:
        call_back = lambda the_position: control_func(the_position, the_image, window_name)
    else:
        call_back = lambda the_position: refresh_image(the_position, the_image, window_name, blurring_func)
    cv2.createTrackbar('blur', window_name, 0, MAX_KERNEL_LENGTH, call_back)
    call_back(0)
    cv2.moveWindow(window_name, the_image.shape[1]*index, 0)

def show_all(the_image):
    all_names = filter(lambda name: name.startswith(BLUR_PREFIX), globals())
    for index, name in enumerate(all_names):
        window_name = name[len(BLUR_PREFIX):]
        method = globals()[name]
        show_blurring(the_image, window_name, index, blurring_func=method)

    control_name = filter(lambda name: name.startswith(CONTROL_NAME), globals())[0]
    show_blurring(the_image, control_name, len(all_names), blurring_func=None, control_func=globals()[control_name])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def draw_text(the_image, the_text):
    cv2.putText(the_image, the_text, (20,20), cv2.FONT_HERSHEY_PLAIN, 1.0, (0,255,0))

def get_odd_value(the_value):
    odd_value = the_value
    if odd_value % 2 == 0:
        odd_value += 1
    return odd_value



if __name__ == '__main__':
    from minitest import *
    image_path = './original.jpg'
    color_image = cv2.imread(image_path)
    gray_image = cv2.imread(image_path, 0)
    color_image = cv2_helper.resize_with_fixed_height(color_image)
    gray_image = cv2_helper.resize_with_fixed_height(gray_image)

    with test("blurring"):
        # show_simple_blurring(color_image)
        show_all(color_image)
        pass

