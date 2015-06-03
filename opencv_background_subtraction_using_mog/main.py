import numpy as np
import cv2

def main():
    cap = cv2.VideoCapture(0)

    #The class implements the Gaussian mixture model background subtraction described in
    #http://www.zoranz.net/Publications/zivkovic2004ICPR.pdf.
    fgbg = cv2.BackgroundSubtractorMOG2()

    while(1):
        ret, frame = cap.read()

        fgmask = fgbg.apply(frame)

        cv2.imshow('frame',fgmask)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
