import os
import pandas as pd

print("src:", os.getcwd())
print("data:", os.listdir())

df = pd.read_csv("data/sales.csv")

print(df.head())
