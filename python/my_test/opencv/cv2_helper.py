import cv2

class Image(object):
    @staticmethod
    def resize_keeping_ratio_by_height(the_image, height=700):
        width = float(height) / the_image.shape[0]
        dim = (int(the_image.shape[1] * width), height)
        return cv2.resize(the_image, dim, interpolation = cv2.INTER_AREA)
