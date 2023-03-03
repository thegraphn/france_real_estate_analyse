# create the html report with streamlit
from glob import glob
import pandas as pd

from visualization import Visualizer

list_csv_path = [csv_path for csv_path in glob("./data/stat_model*.csv")]
list_df = [pd.read_csv(csv_path) for csv_path in list_csv_path]
visualizer = Visualizer(list_df)
visualizer.run()
