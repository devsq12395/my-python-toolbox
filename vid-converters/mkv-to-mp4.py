import os
import subprocess
import time

# ##########################################
#
# USE PYTHON 3.13.1
#
# ##########################################

def convert_mkv_to_mp4(input_file, output_file):
    """
    Convert an MKV file to MP4 using FFmpeg.

    :param input_file: Path to the input MKV file.
    :param output_file: Path to save the converted MP4 file.
    """
    if not os.path.exists(input_file):
        print("Input file does not exist:", input_file)
        return

    try:
        command = [
            "ffmpeg",
            "-i", input_file,  # Input file
            "-c:v", "copy",    # Copy video codec
            "-c:a", "aac",     # Convert audio to AAC for compatibility
            output_file        # Output file
        ]
        subprocess.check_call(command)
        print("Converted:", input_file, "->", output_file)
    except subprocess.CalledProcessError as e:
        print("Error during conversion for file:", input_file, "-", e)

def convert_all_mkv_to_mp4(directory):
    """
    Convert all MKV files in a directory to MP4 with timestamped filenames.

    :param directory: Path to the directory containing MKV files.
    """
    if not os.path.isdir(directory):
        print("The specified path is not a directory.")
        return

    mkv_files = [f for f in os.listdir(directory) if f.lower().endswith(".mkv")]

    if not mkv_files:
        print("No MKV files found in the directory.")
        return

    for file_name in mkv_files:
        input_file = os.path.join(directory, file_name)
        
        # Add timestamp suffix to the filename
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        base_name = os.path.splitext(file_name)[0]
        output_file = os.path.join(directory, f"{base_name}_{timestamp}.mp4")
        
        convert_mkv_to_mp4(input_file, output_file)

if __name__ == "__main__":
    # Automatically use the current directory
    current_directory = os.getcwd()
    print("Using current directory:", current_directory)
    convert_all_mkv_to_mp4(current_directory)
