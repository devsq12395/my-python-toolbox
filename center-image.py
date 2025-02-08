from PIL import Image, ImageDraw
import numpy as np
from collections import Counter

def get_dominant_color(image):
    """Returns the dominant color of an image."""
    image = image.convert("RGB")
    np_image = np.array(image)
    np_image = np_image.reshape((-1, 3))
    counter = Counter(map(tuple, np_image))
    return counter.most_common(1)[0][0]

def place_image_on_canvas(image_path, output_path="output.png"):
    canvas_size = (960, 540)
    
    # Load the image
    img = Image.open(image_path)
    
    # Get the dominant color
    dominant_color = get_dominant_color(img)
    
    # Create a blank canvas with the dominant color
    canvas = Image.new("RGB", canvas_size, dominant_color)
    
    # Resize image while maintaining aspect ratio
    img.thumbnail(canvas_size, Image.LANCZOS)
    
    # Calculate position to center the image
    img_x = (canvas_size[0] - img.width) // 2
    img_y = (canvas_size[1] - img.height) // 2
    
    # Paste the image onto the canvas
    canvas.paste(img, (img_x, img_y))
    
    # Save the output image
    canvas.save(output_path)
    print(f"Image saved to {output_path}")

# Put the images to set here
place_image_on_canvas("screenshot.jpg", "output.jpg")
