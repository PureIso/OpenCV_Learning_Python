"""
Main Module
Record webcam - MacOS X
"""
from __builtin__ import ord
from datetime import datetime
import cv2
import os

VIDEO_DIRECTORY = os.path.join(os.path.dirname(__file__), "saved_videos/")


def main():
    try:
        cv2.namedWindow("Video Window", cv2.WINDOW_NORMAL)
        video_capture = cv2.VideoCapture(0)

        frames_per_seconds = 15
        size = (int(video_capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
                int(video_capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
        four_cc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
        is_color = True
        file_name = str(datetime.now().hour) + '_' + \
                    str(datetime.now().minute) + '_' + \
                    str(datetime.now().second) + '_video.mov'

        writer = cv2.VideoWriter()
        writer.open(VIDEO_DIRECTORY + '/' + file_name, four_cc, frames_per_seconds, size, is_color)

        while video_capture.isOpened():
            ret, frame = video_capture.read()
            writer.write(frame)
            cv2.imshow('Video Window', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release everything if job is finished
        video_capture.release()
        writer.release()
        cv2.destroyAllWindows()

    except Exception, ex:
        print(str(ex))


if __name__ == "__main__":
    main()
