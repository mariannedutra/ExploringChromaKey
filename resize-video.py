import argparse
import cv2

def resize_video(input_path, output_path, width, height):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("Error opening video!")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        resized_frame = cv2.resize(frame, (width, height))
        out.write(resized_frame)

    cap.release()
    out.release()

    print("Resized video saved successfully at:", output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Resize a video to a specified width and height'
    )
    parser.add_argument(
        '-i', '--input', 
        help='Path to the input video', 
        required=True
    )
    parser.add_argument(
        '-o', '--output', 
        help='Path to save the output video', 
        required=True
    )
    parser.add_argument(
        '-w', '--width', 
        type=int, 
        help='Desired width of the output video', 
        required=True
    )
    parser.add_argument(
        '-ht', '--height', 
        type=int, 
        help='Desired height of the output video', 
        required=True
    )
    args = parser.parse_args()

    resize_video(args.input, args.output, args.width, args.height)
