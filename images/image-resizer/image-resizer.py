from PIL import Image
import os

# Set the target size for the images
target_width = 1280  # Adjust this to your desired width
target_height = 720  # Adjust this to your desired height

# Get the current directory
current_dir = os.getcwd()

# List all files in the current directory
files = os.listdir(current_dir)

# Loop through the files
for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):  # Add more image extensions if needed
        with Image.open(file) as img:
            # Resize the image
            img = img.resize((target_width, target_height))
            # Save the resized image
            img.save("resized_" + file)

print("Image resizing complete.")