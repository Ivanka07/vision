import cv2
import numpy as np
import sys, os
import glob

HOME_DIR = os.environ['HOME']
PATH_TO_VIDEOS = '/fa_data/validation_data/utdalas_videos/'
EXTRACT_IMAGES = '/fa_data/validation_data/utdalas_images/'
VIDEO_FORMAT = '.avi'
image_counter = 0

def get_files():
    files = glob.glob(HOME_DIR + '/' + PATH_TO_VIDEOS + '*' + VIDEO_FORMAT)
    return files

def extract_images():
    global image_counter
    videos = get_files()
    assert len(videos)>0
    for v in videos:
        print('capturing {}'.format(v))
        video_capture = cv2.VideoCapture(v)
        rval, frame = video_capture.read()
        while rval:
            image_path = HOME_DIR + EXTRACT_IMAGES + 'utdallas_{}'.format(image_counter) + '.png'
            print image_path
            cv2.imwrite(image_path, frame)
            image_counter = image_counter + 1
            rval, frame = video_capture.read()

extract_images()
