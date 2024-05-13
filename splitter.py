from moviepy.editor import VideoFileClip, CompositeVideoClip, vfx
from moviepy.video.VideoClip import ImageClip

import math
import random

# set the input file path
input_file = "video/Ep77.mp4"

# set the duration range of the output clips in seconds
min_duration = 37
max_duration = 59

# check that the minimum duration is not greater than the maximum duration
if min_duration > max_duration:
    raise ValueError("min_duration cannot be greater than max_duration")

# set the number of output clips to generate
num_clips = 30

# set the path to the burn-in image
burn_in_image_path = "images/77-header.png"

# set the location size of the overlay
burn_in_width = 500
burn_in_height = 142
burn_in_position = (0, -20)

# set the prefix for the output filename
file_prefix = "Ep77-mov_"

# create an ImageClip object from the burn-in image file
try:
    burn_in_image = ImageClip(burn_in_image_path)
except OSError:
    burn_in_image = ImageClip("images/default-header.png")  # replace with a default image

burn_in_image = burn_in_image.set_duration(max_duration).resize(width=burn_in_width, height=burn_in_height).set_position(burn_in_position)

# create a VideoFileClip object from the input file
video = VideoFileClip(input_file)

# loop through the total number of clips and create each one
for i in range(num_clips):
    # generate a random start time for the clip
    start_time = random.uniform(0, video.duration - max_duration)
    
    # generate a random duration for the clip within the specified range
    clip_duration = random.uniform(min_duration, max_duration)
    
    # calculate the end time for the clip
    end_time = start_time + clip_duration

    # create a new clip using the start and end times
    clip = video.subclip(start_time, end_time)

    # This creates a new clip (burn_in_clip) from the burn-in image that has the same duration as the actual video clip.
    burn_in_clip = burn_in_image.subclip(0, clip.duration)

    # set the output file path for the new clip
    output_file = f"output/{file_prefix}clips_{i+1}.mov"

    # set the dimensions and rotation for the output video
    dimensions = (1080, 1920) # width, height
    rotation = 0

    # rotate the clip clockwise by 90 degrees
    clip = clip.rotate(angle=rotation, resample='bilinear')

    # set the dimensions of the region to crop
    crop_width = 350
    crop_height = 500

    # set the crop coordinates
    crop_x1 = 325
    crop_y1 = 100
    crop_x2 = crop_x1 + crop_width
    crop_y2 = crop_y1 + crop_height

    # crop the region from the center of the video
    clip = clip.crop(x1=crop_x1, y1=crop_y1, x2=crop_x2, y2=crop_y2)

    # create a CompositeVideoClip with the clip, burn-in image, and overlay image
    clip = CompositeVideoClip([clip, burn_in_clip])

    # write the new clip to the output file with the specified dimensions and rotation
    clip = clip.resize(dimensions)
    clip.write_videofile(output_file, codec="libx265", audio_codec="aac",
                         ffmpeg_params=["-preset", "slow"])
