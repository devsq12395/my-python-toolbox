import os
from PIL import Image

def compress_image(input_path, output_path, quality=60):
    try:
        img = Image.open(input_path)

        # Convert to RGB if image has alpha channel
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img.save(output_path, optimize=True, quality=quality)
        print(f"Compressed: {input_path} -> {output_path}")

    except Exception as e:
        print(f"Error compressing {input_path}: {e}")

def compress_all_images_in_directory(quality=60):
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Create output folder
    output_dir = os.path.join(current_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    # Supported image formats
    supported_formats = (".jpg", ".jpeg", ".png", ".webp")

    # Loop through all files
    for filename in os.listdir(current_dir):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(current_dir, filename)
            output_path = os.path.join(output_dir, filename)
            compress_image(input_path, output_path, quality)

if __name__ == "__main__":
    compress_all_images_in_directory(quality=60)
