import os.path

from icrawler.builtin import GoogleImageCrawler

def fetch_images(search_term: str, count: int, save_dir: str) -> None:
    """
    Загружает изображения на основе поискового запроса и сохраняет их в указанном каталоге.

    :параметр search_term: Термин для поиска изображений
    :параметр count: Количество загружаемых изображений
    :параметр save_dir: Каталог для сохранения изображений
    """

    try:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        crawler = GoogleImageCrawler(
            feeder_threads=1,
            parser_threads=2,
            downloader_threads=4,
            storage={'root_dir': save_dir}
        )
        crawler.crawl(keyword=search_term, max_num=count)
    except Exception as e:
        raise
