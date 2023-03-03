"""Load data from csv files"""
import math
from tqdm import tqdm
import pandas as pd


class DataPreparer:
    """Class to prepare the data"""

    def __init__(self, list_path_csv_files=None):
        if list_path_csv_files is None:
            list_path_csv_files = []
        self.list_path_csv_files = list_path_csv_files
        self.merged_data_frame = None

    def merge_data_frame(self):
        """Merge all data frames"""
        print(f"Merging data frames")
        data_frames_merged = pd.concat([
            pd.read_csv(path_csv_file, low_memory=False)
            for path_csv_file in self.list_path_csv_files
        ]
            , ignore_index=True
        )

        print(f"Data frames merged")
        print(f"Number of rows: {len(data_frames_merged)}")
        self.merged_data_frame = data_frames_merged

    def get_merged_data_frame(self, csv_path):
        """Return the merged data frame"""
        self.merged_data_frame = pd.read_csv(csv_path, low_memory=False)
        # Keep rows with Maison or Appartement in the column type_local
        self.merged_data_frame = self.merged_data_frame[
            self.merged_data_frame["type_local"].isin(["Maison", "Appartement"])]
        print(f"Number of rows: {len(self.merged_data_frame)}")
        print(f"Data frame loaded")

    def group_transaction_by_postal_code(self):
        """
        Group transactions by postal code
        """
        # Based on the column code_postal group the data
        # Group the data by postal code

        grouped_data = self.merged_data_frame.groupby("code_postal")
        # for each postal_code save the data in a csv file
        return grouped_data

