import csv
import os

def generate_annotation_file(img_folder: str, output_csv: str) -> None:
    """
    Генерирует CSV-файл со списком абсолютных и относительных путей к изображениям в заданном каталоге.

    :параметр img_folder: Каталог, содержащий изображения
    :параметр output_csv: Путь к выходному CSV-файлу
    """

    try:
        with open(output_csv, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            headers = ['Absolute_Path', 'Relative_Path']
            writer.writerow(headers)

            for image_file in os.listdir(img_folder):
                rel_path = os.path.join(img_folder, image_file)
                abs_path = os.path.abspath(rel_path)
                writer.writerow([abs_path, rel_path])
    except (OSError, csv.Error) as e:
        raise
