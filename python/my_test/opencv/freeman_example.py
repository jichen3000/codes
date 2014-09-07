import cv2

from picture_sudoku.cv2_helpers.image import Image
from picture_sudoku.cv2_helpers.display import Display

from picture_sudoku.helpers.common import Resource

if __name__ == '__main__':
    from minitest import *

    with test("show freeman"):
        the_pic_path = Resource.get_path('test/pic16_no05_real8_cal6.dataset')
        the_image = Image.load_from_txt(the_pic_path)
        # contours,not_use = cv2.findContours(the_image.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        # # Display.contours(the_image, contours)
        # contours.ppl()

        cv2.CHAIN_APPROX_NONE.pl()
        cv2.CHAIN_APPROX_SIMPLE.pl()
        contours,not_use = cv2.findContours(the_image.copy(),cv2.RETR_LIST,0)
        # Display.contours(the_image, contours)
        contours.ppl()
