import cv2
import os

def extract_frames(video_path, output_folder, interval=3):
    """
    Extracts frames from a video every 'interval' seconds and saves them as .jpeg images.
    Frame filenames will include the video name to avoid overwriting.
    """
    # Check if video file exists
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        return

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Extract video name (without extension)
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # Open the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
    frame_interval = int(fps * interval)  # Number of frames to skip

    frame_count = 0
    saved_count = 0

    print(f"Extracting frames from '{video_name}'...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # End of video

        if frame_count % frame_interval == 0:
            frame_name = f"{video_name}_frame_{saved_count:04d}.jpeg"
            frame_path = os.path.join(output_folder, frame_name)
            cv2.imwrite(frame_path, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"Done! {saved_count} frames saved to '{output_folder}'.")

# usage example:
extract_frames(r"D:\helyia\New folder (2)\day_6_train2.mp4",
               r"D:\helyia\New folder (2)\frames")