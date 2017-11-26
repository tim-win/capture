#!/usr/bin/env python3
"""Take and save pictures."""
from datetime import datetime
from datetime import timedelta
import os
import sys
import time

import pygame.camera

DELAY = 8  # delay between images in seconds
BASE_PATH = '~/Pictures/stills/'

def get_camera():
    pygame.camera.init()
    camera = pygame.camera.list_cameras()[-1]
    cam = pygame.camera.Camera(camera, (1920, 1080))
    cam.start()
    return cam

def create_folder():
    base_path = os.path.expanduser(BASE_PATH)
    for x in range(1000):
        try:
            prefix = datetime.now().strftime('%Y-%m-%d-')
            prefix += format(x, '04')
            path = os.path.join(base_path, prefix)
            os.makedirs(path)
            return path
        except FileExistsError as e:
            print('WARN:', e, '- Ignoring')
            continue


def main_loop(path):
    # Initialize camera

    # Use a mark to keep time
    mark = datetime.now() - timedelta(seconds=DELAY)
    try:
        while True:
            if datetime.now() - mark > timedelta(seconds=DELAY):
                cam = get_camera()
                mark = datetime.now()

                img = cam.get_image()
                filename = datetime.now().strftime('%Y-%m-%d-%H:%M:%S.png')
                full_path = os.path.join(path, filename)
                pygame.image.save(img, full_path)
                print('Saved {0}...'.format(full_path))
                cam.stop()
                time.sleep(0.5)
    except KeyboardInterrupt:
        return 0
    except Exception as e:
        print(e)
        return 1
    finally:
        try:
            cam.stop()
        except:
            pass


def main():
    rc = 0

    path = create_folder()
    
    rc = main_loop(path)
    return rc

if __name__ == '__main__':
    sys.exit(main())
