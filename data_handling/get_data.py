"""Class to download input data"""
import gzip
import logging
import shutil
import requests
import os


class InputDownloader:
    """Download handler to download and unzip the input data"""

    def __init__(self, base_url: str, suffix_url: str, suffix_file_name: str):
        self.data_dir = "./data"
        self.data_there = False
        self.can_be_downloaded = True
        self.base_url = base_url
        self.suffix_url = suffix_url
        self.suffix_file_name = suffix_file_name
        self.full_url = self.get_full_url()
        self.temp_file_path = None
        self.output_file_path = self.get_file_name()
        self.set_up()

    def set_up(self):
        """Set up the input downloader"""
        if os.path.exists(self.data_dir) is False:
            os.mkdir(self.data_dir)
        if os.path.exists(self.get_file_name()):
            self.data_there = True

    def get_full_url(self) -> str:
        """Return the full url to download the file"""
        return self.base_url + self.suffix_url + "/" + self.suffix_file_name

    def get_file_name(self) -> str:
        """Return the local file name"""
        return os.path.join(self.data_dir, self.suffix_url + "_" + self.suffix_file_name.replace(".gz", ""))

    def get_temp_file_path(self) -> str:
        """Return the path to the temporary file"""
        return os.path.join(self.data_dir, self.suffix_url + "_" + self.suffix_file_name + ".tmp")

    def download_file_from_url(self) -> None:
        """Download file from url and return the path to the downloaded file
        """
        print(f"Downloading file from url {self.get_full_url()}")
        try:
            request = requests.get(self.full_url, allow_redirects=True)
            if request.status_code == 200:
                with open(self.get_temp_file_path(), 'wb') as f:
                    f.write(request.content)
            else:
                self.can_be_downloaded = False
        except Exception as e:
            logging.error(e)
        print(f"File downloaded from url {self.get_full_url()}")

    def unzip_file(self) -> None:
        """Unzip file and return the path to the unzipped file
        """
        print(f"Unzipping file {self.get_temp_file_path()}")
        with gzip.open(self.get_temp_file_path(), 'rb') as f_in:
            with open(self.get_file_name(), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"File unzipped {self.get_file_name()}")
