import argparse

import os

import sys

import matplotlib.pyplot as plt
from image_manipulator import load_image, display_image, scale_image, save_image
from colo_distribution import generate_color_histogram, display_histogram

def create_argument_parser():
    parser = argparse.ArgumentParser(description='Image manipulation script')
    parser.add_argument('input_image_name', type=str, help='Name of the input image without extension')
    parser.add_argument('output_image_name', type=str, help='Name of the output image without extension')
    parser.add_argument('new_width', type=int, help='New width for the image')
    parser.add_argument('new_height', type=int, help='New height for the image')
    return parser.parse_args()

def main():
    try:
        # Обработка аргументов
        args = create_argument_parser()
        input_image_filename = args.input_image_name + '.jpg'

        # Загрузка изображения
        original_image = load_image(input_image_filename)

        # Отображение оригинального изображения
        display_image(original_image)

        # Генерируем и отображаем гистограмму
        histograms = generate_color_histogram(original_image)
        display_histogram(histograms)

        # Масштабирование изображения
        resized_image = scale_image(original_image, args.new_width, args.new_height)
        display_image(resized_image)

        # Сохранение результата
        save_image(resized_image, args.output_image_name)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
