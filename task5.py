import pandas as pd

df = pd.read_csv('Dataset_of_diabetes.csv')
age_gender = df.groupby('Gender')['AGE'].mean()
print(age_gender)
