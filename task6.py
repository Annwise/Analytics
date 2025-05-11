import pandas as pd

df = pd.read_csv('Dataset_of_diabetes.csv')
print(df.isnull().sum())
