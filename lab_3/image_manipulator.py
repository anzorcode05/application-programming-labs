import cv2
from numpy import ndarray

def load_image(image_filename: str) -> ndarray:
    """
    Loads an image file and returns it as a NumPy array.
    :param image_filename: The filename of the image to load.
    :return: Image data as a NumPy array.
    """
    image = cv2.imread(image_filename)
    return image

def display_image(image_data: ndarray) -> None:
    """
    Displays an image in a window using OpenCV and prints its dimensions.
    :param image_data: The image to display as a NumPy array.
    """
    cv2.imshow('Displayed Image', image_data)
    cv2.waitKey(0)

    img_height, img_width = image_data.shape[:2]
    print(f'Image height: {img_height}\nImage width: {img_width}\n')

def scale_image(image_data: ndarray, target_width: int, target_height: int) -> ndarray:
    """
    Resizes an image to specified dimensions.
    :param image_data: The image as a NumPy array.
    :param target_width: Desired width.
    :param target_height: Desired height.
    :return: Resized image as a NumPy array.
    """
    target_size = (target_width, target_height)
    scaled_image = cv2.resize(image_data, target_size, interpolation=cv2.INTER_LINEAR)
    return scaled_image

def save_image(output_image_data: ndarray, output_filename: str) -> None:
    """
    Saves the processed image to a specified filename.
    :param output_image_data: The image data to save.
    :param output_filename: The name of the output file.
    """
    cv2.imwrite(output_filename, output_image_data)
