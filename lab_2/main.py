import argparse

from iterator import ImagePathIterator
from annotations_csv import generate_annotation_file
from crawl_images import fetch_images

def get_args():
    """
    Анализирует аргументы командной строки для ключевого слова поиска, каталога изображений и пути к файлу CSV.

    :return: Проанализированные аргументы
    """

    parser = argparse.ArgumentParser(description="Download images and create CSV annotations.")
    parser.add_argument('keyword', type=str, help="Search term for images")
    parser.add_argument('image_dir', type=str, help="Directory to save images")
    parser.add_argument('csv_path', type=str, help="Output CSV file path")
    return parser.parse_args()

def main():
    try:
        args = get_args()
        fetch_images(args.keyword, 50, args.image_dir)
        generate_annotation_file(args.image_dir, args.csv_path)

        path_iterator = ImagePathIterator(args.csv_path)
        for entry in path_iterator:
            print(entry)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
