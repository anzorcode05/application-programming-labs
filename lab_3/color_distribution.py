import cv2
import matplotlib.pyplot as plt
from numpy import ndarray

def generate_color_histogram(image: ndarray) -> list:
    """
    Computes color histograms for each channel in the image.
    :param image: The input image as a NumPy array.
    :return: A list containing histograms for each color channel.
    """

    color_histograms = []

    for channel in range(3):
        histogram = cv2.calcHist([image], [channel], None, [256], [0, 256])
        color_histograms.append(histogram)

    return color_histograms

def display_histogram(color_histograms: list) -> None:
    """
    Displays the color histograms for each channel in a plot.
    :param color_histograms: List of histograms for color channels.
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
