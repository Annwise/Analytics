# фильтрация данных

import pandas as pd

df = pd.read_csv('travel_destinations.csv')

x = df[df["City"] == "Paris"]
print(x)
