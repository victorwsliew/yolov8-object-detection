from PIL import Image
import os
import argparse

def resize_images(directory, size):
    for img in os.listdir(directory):
        # only process image files
        if img.endswith(".jpg"):
            im = Image.open(directory + img)
            width, height = im.size

            # Determine the size of the square to crop
            crop_size = min(size[0], size[1], width, height)

            # Calculate the left, top, right, and bottom boundaries to crop a square from the center
            left = (width - crop_size) / 2
            right = (width + crop_size) / 2
            top = (height - crop_size) / 2
            bottom = (height + crop_size) / 2

            # Crop the image
            im_cropped = im.crop((left, top, right, bottom))

            # Save the cropped image
            im_cropped.save(directory + "cropped_" + img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Crop images")
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the images')
    parser.add_argument('-s', '--size', type=int, nargs=2, required=True, metavar=('width', 'height'), help='Crop size')
    args = parser.parse_args()
    resize_images(args.directory, tuple(args.size))