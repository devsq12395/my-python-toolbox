import os
import subprocess
import time

# ##########################################
#
# USE PYTHON 3.13.1
#
# ##########################################

def convert_mp4_to_webm(input_file, output_file):
    """
    Convert an MP4 file to WEBM using FFmpeg.

    :param input_file: Path to the input MP4 file.
    :param output_file: Path to save the converted WEBM file.
    """
    if not os.path.exists(input_file):
        print("Input file does not exist:", input_file)
        return

    try:
        command = [
            "ffmpeg",
            "-i", input_file,     # Input file
            "-c:v", "libvpx-vp9", # Use VP9 codec for video
            "-b:v", "2M",         # Set video bitrate (2 Mbps)
            "-c:a", "libopus",    # Use Opus for audio
            output_file           # Output file
        ]
        subprocess.check_call(command)
        print("Converted:", input_file, "->", output_file)
    except subprocess.CalledProcessError as e:
        print("Error during conversion for file:", input_file, "-", e)

def convert_all_mp4_to_webm(directory):
    """
    Convert all MP4 files in a directory to WEBM with timestamped filenames.

    :param directory: Path to the directory containing MP4 files.
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
        
        # Add timestamp suffix to the filename
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        base_name = os.path.splitext(file_name)[0]
        output_file = os.path.join(directory, f"{base_name}_{timestamp}.webm")
        
        convert_mp4_to_webm(input_file, output_file)

if __name__ == "__main__":
    # Automatically use the current directory
    current_directory = os.getcwd()
    print("Using current directory:", current_directory)
    convert_all_mp4_to_webm(current_directory)
