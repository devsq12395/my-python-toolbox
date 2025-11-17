import os
import subprocess
import time

# ##########################################
#
# USE PYTHON 3.13.1
#
# ##########################################

def convert_mp4_to_webp(input_file, output_file):
    """
    Convert an MP4 file to animated WEBP using FFmpeg.

    :param input_file: Path to the input MP4 file.
    :param output_file: Path to save the converted WEBP file.
    """
    if not os.path.exists(input_file):
        print("Input file does not exist:", input_file)
        return

    try:
        command = [
            "ffmpeg",
            "-i", input_file,           # Input file
            "-vcodec", "libwebp",       # Use WebP codec
            "-lossless", "0",           # Use lossy compression (set to 1 for lossless)
            "-q:v", "70",               # Quality (0–100, lower = better quality)
            "-preset", "picture",       # Good balance between speed and quality
            "-loop", "0",               # Infinite loop for animated WebP
            "-an",                      # Remove audio (WebP doesn’t support it)
            "-vsync", "0",              # Prevent frame duplication
            output_file                 # Output file
        ]
        subprocess.check_call(command)
        print("Converted:", input_file, "->", output_file)
    except subprocess.CalledProcessError as e:
        print("Error during conversion for file:", input_file, "-", e)

def convert_all_mp4_to_webp(directory):
    """
    Convert all MP4 files in a directory to WEBP with timestamped filenames.

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
        output_file = os.path.join(directory, f"{base_name}_{timestamp}.webp")
        
        convert_mp4_to_webp(input_file, output_file)

if __name__ == "__main__":
    # Automatically use the current directory
    current_directory = os.getcwd()
    print("Using current directory:", current_directory)
    convert_all_mp4_to_webp(current_directory)
