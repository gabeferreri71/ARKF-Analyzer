# requesting manually is beyond my ability to do
import pandas as pd
#read filenames in data folder
import os
names = os.listdir("./data")
#read in data
df = pd.read_csv("data/"+names[0])
print(df.columns)
relevantdf = df[['ticker', 'weight (%)']]

relevantdf.dropna(inplace=True)
print(relevantdf)