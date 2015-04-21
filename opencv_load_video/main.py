"""
Main Module
Load video using open cv
"""
import cv2
import os

RESOURCES_DIRECTORY = os.path.join(os.path.dirname(__file__), "resources/")


def main():
    try:
        # Load an color image
        cv2.namedWindow("Video Window", cv2.WINDOW_NORMAL)
        video_capture = cv2.VideoCapture(RESOURCES_DIRECTORY+'Wildlife_512kb.mp4')
        while video_capture.isOpened():
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cv2.imshow('Video Window', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()
    except Exception, ex:
        print(str(ex))


if __name__ == "__main__":
    main()