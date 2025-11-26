import cv2
import numpy as np

def remove_background(input_image_path, output_image_path):
    """
    Removes the background from an image using OpenCV.
    
    Args:
        input_image_path (str): Path to the input image.
        output_image_path (str): Path to save the image with the background removed.
    """
    # Load the image
    image = cv2.imread(input_image_path)
    if image is None:
        print("Error: Could not load image.")
        return

    # Convert to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Apply thresholding to create a mask
    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

    # Invert the mask
    inverted_mask = cv2.bitwise_not(mask)

    # Use the mask to extract the foreground
    fg = cv2.bitwise_and(image, image, mask=inverted_mask)

    # Save the resulting image
    cv2.imwrite(output_image_path, cv2.cvtColor(fg, cv2.COLOR_RGB2BGR))
    print(f"Background removed successfully. Image saved at {output_image_path}")

# Usage example
if __name__ == "__main__":
    input_path = "crosshair082.png"  # Replace with your image file path
    output_path = "crosshair-grenade.png"  # The output will be in PNG format (supports transparency)

    remove_background(input_path, output_path)
