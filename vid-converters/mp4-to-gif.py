import os
import subprocess
import time
import argparse

# ##########################################
#
# USE PYTHON 3.13.1
#
# ##########################################

def convert_mp4_to_gif(input_file, output_file, trim_duration=None):
    """
    Convert an MP4 file to a GIF using FFmpeg.

    :param input_file: Path to the input MP4 file.
    :param output_file: Path to save the converted GIF file.
    :param trim_duration: Optional duration in seconds (int or float). If set, only converts that duration from start.
    """
    if not os.path.exists(input_file):
        print("Input file does not exist:", input_file)
        return

    try:
        # Build ffmpeg command
        command = [
            "ffmpeg",
            "-i", input_file,       # Input file
            "-vf", "fps=15,scale=480:-1:flags=lanczos",  # Frame rate + scaling filter
            "-loop", "0",           # Loop forever
        ]

        # Add trim duration if specified
        if trim_duration:
            command.extend(["-t", str(trim_duration)])

        # Output file
        command.append(output_file)

        subprocess.check_call(command)
        print("Converted:", input_file, "->", output_file)
    except subprocess.CalledProcessError as e:
        print("Error during conversion for file:", input_file, "-", e)

def convert_all_mp4_to_gif(directory, trim_duration=None):
    """
    Convert all MP4 files in a directory to GIF with timestamped filenames.

    :param directory: Path to the directory containing MP4 files.
    :param trim_duration: Optional trim duration in seconds.
    """
    if not os.path.isdir(directory):
        print("The specified path is not a directory.")
        return

    mp4_files = [f for f in os.listdir(directory) if f.lower().endswith(".mp4")]

    if not mp4_files:
        print("No MP4 files found in the directory.")
        return

    for file_name in mp4_files:
        input_file = os.path.join(directory, file_name)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        base_name = os.path.splitext(file_name)[0]
        output_file = os.path.join(directory, f"{base_name}_{timestamp}.gif")

        convert_mp4_to_gif(input_file, output_file, trim_duration)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MP4 videos in a directory to GIFs")
    parser.add_argument("--trim", type=float, default=None,
                        help="Trim duration in seconds (optional). Example: --trim 5 converts only the first 5 seconds.")
    parser.add_argument("--dir", default=os.getcwd(),
                        help="Directory containing MP4 files (default: current directory)")
    
    args = parser.parse_args()

    print("Using directory:", args.dir)
    convert_all_mp4_to_gif(args.dir, args.trim)


"""
==========================================
HOW TO USE THIS SCRIPT
==========================================

# Basic usage (convert all .mp4 files in current folder):
python mp4_to_gif.py

# Specify a directory:
python mp4_to_gif.py --dir "C:/Videos"

# Trim conversion to the first 5 seconds of each video:
python mp4_to_gif.py --trim 5

# Trim and specify directory:
python mp4_to_gif.py --dir "C:/Videos" --trim 10

# Output will look like:
example_20251027-191525.gif

==========================================
NOTES:
- Default frame rate: 15 fps
- Default width: 480px (keeps aspect ratio)
- Uses Lanczos scaling for quality
- Loops infinitely (-loop 0)
- You can adjust FPS or scale for smaller or higher quality GIFs
==========================================
"""
