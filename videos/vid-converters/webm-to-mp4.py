import os
import subprocess
import time

# ##########################################
#
# USE PYTHON 3.13.1
#
# ##########################################

def convert_webm_to_mp4(input_file, output_file):
    """
    Convert a WEBM file to MP4 using FFmpeg.

    :param input_file: Path to the input WEBM file.
    :param output_file: Path to save the converted MP4 file.
    """
    if not os.path.exists(input_file):
        print("Input file does not exist:", input_file)
        return

    try:
        command = [
            "ffmpeg",
            "-i", input_file,   # Input file
            "-c:v", "libx264",  # H.264 video codec (widely compatible)
            "-c:a", "aac",      # AAC audio codec
            "-b:v", "2M",       # Set video bitrate (2 Mbps)
            "-movflags", "+faststart",  # Optimize for web playback
            output_file         # Output file
        ]
        subprocess.check_call(command)
        print("Converted:", input_file, "->", output_file)
    except subprocess.CalledProcessError as e:
        print("Error during conversion for file:", input_file, "-", e)

def convert_all_webm_to_mp4(directory):
    """
    Convert all WEBM files in a directory to MP4 with timestamped filenames.

    :param directory: Path to the directory containing WEBM files.
    """
    if not os.path.isdir(directory):
        print("The specified path is not a directory.")
        return

    webm_files = [f for f in os.listdir(directory) if f.lower().endswith(".webm")]

    if not webm_files:
        print("No WEBM files found in the directory.")
        return

    for file_name in webm_files:
        input_file = os.path.join(directory, file_name)
        
        # Add timestamp suffix to filename
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        base_name = os.path.splitext(file_name)[0]
        output_file = os.path.join(directory, f"{base_name}_{timestamp}.mp4")
        
        convert_webm_to_mp4(input_file, output_file)

if __name__ == "__main__":
    # Automatically use the current directory
    current_directory = os.getcwd()
    print("Using current directory:", current_directory)
    convert_all_webm_to_mp4(current_directory)


"""
==========================================
HOW TO USE THIS SCRIPT
==========================================

# Basic usage (convert all .webm files in current folder):
python webm_to_mp4.py

# Specify a different directory:
python webm_to_mp4.py  (then modify 'current_directory' variable in code)

# Output format:
input:  myclip.webm
output: myclip_20251112-152500.mp4

==========================================
NOTES:
- Video codec: libx264 (best MP4 compatibility)
- Audio codec: AAC (widely supported)
- Bitrate: 2 Mbps (change "-b:v" for quality/size)
- "+faststart" makes MP4s load faster on the web
==========================================
"""
