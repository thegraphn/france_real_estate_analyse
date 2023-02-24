
def main():
    download_file_from_url(url="https://files.data.gouv.fr/geo-dvf/latest/csv/2022/full.csv.gz",
                           ouput_file_path="input_data.csv.gz")
    unzip_file(file_path="input_data.csv.gz", output_file_path="input_data.csv")

base_url = "https://files.data.gouv.fr/geo-dvf/latest/csv/"
years = ["2017", "2018", "2019", "2020", "2021", "2022"]
suffix_file_name = "full.csv.gz"

import gzip
import shutil

import requests


def download_file_from_url(url: str, ouput_file_path) -> str:
    """Download file from url and return the path to the downloaded file
    """
    request = requests.get(url, allow_redirects=True)
    with open(ouput_file_path, 'wb') as f:
        f.write(request.content)
    return ouput_file_path


def unzip_file(file_path: str, output_file_path) -> str:
    """Unzip file and return the path to the unzipped file
    """
    with gzip.open(file_path, 'rb') as f_in:
        with open(output_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    return output_file_path