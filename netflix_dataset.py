import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Netflix Dataset.csv")
print(df.head())

Q1 = df[df['Title']=='House of Cards'][['Show_Id','Director']]
print(Q1)
df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')
df['Release_Years'] = df['Release_Date'].dt.year
years_count = df['Release_Years'].value_counts().sort_index()
max_count = years_count.max()
max_year = years_count.idxmax()
print(max_count)
print(max_year)

plt.figure(figsize=(12,6))

