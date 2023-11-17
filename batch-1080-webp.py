import os
from PIL import Image

def resize_image(input_path, output_path, max_length=1080):
    with Image.open(input_path) as img:
        # Calculate the scaling factor
        scale_factor = min(max_length / max(img.size), 1)
        new_size = (int(img.size[0] * scale_factor), int(img.size[1] * scale_factor))

        # Resize the image using the LANCZOS filter
        resized_img = img.resize(new_size, Image.Resampling.LANCZOS)

        # Save the image in WebP format
        resized_img.save(output_path, 'WEBP')

def batch_resize_images(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, filename)
                relative_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, relative_path)

                if not os.path.exists(output_subdir):
                    os.makedirs(output_subdir)

                output_path = os.path.join(output_subdir, os.path.splitext(filename)[0] + '.webp')
                resize_image(input_path, output_path)
                print(f'Processed {input_path}')

# Usage
input_directory = 'input directory path'
output_directory = 'output directory path'
batch_resize_images(input_directory, output_directory)
