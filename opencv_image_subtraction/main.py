"""
Main Module
Load image using open cv
"""
import cv2


def main():
    # Load an color image in gray scale
    image = cv2.imread('number_1.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
    image_2 = cv2.imread('number_13.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
    image_subtracted = image - image_2
    cv2.namedWindow("Image Window", cv2.WINDOW_NORMAL)
    cv2.imshow('image', image_subtracted)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
