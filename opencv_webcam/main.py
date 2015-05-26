"""
Main Module
Load video using open cv
"""
from __builtin__ import ord
from datetime import datetime
import cv2
import os

IMAGES_DIRECTORY = os.path.join(os.path.dirname(__file__), "saved_images/")


def main():
    try:
        # Load an color image
        cv2.namedWindow("Video Window", cv2.WINDOW_NORMAL)
        video_capture = cv2.VideoCapture(0)
        gray_view = False
        while video_capture.isOpened():
            # Capture video frame by frame
            ret, frame = video_capture.read()

            if gray_view:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Video Window', frame)

            # x64 machine - remove the & 0xFF for x86
            # 0 -> wait indefinitely for a key stroke and 1 -> else
            key = cv2.waitKey(1) & 0xFF
            if key == 27 or key == ord('q'):  # wait for ESC key to exit
                video_capture.release()
                cv2.destroyAllWindows()
            elif key == ord('s'):  # save and exit
                file_name = str(datetime.now().hour) + '_' + \
                            str(datetime.now().minute) + '_' + \
                            str(datetime.now().second) + '_image.png'
                cv2.imwrite(IMAGES_DIRECTORY + '/' + file_name, frame)
                cv2.destroyAllWindows()
            elif key == ord('g'):     # Display to grey frames or coloured
                if gray_view:
                    gray_view = False
                else:
                    gray_view = True

    except Exception, ex:
        print(str(ex))


if __name__ == "__main__":
    main()
