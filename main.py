from PIL import Image

def change_aspect_ratio(image_path, new_width, new_height, output_path):
    try:
        # Open the image
        img = Image.open(image_path)

        # Resize the image to the new aspect ratio
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)

        # Save the resized image
        resized_img.save(output_path)
        print(f"Image aspect ratio changed and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_image_path = "path/to/input/image.jpg"
output_image_path = "path/to/output/resized_image.jpg"
new_width = 800  # Desired width
new_height = 600  # Desired height

change_aspect_ratio(input_image_path, new_width, new_height, output_image_path)
