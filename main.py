import logging

from config.config import base_url, years
from data_handling.get_data import InputDownloader


def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    input_downloaders = [InputDownloader(
        base_url=base_url,
        suffix_url=year,
        suffix_file_name="full.csv.gz"
    )
        for year in years]
    for input_downloader in input_downloaders:
        input_downloader.download_file_from_url()
        input_downloader.unzip_file()


if __name__ == "__main__":
    main()
