from utils import read_video, save_video
from trackers import Tracker

def main():
    # Read Video
    video_path = r"C:\Users\44780\Documents\python_motion_tracking_again\input_videos\08fd33_4.mp4"
    video_frames = read_video(video_path)
    
    # Initialize Tracker
    tracker = Tracker(r"C:\Users\44780\Documents\python_motion_tracking_again\models\best.pt")
    
    # Create a new generator for tracking
    tracking_frames = read_video(video_path)
    tracks = tracker.get_object_tracks(tracking_frames,
                                       read_from_stub=True,
                                       stub_path='stubs/track_stubs.pkl')
    
    # Create a new generator for saving the video
    saving_frames = read_video(video_path)
    save_video(saving_frames, r"C:\Users\44780\Documents\python_motion_tracking_again\output\output_video_2.avi")

if __name__ == "__main__":
    main()