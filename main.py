from utils import read_video, save_video
from trackers import Tracker

def main():
    # Read Video
    video_frames = read_video(r"C:\Users\44780\Documents\python_motion_tracking_again\input_videos\08fd33_4.mp4")

    # Initialize Tracker
    tracker = Tracker(r"C:\Users\44780\Documents\python_motion_tracking_again\models\best.pt")

    tracks = tracker.get_object_tracks(video_frames)

    # Save video
    save_video(video_frames, r"C:\Users\44780\Documents\python_motion_tracking_again\output\output_video.avi")

if __name__ == "__main__":
    main()