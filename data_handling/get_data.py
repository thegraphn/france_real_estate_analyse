"""Class to download input data"""
import gzip
import logging
import shutil
import requests


class InputDownloader:
    """Download handler to download and unzip the input data"""
    def __init__(self, base_url: str, suffix_url: str, suffix_file_name: str):
        self.logger = logging.getLogger(__name__)
        self.base_url = base_url
        self.suffix_url = suffix_url
        self.suffix_file_name = suffix_file_name
        self.full_url = self.get_full_url()
        self.temp_file_path = None
        self.output_file_path = self.get_file_name()

    def get_full_url(self) -> str:
        """Return the full url to download the file"""
        return self.base_url   + self.suffix_url + "/"+self.suffix_file_name

    def get_file_name(self) -> str:
        """Return the local file name"""
        return self.suffix_url + "_" + self.suffix_file_name

    def get_temp_file_path(self) -> str:
        """Return the path to the temporary file"""
        return self.get_file_name() + ".tmp"

    def download_file_from_url(self) -> None:
        """Download file from url and return the path to the downloaded file
        """
        print(f"Downloading file from url {self.get_full_url()}")
        request = requests.get(self.full_url, allow_redirects=True)
        with open(self.get_temp_file_path(), 'wb') as f:
            f.write(request.content)
        print(f"File downloaded from url {self.get_full_url()}")

    def unzip_file(self) -> None:
        """Unzip file and return the path to the unzipped file
        """
        print(f"Unzipping file {self.get_temp_file_path()}")
        with gzip.open(self.get_temp_file_path(), 'rb') as f_in:
            with open(self.get_file_name(), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"File unzipped {self.get_temp_file_path()}")
