import pandas as pd

df = pd.read_csv('Dataset_of_diabetes.csv')
df_sorted = df.sort_values('ID', ascending=True)
print(df_sorted.head())
