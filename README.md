# ExploringChromaKey

## Overview
Scripts for replacing video backgrounds in Chroma Key using the **OpenCV** library.

## Process 
This project was the first challenge of [Carlos Melo's](https://www.linkedin.com/in/carlos-melo-data-science/) Computer Vision course.
Firstly, I used an open source deep learning project to change the background of a random video of mine with a chroma key background, then I used the OpenCV library to process this video, leaving it with the proportions of the new chosen background, and then I collected samples RGB of the green background to improve the appearance of the final result. So, finally, a script was made to replace the green background with the desired one.

### How to run
1. Clone this project

```bash
git clone https://github.com/mariannedutra/ExploringChromaKey.git
```

2. Create and activate a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install the requirements
```bash
pip install -r requirements.txt
```

### Using OpenCV to replaces the green background in a video (chroma key) with a selected video or background image.

Use:
```bash
python main.py -i <video_file> -b <video_background_file> -c <colors_json>
```

Arguments:
```bash
-i (--input): Path to the foreground video.
-b (--background): Path to green background video.
-c (--colors): Path to the JSON file with color bounds.
```

Example:
```bash
python main.py -i data/foreground.mp4 -b data/background.jpg -c data/samples.json

```

### Using a deep learning open source project to change a video background to Chroma Key
This project allows you to insert your own videos and convert your backgrounds to Chroma Key.

* [Link for Github](https://github.com/PeterL1n/RobustVideoMatting)
* [Link for Colab](https://colab.research.google.com/drive/10z-pNKRnVNsp0Lq9tH1J_XPZ7CBC_uHm?usp=sharing)

### Script to resize a video.
Use:
```bash
python resize-video.py -i <video_file> 
```

Arguments:
```bash
-i (--input): Path to the input video.
-o (--output): Path to save the output video.
-w (--width): Desired width of the output video.
-ht (--height): Desired height of the output video.
```

Example:
```bash
python resize-video.py -i data/input.mp4 -o data/output.mp4 -w 1920 -h 1080

```

### Script to extract RGB colors from a video using OpenCV.
> If the values ​​defined to create the green mask do not give good results with other videos, you can try deleting the content of samples.json and using this script to generate new metrics.

Use:
```bash
python searching-colors.py -i <video_file> -o <output_json>
```

Arguments:
```bash
-i (--image): Path to the video file.
-o (--output): Output file to save color bounds.
```

Example:
```bash
python searching-colors.py -i data/video.mp4 -o data/samples.json
```


