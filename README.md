# Video Splitter

This python script will convert a MP4 into multiple smaller video files.

Take a full length video such as ..

![](documentation/full_video.png)

.. and create random clips of various lengths that look like ..

![](documentation/clipped_video.png)

## The user can set the following parameters

The user can set the input file.
```
input_file = "video/Ep77.mp4"
```

- Max and Min length (in seconds) of clipped video
- Number of clippped videos to generate
- Image to burn in as overlay
- Prefix of clipped video file name
- clipped video dimension and rotation
- Dimensions of region to crop
- Region of original video to crop

**Length of clipped videos.**
```
min_duration = 37
max_duration = 59
```
**Number of clipped videos.**
```
num_clips = 30
```
**Image to burn in as overlay**
```
burn_in_image_path = "images/77-header.png"
```
**Length of clipped videos.**
```
file_prefix = "Ep77-mov_"
```

**Clipped video dimension and rotation**
```
    dimensions = (1080, 1920) # width, height
    rotation = 0
```
**Dimensions of region to crop**
```
    crop_width = 350
    crop_height = 500
```

**Region of original video to crop**
```
    crop_x1 = 325
    crop_y1 = 100
    crop_x2 = crop_x1 + crop_width
    crop_y2 = crop_y1 + crop_height
```


>NOTE: You will need ffmpeg installed locally
