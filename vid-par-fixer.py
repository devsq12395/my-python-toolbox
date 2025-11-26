import sys
import subprocess
import os

def fix_video_resolution(input_path):
    base, ext = os.path.splitext(input_path)
    output_path = base + "_fixed.mp4"

    print("Fixing video:", input_path)
    print("Output file:", output_path)

    # Correct filter order to force real encoding resolution
    vf_filter = "setsar=1,scale=1110:684,setdar=1110/684"

    cmd = [
        "ffmpeg",
        "-i", input_path,
        "-vf", vf_filter,
        "-c:v", "libx264",
        "-crf", "20",
        "-preset", "medium",
        "-c:a", "aac",
        "-b:a", "128k",
        output_path
    ]

    try:
        subprocess.check_call(cmd)
        print("\nDone! Saved as:", output_path)
    except subprocess.CalledProcessError:
        print("\nError: FFmpeg failed to process the file.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 fix.py <input_video>")
        sys.exit(1)

    fix_video_resolution(sys.argv[1])
