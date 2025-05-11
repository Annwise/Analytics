import pandas as pd

df = pd.read_csv('Dataset_of_diabetes.csv')
age_med = df['AGE'].agg(['mean', 'median', 'max'])
print(age_med)
