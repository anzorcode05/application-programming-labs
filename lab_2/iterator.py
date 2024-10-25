
import csv

class ImagePathIterator:
    """
    Пользовательский класс-итератор, который выполняет итерацию по записям CSV для поиска путей к изображениям
    """

    def __init__(self, csv_path: str):
        self.csv_path = csv_path

    def __iter__(self):
        self.file = open(self.csv_path)
        self.reader = csv.reader(self.file)
        next(self.reader)  # Skip header
        return self

    def __next__(self):
        try:
            return next(self.reader)
        except StopIteration:
            self.file.close()
            raise StopIteration
