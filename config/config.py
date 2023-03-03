import os

DATA_DIR = "./data"
base_url = "https://files.data.gouv.fr/geo-dvf/latest/csv/"
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
suffix_file_name = "full.csv.gz"

merged_data_file_name = os.path.join(DATA_DIR, "merged_data.csv")
