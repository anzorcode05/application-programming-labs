import argparse

import data_frame as df_tool


def parse_arguments() -> argparse.Namespace:
    """
    Получение аргументов из командной строки.
    :return: Возвращает полученные из командной строки аргументы.
    """
    parser = argparse.ArgumentParser(description='Скачивание изображений и создание аннотации.')
    parser.add_argument('--annotation', '-a', type=str, required=True, help='Путь к файлу аннотации (CSV).')
    parser.add_argument('--max_width', '-w', type=int, required=True, help='Максимальная ширина изображения.')
    parser.add_argument('--max_height', '-h', type=int, required=True, help='Максимальная высота изображения.')
    return parser.parse_args()

def run_analysis():
    """
    Выполняет полный анализ данных на основе аннотаций, включая загрузку, фильтрацию, сортировку и визуализацию.
    :return: None
    """
    try:
        args = parse_arguments()

        # Загрузка и обработка данных
        data = df_tool.create_dataframe(args.annotation)
        df_tool.extend_with_image_properties(data)
        df_tool.show_image_stats(data)

        # Фильтрация данных
        print("Оригинальные данные:")
        print(data)
        filtered = df_tool.filter_images(data, args.max_width, args.max_height)
        print("Отфильтрованные данные:")
        print(filtered)

        # Сортировка и визуализация
        df_tool.compute_image_area(data)
        sorted_data = df_tool.sort_by_area(data)
        print("Сортированные данные:")
        print(sorted_data)

        df_tool.plot_area_histogram(data)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    run_analysis()
