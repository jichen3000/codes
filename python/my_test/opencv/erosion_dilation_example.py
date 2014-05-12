import cv2
import numpy

import cv2_helper

''' 
    the methods which name starts with "__perform_by_" will be invoked when trackbar changes.
    And when you add this type method, the app will show a image for you.
    The __controle__ is the control trackbar.

'''


PERFORM_PREFIX = '__perform_by_'
CONTROL_NAME = '__controle__'

TRACKBAR_1 = 'ELEMENT'
TRACKBAR_2 = 'KERNEL_SIZE'

def __perform_by_erode(the_image, kernel):
    return cv2.erode(the_image, kernel)

def __perform_by_dilate(the_image, kernel):
    return cv2.dilate(the_image, kernel)


def __controle__(the_position, the_image, control_window_name):
    element_value = cv2.getTrackbarPos(TRACKBAR_1, control_window_name)
    kernel_size_value = cv2.getTrackbarPos(TRACKBAR_2, control_window_name)

    all_names = filter(lambda name: name.startswith(PERFORM_PREFIX), globals())
    for index, name in enumerate(all_names):
        window_name = name[len(PERFORM_PREFIX):]
        method = globals()[name]
        cv2.setTrackbarPos(TRACKBAR_1, window_name, element_value)
        cv2.setTrackbarPos(TRACKBAR_2, window_name, kernel_size_value)
        refresh_image(the_position, the_image, window_name, method)

    cv2.imshow(control_window_name, the_image)



def refresh_image(the_position, the_image, window_name, perform_func):
    element_value = cv2.getTrackbarPos(TRACKBAR_1, window_name)
    kernel_size_value = cv2.getTrackbarPos(TRACKBAR_2, window_name)
    kernel_size_value = 2*kernel_size_value+1
    kernel = cv2.getStructuringElement(element_value, (kernel_size_value, kernel_size_value))
    performed_image = perform_func(the_image, kernel)


    shape_types = {0: 'Rect', 1: 'Cross', 2: 'Ellipse'}
    draw_text(performed_image, 'shape type: '+shape_types[element_value]+" and kernel size: "+str(kernel_size_value))
    cv2.imshow(window_name, performed_image)


def show_window(the_image, window_name, index, perform_func, control_func=None):
    cv2.namedWindow(window_name)
    if control_func:
        call_back = lambda the_position: control_func(the_position, the_image, window_name)
    else:
        call_back = lambda the_position: refresh_image(the_position, the_image, window_name, perform_func)
    cv2.createTrackbar(TRACKBAR_1, window_name, 0, 2, call_back)
    cv2.createTrackbar(TRACKBAR_2, window_name, 0, 21, call_back)
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
    image_path = './original.jpg'
    color_image = cv2.imread(image_path)
    gray_image = cv2.imread(image_path, 0)
    color_image = cv2_helper.Image.resize_keeping_ratio_by_height(color_image)
    gray_image = cv2_helper.Image.resize_keeping_ratio_by_height(gray_image)

    with test("blurring"):
        # show_simple_blurring(color_image)
        show_all(color_image)
        pass

