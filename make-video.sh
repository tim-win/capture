#!/bin/bash
# source: https://askubuntu.com/questions/380199/converting-images-into-video

# mogrify -resize 800x800 ./*.png
# convert ./*.png -delay 10 -morph 10 --limit thread 6 ./%05d.png
# ffmpeg -r 25 -qscale 2  -i temp/%05d.png output.mp4
ffmpeg -framerate 10 -i ./%04d.png -r 30 output.mp4

