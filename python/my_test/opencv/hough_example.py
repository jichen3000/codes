import cv2
import numpy

from picture_sudoku.helpers import cv2_helper

''' 
    the methods which name starts with "__perform_by_" will be invoked when trackbar changes.
    And when you add this type method, the app will show a image for you.
    The __controle__ is the control trackbar.

'''

'''
    this is not good for sudoku.
'''

PERFORM_PREFIX = '__perform_by_'
CONTROL_NAME = '__controle__'

TRACKBAR_1 = 'canny_low_threshold'
TRACKBAR_2 = 'HoughLines_threshold'
TRACKBAR_1_MAX = 100
TRACKBAR_2_MAX = 100

def __perform_by_normal_line(the_image, bar_value_1, bar_value_2):
    gray_image = cv2.cvtColor(the_image,cv2.COLOR_BGR2GRAY)
    canny_low_threshold = bar_value_1+30
    edges = cv2.Canny(gray_image, canny_low_threshold, (canny_low_threshold)*4, 3);
    # cv2.convertScaleAbs(edges)
    color_image = the_image.copy()

    lines = cv2.HoughLines(edges, rho=1, theta=numpy.pi/180, threshold= bar_value_2+100)

    for rho, theta in lines[0]:
        (rho, theta).pp()
        cos_theta = numpy.cos(theta)
        sin_theta = numpy.sin(theta)
        x0 = cos_theta * rho
        y0 = sin_theta * rho
        point0 = (int(numpy.around(x0 + 1000*(- sin_theta))),  int(numpy.around(y0 + 1000*( cos_theta))))
        point1 = (int(numpy.around(x0 - 1000*(- sin_theta))),  int(numpy.around(y0 - 1000*( cos_theta))))
        cv2.line(color_image, point0, point1, (0,0,255), thickness=3)
    return color_image

def __perform_by_canny(the_image, bar_value_1, bar_value_2):
    gray_image = cv2.cvtColor(the_image,cv2.COLOR_BGR2GRAY)
    canny_low_threshold = bar_value_1+30
    edges = cv2.Canny(gray_image, canny_low_threshold, (canny_low_threshold)*4, 3);
    return cv2.convertScaleAbs(edges)


def __controle__(the_position, the_image, control_window_name):
    bar_value_1, bar_value_2 = get_parameters(control_window_name)

    all_names = filter(lambda name: name.startswith(PERFORM_PREFIX), globals())
    for index, name in enumerate(all_names):
        window_name = name[len(PERFORM_PREFIX):]
        method = globals()[name]
        set_parameters(window_name, bar_value_1, bar_value_2)
        refresh_image(the_position, the_image, window_name, method)

    draw_text(the_image, gen_message(bar_value_1, bar_value_2))
    cv2.imshow(control_window_name, the_image)


def gen_message(bar_value_1, bar_value_2):
    return "%s: %s, %s: %s" % (TRACKBAR_1, str(bar_value_1), TRACKBAR_2, str(bar_value_2))

def get_parameters(window_name):
     return (cv2.getTrackbarPos(TRACKBAR_1, window_name), 
            cv2.getTrackbarPos(TRACKBAR_2, window_name))

def set_parameters(window_name, value1, value2):
     return (cv2.setTrackbarPos(TRACKBAR_1, window_name, value1), 
            cv2.setTrackbarPos(TRACKBAR_2, window_name, value2))

def refresh_image(the_position, the_image, window_name, perform_func):
    bar_value_1, bar_value_2 = get_parameters(window_name)
    # kernel = numpy.ones((bar_value_1, bar_value_1), dtype=numpy.float32) / (bar_value_1**2)
    performed_image = perform_func(the_image, bar_value_1, bar_value_2)


    draw_text(performed_image, gen_message(bar_value_1, bar_value_2))
    cv2.imshow(window_name, performed_image)


def show_window(the_image, window_name, index, perform_func, control_func=None):
    cv2.namedWindow(window_name)
    if control_func:
        call_back = lambda the_position: control_func(the_position, the_image, window_name)
    else:
        call_back = lambda the_position: refresh_image(the_position, the_image, window_name, perform_func)
    cv2.createTrackbar(TRACKBAR_1, window_name, 0, TRACKBAR_1_MAX, call_back)
    cv2.createTrackbar(TRACKBAR_2, window_name, 0, TRACKBAR_2_MAX, call_back)
    call_back(0)
    cv2.moveWindow(window_name, the_image.shape[1]*index, 0)

def show_all(the_image):
    all_names = filter(lambda name: name.startswith(PERFORM_PREFIX), globals())
    for index, name in enumerate(all_names):
        window_name = name[len(PERFORM_PREFIX):]
        method = globals()[name]
        show_window(the_image, window_name, index, perform_func=method)

    control_name = filter(lambda name: name.startswith(CONTROL_NAME), globals())[0]
    show_window(the_image, control_name, len(all_names), perform_func=None, control_func=globals()[control_name])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def draw_text(the_image, the_text):
    cv2.putText(the_image, the_text, (20,20), cv2.FONT_HERSHEY_PLAIN, 1.0, (0,255,0))



if __name__ == '__main__':
    from minitest import *

    def main_test(image_path):
        color_image = cv2.imread(image_path)
        gray_image = cv2.imread(image_path, 0)
        color_image = cv2_helper.resize_with_fixed_height(color_image)
        gray_image = cv2_helper.resize_with_fixed_height(gray_image)
        show_all(color_image)

    with test("blurring"):
        pic_file_path = './original.jpg'
        pic_file_path = '../../../../picture_sudoku/resource/example_pics/sample14.dataset.jpg'
        main_test(pic_file_path)
        # for i in range(1,15):
        #     pic_file_path = '../resource/example_pics/sample'+str(i).zfill(2)+'.dataset.jpg'
        #     main_test(pic_file_path)
        pass

