from utils import read_video, save_video

def main():
    # Read Video
    video_frames = read_video(r"C:\Users\44780\Documents\python_motion_tracking_again\input_videos\08fd33_4.mp4")

    # Save video
    save_video(video_frames, r"C:\Users\44780\Documents\python_motion_tracking_again\output\output_video.avi")

if __name__ == "__main__":
    main()