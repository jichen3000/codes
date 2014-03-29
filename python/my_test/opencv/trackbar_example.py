import cv2
import numpy

def simple_one():
    def nothing(x):
        print x

    # Create a black image, a window
    img = numpy.zeros((300,512,3), numpy.uint8)
    cv2.namedWindow('image')

    # create trackbars for color change
    cv2.createTrackbar('R','image',0,255,nothing)
    cv2.createTrackbar('G','image',0,255,nothing)
    cv2.createTrackbar('B','image',0,255,nothing)

    # create switch for ON/OFF functionality
    switch = 'ON / OFF'
    cv2.createTrackbar(switch, 'image',0,1,nothing)

    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        # escap
        if k == 27:
            break

        # get current positions of four trackbars
        r = cv2.getTrackbarPos('R','image')
        g = cv2.getTrackbarPos('G','image')
        b = cv2.getTrackbarPos('B','image')
        s = cv2.getTrackbarPos(switch,'image')

        if s == 1:
            img[:] = 0
        else:
            img[:] = [b,g,r]


def use_callback():
    window_name = 'image'
    def refresh_image(x=None):
        r = cv2.getTrackbarPos('R',window_name)
        g = cv2.getTrackbarPos('G',window_name)
        b = cv2.getTrackbarPos('B',window_name)
        img[:] = [b,g,r]
        cv2.imshow(window_name, img)
        cv2.imshow('123', img)
        cv2.moveWindow('123', 512, 0)

    img = numpy.zeros((300,512,3), numpy.uint8)
    cv2.namedWindow(window_name)

    cv2.createTrackbar('R',window_name,0,255,refresh_image)
    cv2.createTrackbar('G',window_name,0,255,refresh_image)
    cv2.createTrackbar('B',window_name,0,255,refresh_image)

    refresh_image()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    from minitest import *
    with test("simple_one"):
        # simple_one()
        pass

    with test("use_callback"):
        use_callback()
        pass