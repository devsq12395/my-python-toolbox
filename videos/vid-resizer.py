import argparse
import subprocess

def resize_video(input_video_path, output_video_path, size_x, size_y):
    """
    Resize a video to the given width (size_x) and height (size_y).

    Example:
        resize_video("input.mp4", "output.mp4", 1020, 720)
    """

    cmd = [
        "ffmpeg",
        "-i", input_video_path,
        "-vf", "scale={}:{}".format(size_x, size_y),
        "-preset", "fast",
        "-y",
        output_video_path
    ]

    subprocess.call(cmd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize a video to a specific width and height.")
    parser.add_argument("input_video", help="Input video file")
    parser.add_argument("output_video", help="Output video file")
    parser.add_argument("--size_x", type=int, required=True, help="Target width (e.g., 1020)")
    parser.add_argument("--size_y", type=int, required=True, help="Target height (e.g., 720)")

    args = parser.parse_args()

    resize_video(args.input_video, args.output_video, args.size_x, args.size_y)



"""
============================================================
HOW TO USE THIS SCRIPT
============================================================

# Resize a video to 1020×720:
python3 vid-resizer.py input.mp4 output.mp4 --size-x 1020 --size-y 720

# Another example:
python3 vid-resizer.py xiaomi.mp4 xiaomi-out.mp4 --size-x 1280 --size-y 720

# Works with any format supported by ffmpeg (mp4, webm, mkv, etc.)

# Requirements:
- ffmpeg must be installed and accessible from your terminal.
============================================================
"""
