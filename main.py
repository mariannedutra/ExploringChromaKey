import argparse
import cv2
import numpy as np
import json

parser = argparse.ArgumentParser(
    description='Script to replace the green background with a selected video or image'
)
parser.add_argument(
    '-i',
    '--input',
    help='Path to green background video.',
    required=True,
)
parser.add_argument(
    '-b', '--background', help='Path to new background.', required=True
)
parser.add_argument(
    '-c', '--colors', help='Path to the JSON file with color bounds.', required=True
)
args = parser.parse_args()

# Load the color bounds
with open(args.colors, 'r') as f:
    bounds = json.load(f)
    lower_green = np.array(bounds['lower_bound'], dtype=np.uint8)
    upper_green = np.array(bounds['upper_bound'], dtype=np.uint8)

cap_foreground = cv2.VideoCapture(args.input)
cap_background = cv2.VideoCapture(args.background)

while True:
    ret_foreground, frame_foreground = cap_foreground.read()
    ret_background, frame_background = cap_background.read()

    if not ret_foreground or not ret_background:
        break

    mask = cv2.inRange(frame_foreground, lower_green, upper_green)

    background = cv2.bitwise_and(frame_background, frame_background, mask=mask)

    mask_inv = cv2.bitwise_not(mask)

    foreground = cv2.bitwise_and(
        frame_foreground, frame_foreground, mask=mask_inv
    )
    result = cv2.addWeighted(background, 1, foreground, 1, 0)

    cv2.imshow('Result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_foreground.release()
cap_background.release()
cv2.destroyAllWindows()
