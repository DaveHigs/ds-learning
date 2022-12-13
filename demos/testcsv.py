# This program transforms .CSVs to .parquet

import pandas as pd

data = pd.read_csv('data/Hotel_Reviews.csv')

data.to_parquet('data/Hotel_Reviews.parquet')
