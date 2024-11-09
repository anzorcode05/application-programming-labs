import argparse

import os

import sys

import cv2
import matplotlib.pyplot as plt

def create_argument_parser():
    parser = argparse.ArgumentParser(description='Image manipulation script')
    parser.add_argument('input_image_name', type=str, help='Name of the input image without extension')
    parser.add_argument('output_image_name', type=str, help='Name of the output image without extension')
    parser.add_argument('new_width', type=int, help='New width for the image')
    parser.add_argument('new_height', type=int, help='New height for the image')
    return parser.parse_args()

def load_image(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} not found.")
    return cv2.imread(filename)

def display_image(image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

def generate_color_histogram(image):
    colors = ('b', 'g', 'r')
    histograms = {}
    for i, col in enumerate(colors):
        histograms[col] = cv2.calcHist([image], [i], None, [256], [0, 256])
    return histograms

def display_histogram(histograms):
    for col, hist in histograms.items():
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.show()

def scale_image(image, width, height):
    return cv2.resize(image, (width, height))

def save_image(image, filename):
    cv2.imwrite(filename + '.jpg', image)

try:
    args = create_argument_parser()
    input_image_filename = args.input_image_name + '.jpg'

    # загрузка и отображение изображения
    original_image = load_image(input_image_filename)
    display_image(original_image)

    # Получаем высоту и ширину изображения
    img_height, img_width = display_image(original_image)
    print(f'Image height: {img_height}\nImage width: {img_width}\n')

except Exception:
    print('Unable to read the specified image file.')
    sys.exit(1)  # Завершение выполнения при ошибке загрузки изображения

try:
    histograms = generate_color_histogram(original_image)
    display_histogram(histograms)
except Exception:
    print('Failed to generate the histogram.')
    sys.exit(1)  # Завершение выполнения при ошибке генерации гистограммы

# Масштабируем и отображаем изображение
resized_image = scale_image(original_image, args.new_width, args.new_height)
display_image(resized_image)

# Сохраняем изображение
save_image(resized_image, args.output_image_name)


if __name__ == "__main__":
    main()
