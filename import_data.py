import pandas as pd
import matplotlib.pyplot as plt

food_loss = pd.read_csv('Food Loss Data.csv')
temperature = pd.read_csv('matYearCountry.csv')
GDP = pd.read_csv('global_gdp.csv')

# print(GDP.head(5))
 
food_loss.head(5)
countries = food_loss["country"]

# see which year has the most information
data2022 = food_loss[food_loss['year'] == 2021]
data_per_year = {}
for year in food_loss['year'].unique():
    data_per_year[year] = data2022 = food_loss[food_loss['year'] == year]
    print(f'the year {year} has {data_per_year[year].shape[0]} datapoints')

data2022.shape[0] #nb of rows

print(countries.unique())

# investige row 'activity' (whole supply chain)