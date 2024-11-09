import cv2
from numpy import ndarray

def load_image(image_filename: str) -> ndarray:
    """
    Загружает файл изображения и возвращает его в виде массива NumPy.
    :параметр image_filename: Имя файла загружаемого изображения.
    :возвращает: Данные изображения в виде массива NumPy.
    """
    image = cv2.imread(image_filename)
    return image

def display_image(image_data: ndarray) -> None:
    """
    Отображает изображение в окне с помощью OpenCV и печатает его размеры.
    :параметр image_data: Изображение для отображения в виде числового массива.
    """
    cv2.imshow('Displayed Image', image_data)
    cv2.waitKey(0)

    img_height, img_width = image_data.shape[:2]
    return img_height, img_width

def scale_image(image_data: ndarray, target_width: int, target_height: int) -> ndarray:
    """
    Изменяет размер изображения до заданных размеров.
    :параметр image_data: Изображение в виде числового массива.
    :параметр target_width: Желаемая ширина.
    :параметр target_height: Желаемая высота.
    :return: Изменение размера изображения в виде числового массива.
    """
    target_size = (target_width, target_height)
    scaled_image = cv2.resize(image_data, target_size, interpolation=cv2.INTER_LINEAR)
    return scaled_image

def save_image(output_image_data: ndarray, output_filename: str) -> None:
    """
    Сохраняет обработанное изображение в указанном файле с именем файла.
    :параметр output_image_data: Данные изображения для сохранения.
    :параметр output_filename: имя выходного файла.
    """
    cv2.imwrite(output_filename, output_image_data)
