import cv2
import numpy

from picture_sudoku.helpers import cv2_helper

''' 
    the methods which name starts with "__perform_by_" will be invoked when trackbar changes.
    And when you add this type method, the app will show a image for you.
    The __controle__ is the control trackbar.

'''


PERFORM_PREFIX = '__perform_by_'
CONTROL_NAME = '__controle__'

TRACKBAR_1 = 'KERNEL_SIZE'

def __perform_by_sobel_x(the_image, kernel):
    the_image = cv2.GaussianBlur(the_image,(3,3),0)
    gray_image = cv2.cvtColor(the_image,cv2.COLOR_BGR2GRAY)
    sobeled_image = cv2.Sobel(gray_image, cv2.CV_16S,1,0, ksize=kernel)
    return cv2.convertScaleAbs(sobeled_image)

def __perform_by_sobel_y(the_image, kernel):
    the_image = cv2.GaussianBlur(the_image,(3,3),0)
    gray_image = cv2.cvtColor(the_image,cv2.COLOR_BGR2GRAY)
    sobeled_image = cv2.Sobel(gray_image, cv2.CV_16S,0,1, ksize=kernel)
    return cv2.convertScaleAbs(sobeled_image)

def __perform_by_Laplacian(the_image, kernel):
    the_image = cv2.GaussianBlur(the_image,(3,3),0)
    gray_image = cv2.cvtColor(the_image,cv2.COLOR_BGR2GRAY)
    sobeled_image = cv2.Laplacian(gray_image, cv2.CV_16S, ksize=kernel)
    return cv2.convertScaleAbs(sobeled_image)


# def __perform_by_Scharr_x(the_image, kernel):
#     the_image = cv2.GaussianBlur(the_image,(3,3),0)
#     gray_image = cv2.cvtColor(the_image,cv2.COLOR_BGR2GRAY)
#     Scharred_image = cv2.Scharr(gray_image, cv2.CV_16S,1,0)
#     return cv2.convertScaleAbs(Scharred_image)

# def __perform_by_Scharr_y(the_image, kernel):
#     the_image = cv2.GaussianBlur(the_image,(3,3),0)
#     gray_image = cv2.cvtColor(the_image,cv2.COLOR_BGR2GRAY)
#     Scharred_image = cv2.Scharr(gray_image, cv2.CV_16S,0,1)
#     return cv2.convertScaleAbs(Scharred_image)


def __controle__(the_position, the_image, control_window_name):
    kernel_size_value = cv2.getTrackbarPos(TRACKBAR_1, control_window_name)

    all_names = filter(lambda name: name.startswith(PERFORM_PREFIX), globals())
    for index, name in enumerate(all_names):
        window_name = name[len(PERFORM_PREFIX):]
        method = globals()[name]
        cv2.setTrackbarPos(TRACKBAR_1, window_name, kernel_size_value)
        refresh_image(the_position, the_image, window_name, method)

    kernel_size_value = 2*kernel_size_value+1
    draw_text(the_image, "kernel size: "+str(kernel_size_value))
    cv2.imshow(control_window_name, the_image)



def refresh_image(the_position, the_image, window_name, perform_func):
    kernel_size_value = cv2.getTrackbarPos(TRACKBAR_1, window_name)
    kernel_size_value = 2*kernel_size_value+1
    # kernel = numpy.ones((kernel_size_value, kernel_size_value), dtype=numpy.float32) / (kernel_size_value**2)
    performed_image = perform_func(the_image, kernel_size_value)


    draw_text(performed_image, "kernel size: "+str(kernel_size_value))
    cv2.imshow(window_name, performed_image)


def show_window(the_image, window_name, index, perform_func, control_func=None):
    cv2.namedWindow(window_name)
    if control_func:
        call_back = lambda the_position: control_func(the_position, the_image, window_name)
    else:
        call_back = lambda the_position: refresh_image(the_position, the_image, window_name, perform_func)
    cv2.createTrackbar(TRACKBAR_1, window_name, 0, 3, call_back)
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
    color_image = cv2_helper.resize_with_fixed_height(color_image)
    gray_image = cv2_helper.resize_with_fixed_height(gray_image)

    with test("blurring"):
        # show_simple_blurring(color_image)
        show_all(color_image)
        pass

