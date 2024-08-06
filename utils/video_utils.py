import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        yield frame
    cap.release()

def save_video(video_frames, output_video_path):
    # Get the first frame to determine video properties
    first_frame = next(video_frames)
    height, width = first_frame.shape[:2]

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (width, height))

    # Write the first frame
    out.write(first_frame)

    # Write the rest of the frames
    for frame in video_frames:
        out.write(frame)

    out.release()