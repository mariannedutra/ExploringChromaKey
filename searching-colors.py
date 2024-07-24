import argparse
import cv2
import numpy as np
import json

colors_samples = []

def callback(event: int, x: int, y: int, flags, param) -> None:
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = frame[y, x, 0]
        green = frame[y, x, 1]
        red = frame[y, x, 2]

        colors_samples.append([blue, green, red])

        lower_bound = np.amin(colors_samples, axis=0)
        upper_bound = np.amax(colors_samples, axis=0)
        print(f'Lower bound: {lower_bound}')
        print(f'Upper bound: {upper_bound}')
        text = f'B: {blue}, G: {green}, R: {red}'
        cv2.putText(
            frame,
            text,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1,
        )
        cv2.imshow('image', frame)

parser = argparse.ArgumentParser(
    description='Script to extract RGB colors from a video'
)
parser.add_argument(
    '-i', '--image', help='Video path.', required=True
)
parser.add_argument(
    '-o', '--output', help='Output file to save color bounds.', required=True
)
args = parser.parse_args()

# Open the first frame
cap = cv2.VideoCapture(args.image)
ret, frame = cap.read()
if not ret:
    print(f'Something went wrong: {args.image}')
    exit(1)

cv2.namedWindow('image')
cv2.setMouseCallback('image', callback)

# 'Q' or 'Esc' to quit
while True:
    cv2.imshow('image', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        # Save the bounds to a file
        if colors_samples:
            lower_bound = np.amin(colors_samples, axis=0).tolist()
            upper_bound = np.amax(colors_samples, axis=0).tolist()
            bounds = {
                'lower_bound': lower_bound,
                'upper_bound': upper_bound
            }
            with open(args.output, 'w') as f:
                json.dump(bounds, f)
            print(f'Bounds saved to {args.output}')
        break

cap.release()
cv2.destroyAllWindows()
