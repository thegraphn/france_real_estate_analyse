import os.path
from multiprocessing import Pool
import pandas as pd
from tqdm import tqdm
from config.config import base_url, years, merged_data_file_name
from data_handling.data_preparation import DataPreparer
from data_handling.get_data import InputDownloader
from model.model import ModelStatistics
from utils.utils import write_df_to_csv
from view.visualization import Visualizer


def main():
    print('Starting main')
    input_downloaders = [InputDownloader(
        base_url=base_url,
        suffix_url=year,
        suffix_file_name="full.csv.gz"
    )
        for year in years]
    for input_downloader in input_downloaders:
        if input_downloader.data_there is False:
            input_downloader.download_file_from_url()
            if input_downloader.can_be_downloaded:
                input_downloader.unzip_file()

    # Merge all data frames
    if os.path.exists(merged_data_file_name) is False:
        data_preparer = DataPreparer(list_path_csv_files=
                                     [input_downloader.output_file_path
                                      for input_downloader in input_downloaders
                                      if input_downloader.can_be_downloaded]
                                     )
        data_preparer.merge_data_frame()
        data_preparer.merged_data_frame.to_csv(merged_data_file_name, index=False)
    else:
        data_preparer = DataPreparer()
        data_frame = data_preparer.get_merged_data_frame(merged_data_file_name)
    # Group the data with a range of 10km
    postal_grouped_df = data_preparer.group_transaction_by_postal_code()
    # Save the data in a csv file
    info_save_csv = [(df, f"./data/{postal_code}.csv") for postal_code, df in postal_grouped_df]
    with Pool(10) as p:
        list_csv_path = list(
            tqdm(p.imap(write_df_to_csv, info_save_csv), total=len(info_save_csv), desc="Writing postal code to csv"))
    # Create a model_statistic instance to model each data frame
    stat_models = [ModelStatistics(pd.read_csv(csv_path, low_memory=False)) for csv_path in list_csv_path]

    for stat_model in tqdm(stat_models, total=len(stat_models), desc="Computing statistics"):
        stat_model.compute_mean_value_square_meter_per_year()
        stat_model.compute_value_evolution()
    #Merge the stat df
    list_df = [stat_model.report for stat_model in stat_models]
    merged_stat_df = pd.concat(list_df)
    merged_stat_df.to_csv("./data/merged_stat_df.csv", index=False)


if __name__ == "__main__":
    main()
    #todo what is actually computed is the difference of volume between years
    # it is needed to normalize per m2
