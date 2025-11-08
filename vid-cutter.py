import argparse
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def cut_video(input_video_path, output_video_path, start_time, end_time):
    """
    Cuts a section of the video between start_time and end_time (in seconds).

    Example:
        cut_video("input.mp4", "output.mp4", 0, 15)
    """
    ffmpeg_extract_subclip(input_video_path, start_time, end_time, targetname=output_video_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cut a section of a video using start and end time (in seconds)")
    parser.add_argument("input_video", help="Input video file")
    parser.add_argument("output_video", help="Output video file")
    parser.add_argument("--start_time", type=float, default=0, help="Start time in seconds (default: 0)")
    parser.add_argument("--end_time", type=float, default=8, help="End time in seconds (default: 8)")

    args = parser.parse_args()

    cut_video(args.input_video, args.output_video, args.start_time, args.end_time)


"""
==========================================
HOW TO USE THIS SCRIPT
==========================================

# Basic example:
python vid-cutter.py input.mp4 output.mp4

# Specify start and end time in seconds:
python vid-cutter.py input.mp4 output.mp4 --start_time 3 --end_time 15

# Works with any format supported by ffmpeg (mp4, webm, mkv, etc.)

# Example for your case (from the screenshot):
python vid-cutter.py xiaomi_20251027-190437.webm xiaomi_20251027-190437-output.webm --start_time 3 --end_time 15
==========================================
"""
