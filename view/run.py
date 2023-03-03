# create the html report with streamlit
from glob import glob
import pandas as pd

from visualization import Visualizer

df = pd.read_csv("../data/merged_stat_df.csv",low_memory=False)
visualizer = Visualizer(df)
visualizer.run()
