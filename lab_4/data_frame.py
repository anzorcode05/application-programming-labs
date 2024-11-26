import os

import cv2

import matplotlib.pyplot as plt

import pandas as pd

def create_dataframe(annotation_path: str) -> pd.DataFrame:
    """
    Создает фрейм с абсолютными и относительными путями к изображениям.
    :param annotation_path: Путь к файлу с аннотацией.
    :return: Фрейм с абсолютными и относительными путями.
    """
    if not os.path.exists(annotation_path):
        raise FileNotFoundError(f"Файл аннотации не найден: {annotation_path}")
    data_table = pd.read_csv(annotation_path)
    data_table.columns = ['abs_path', 'rel_path']
    return data_table

def extend_with_image_properties(data: pd.DataFrame) -> None:
    """
    Добавляет столбцы высоты, ширины и глубины изображения во фрейм.
    :param data: Информация об изображениях.
    :return: None
    """
    heights, widths, depths = [], [], []
    for path in data["abs_path"]:
        img = cv2.imread(path).shape
        heights.append(img[0])
        widths.append(img[1])
        depths.append(img[2])
    data["height"] = pd.Series(heights)
    data["width"] = pd.Series(widths)
    data["depth"] = pd.Series(depths)

def compute_image_area(data: pd.DataFrame) -> None:
    """
    Добавляет столбец с площадями изображений.
    :param data: Информация об изображениях.
    :return: None
    """
    data["image_area"] = data["height"] * data["width"]

def show_image_stats(data: pd.DataFrame) -> None:
    """
    Выводит статистическую информацию для столбцов высоты, ширины и глубины.
    :param data: Информация об изображениях.
    :return: None
    """
    print(data[['height', 'width', 'depth']].describe())

def filter_images(data: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Создает отфильтрованный по ширине и высоте фрейм с информацией об изображениях.
    :param data: Информация об изображениях.
    :param max_width: Максимальная ширина изображения.
    :param max_height: Максимальная высота изображения.
    :return: Отфильтрованный фрейм.
    """
    return data[(data['width'] <= max_width) & (data['height'] <= max_height)]

def sort_by_area(data: pd.DataFrame) -> pd.DataFrame:
    """
    Создает отсортированный по увеличению площади фрейм с информацией об изображениях.
    :param data: Информация об изображениях.
    :return: Отсортированный фрейм.
    """
    return data.sort_values(by='image_area')

def plot_area_histogram(data: pd.DataFrame) -> None:
    """
    Выводит гистограмму площадей изображений.
    :param data: Информация об изображениях.
    :return: None
    """
    plt.hist(data['image_area'], bins=20, color='blue', alpha=0.7)
    plt.title('Распределение площадей изображений')
    plt.xlabel('Площадь (пиксели)')
    plt.ylabel('Частота')
    plt.grid(axis='y')
    plt.show()
