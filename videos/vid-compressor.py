import os
import subprocess

# Supported file types
VIDEO_EXTENSIONS = ('.mp4', '.mov', '.webm', '.mkv', '.avi')
GIF_EXTENSIONS = ('.gif',)

def compress_video(input_file, output_file):
    """
    Compress a video using ffmpeg (H.264 + CRF).
    """
    try:
        subprocess.call([
            "ffmpeg",
            "-i", input_file,
            "-vcodec", "libx264",
            "-crf", "28",
            "-preset", "fast",
            "-acodec", "aac",
            output_file,
            "-y"
        ])
    except Exception as e:
        print("Error compressing video {}: {}".format(input_file, e))


def compress_gif(input_file, output_file):
    """
    Compress a GIF by generating a palette and using optimized dithering.
    """
    try:
        palette = "palette.png"

        # Step 1: Generate palette
        subprocess.call([
            "ffmpeg", "-i", input_file,
            "-vf", "palettegen",
            palette,
            "-y"
        ])

        # Step 2: Apply palette for compression
        subprocess.call([
            "ffmpeg", "-i", input_file,
            "-i", palette,
            "-lavfi", "paletteuse=dither=sierra2_4a",
            output_file,
            "-y"
        ])

        # Remove temporary palette file
        if os.path.exists(palette):
            os.remove(palette)

    except Exception as e:
        print("Error compressing GIF {}: {}".format(input_file, e))


def main():
    print("Scanning directory...\n")

    files = os.listdir(".")
    any_found = False

    for file in files:
        lower = file.lower()

        # Skip files already compressed
        if "compressed" in lower:
            print("Skipping already compressed:", file)
            continue

        # Videos
        if lower.endswith(VIDEO_EXTENSIONS):
            any_found = True
            filename, ext = os.path.splitext(file)
            output_file = filename + "-compressed" + ext
            print("Compressing video:", file)
            compress_video(file, output_file)
            print("→ Done:", output_file)
            print("--------------------------------------------------")

        # GIFs
        elif lower.endswith(GIF_EXTENSIONS):
            any_found = True
            filename, ext = os.path.splitext(file)
            output_file = filename + "-compressed.gif"
            print("Compressing GIF:", file)
            compress_gif(file, output_file)
            print("→ Done:", output_file)
            print("--------------------------------------------------")

    if not any_found:
        print("No videos or GIFs found.")

    print("Finished compressing all media files!")


if __name__ == "__main__":
    main()
