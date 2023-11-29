import os
from PIL import Image

def resize_image(image, max_size=1440):
    # Calculate the scaling factor, keeping the aspect ratio
    ratio = float(max_size) / max(image.size)
    if ratio < 1:  # Only resize if image is larger than max size
        new_size = tuple([int(x*ratio) for x in image.size])
        image = image.resize(new_size, Image.Resampling.LANCZOS)  # Use LANCZOS resampling
    return image

def convert_to_webp(input_path, output_path):
    with Image.open(input_path) as img:
        img = resize_image(img)  # Resize the image
        img.save(output_path, 'WEBP')  # Save the resized image in WebP format

def batch_convert_images(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, filename)
                relative_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, relative_path)

                if not os.path.exists(output_subdir):
                    os.makedirs(output_subdir)

                output_path = os.path.join(output_subdir, os.path.splitext(filename)[0] + '.webp')
                convert_to_webp(input_path, output_path)
                print(f'Processed {input_path}')

# Usage
input_directory = 'Paste File Path Here'
output_directory = 'Paste File Path Here'
batch_convert_images(input_directory, output_directory)
