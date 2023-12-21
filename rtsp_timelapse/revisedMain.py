import logging
import colorama
from colorama import Fore, Style

import json
import os
import threading
import time
import datetime
import cv2
from random import random
from urllib.parse import urlparse
APP_FOLDER = os.path.realpath(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(APP_FOLDER, 'config.json')

# Initialize colorama
colorama.init()

# Define colors for logging
YELLOW = Style.BRIGHT + Fore.YELLOW
GREEN = Style.BRIGHT + Fore.GREEN
BLUE = Style.BRIGHT + Fore.BLUE
WHITE = Style.BRIGHT + Fore.WHITE
RED = Style.BRIGHT + Fore.RED

# Create a logger
logger = logging.getLogger('timelapse')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s: %(message)s')
# correct the time
ch.setFormatter(formatter)

logger.addHandler(ch)


def open_config():
    with open(CONFIG_PATH) as file:
        return json.load(file)

def start_capture(camera_id, color):

    logger.info('\n -->' + color + 'Thread ID %s...', camera_id)
    global capture_thread_is_active # Read the camera settings from the config file
    camera_settings = config['sources'][camera_id]
    rtsp_url = camera_settings['source']
    interval = int(camera_settings['interval'])
    quality = int(camera_settings['quality'])

    # Initialize the video capture
    try:
        video_src = cv2.VideoCapture(rtsp_url)
        # check folder
        capture_folder = os.path.join(config['images_folder'], camera_id,datetime.datetime.now().strftime("%y%m%d-%H%M%S") )
        if not os.path.exists(capture_folder):
            os.makedirs(capture_folder)
    except:
        logger.info(color + 'Failed to open camera ID %s', camera_id)
        # capture_thread_is_active[camera_id] = False
        return
    
    logger.info(color + 'Starting capture for camera ID %s...', camera_id)

    capture_thread_is_active[camera_id] = True

    # Start capturing images
    start_capture_time = time.time()
    while capture_thread_is_active[camera_id] == True:
        try:
            retrieve, frame = video_src.read()
            # video_src = cv2.VideoCapture(rtsp_url)
            
            # Check if the connection is still valid
            while not video_src or not video_src.isOpened() or not retrieve:
                # The connection is lost, so attempt to reconnect after 10 seconds
                logger.info(color + 'Failed to connect to camera ID %s...,', camera_id)
                time.sleep(180)  # Wait for 10 seconds
                logger.info(color + 'Attempting to reconnect to camera ID %s', camera_id)

                 # Check the connection again
                video_src = cv2.VideoCapture(rtsp_url)
                retrieve, frame = video_src.read()      
        
            if (time.time() - start_capture_time) > interval:
                start_capture_time = time.time()
                if retrieve:
                    name = datetime.datetime.now().strftime("%y%m%d-%H%M%S-%f")
                    cv2.imwrite(os.path.join(capture_folder, f'{name}.jpg'), frame,
                                [cv2.IMWRITE_JPEG_QUALITY, quality])
                    # Log the capture image
                    logger.info(color + 'Captured image for camera ID %s', camera_id)
                else:
                    logger.info(color + 'Failed to retrieve image for camera ID %s', camera_id)
                    # capture_thread_is_active[camera_id] = False

        except:
            logger.info(color + 'Failed to retrieve image for camera ID %s', camera_id)
            # capture_thread_is_active[camera_id] = False
            pass

    if capture_thread_is_active[camera_id] == False:
        # Stop the capture
        logger.info(color + 'Capture stopped for camera ID %s', camera_id)
        video_src.release()


# MAIN
config = open_config()
# flags
capture_thread_is_active = {camera_id: False for camera_id in config['sources']}
capture_thread_color = {camera_id: color for camera_id, color in zip(config['sources'], [GREEN, YELLOW, BLUE, WHITE])}


# print capture_thread_is_active
logger.info(RED + '%s', capture_thread_is_active)

# Start the captures for all loaded cameras
for camera_id in config['sources']:
    if capture_thread_is_active[camera_id]:
        continue
    # Run the capture process in a separate thread to prevent blocking
    thread = threading.Thread(target=start_capture, args=(camera_id, capture_thread_color[camera_id]))
    thread.start()
