import cv2
import matplotlib.pyplot as plt
from numpy import ndarray

def generate_color_histogram(image: ndarray) -> list:
    """
    Вычисляет цветовые гистограммы для каждого канала изображения
    :параметр image: Входное изображение в виде числового массива.
    :return: Список, содержащий гистограммы для каждого цветового канала.
    """

    color_histograms = []

    for channel in range(3):
        histogram = cv2.calcHist([image], [channel], None, [256], [0, 256])
        color_histograms.append(histogram)

    return color_histograms

def display_histogram(color_histograms: list) -> None:
    """
    Отображает цветовые гистограммы для каждого канала на графике.
    :параметр color_histograms: Список гистограмм для цветовых каналов.
    """

    color_codes = ['b', 'g', 'r']
    channel_names = ['Blue', 'Green', 'Red']

    plt.figure(figsize=(10, 5))

    for index, histogram in enumerate(color_histograms):
        plt.plot(histogram, color=color_codes[index], label=channel_names[index])

    plt.title('Image Color Histogram')
    plt.xlabel('Intensity Value')
    plt.ylabel('Pixel Count')

    plt.legend()
    plt.show()
