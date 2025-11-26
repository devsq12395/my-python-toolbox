from PIL import Image, ImageOps
import os

def resize_with_black_mask(input_image_path, output_image_path, target_width, target_height):
    # Open the input image
    image = Image.open(input_image_path)
    
    # Create a new image with the target resolution and a black background
    new_image = Image.new("RGB", (target_width, target_height), "black")

    # Calculate the position to center the input image
    left = (target_width - image.width) // 2
    top = (target_height - image.height) // 2

    # Paste the input image onto the black background at the calculated position
    new_image.paste(image, (left, top))

    # Save the resulting image
    new_image.save(output_image_path)

if __name__ == "__main__":
    input_directory = os.getcwd()  # Get the current directory
    target_width = 3413
    target_height = 1920

    # Loop through all files in the current directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            input_image_path = os.path.join(input_directory, filename)
            output_image_path = os.path.join(input_directory, "resized_" + filename)

            resize_with_black_mask(input_image_path, output_image_path, target_width, target_height)

print("Image resizing complete.")