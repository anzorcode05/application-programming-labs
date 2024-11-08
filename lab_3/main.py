import argparse
import cv2
import matplotlib.pyplot as plt
import os

from color_distribution import *
from image_manipulator import *

def create_argument_parser() -> tuple:
    """
    Parses command-line arguments.
    :return: tuple of arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('input_image_name', type=str, help='Name of the input image')
    parser.add_argument('output_image_name', type=str, help='Name of the output image')
    parser.add_argument('new_height', type=int, help="Desired image height")
    parser.add_argument('new_width', type=int, help="Desired image width")

    return parser.parse_args()

def main_process():

    try:
        args = create_argument_parser()
        input_image_filename = args.input_image_name + '.jpg'

        # Load and display the image
        original_image = load_image(input_image_filename)
        display_image(original_image)
    except Exception:
        print('Unable to read the specified image file.')

    try:
        histograms = generate_color_histogram(original_image)
        display_histogram(histograms)
    except Exception:
        print('Failed to generate the histogram.')

    resized_image = scale_image(original_image, args.new_width, args.new_height)
    display_image(resized_image)

    save_image(resized_image, args.output_image_name)

if __name__ == "__main__":
    main_process()
