import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_colwidth', None)


food_loss = pd.read_csv('Food Loss Data.csv')
temperature = pd.read_csv('matYearCountry.csv')
GDP = pd.read_csv('global_gdp.csv')

# print(GDP.head(5))
 
food_loss.head(5)
countries = food_loss["country"]

# see which year has the most information
counts = food_loss['year'].value_counts()
counts[counts > 100]

food_loss['year'].shape[0] #nb of rows

#print(countries.unique())

# GDP
# Total number of datapoints
counts=GDP['2021'].value_counts()
counts

GDP2021= pd.DataFrame()
GDP2021['Country']=GDP['Country Name']
GDP2021['2021']=GDP['2021']
print(GDP2021.head())

food_loss_whole_chain = food_loss[food_loss['food_supply_stage'] == "Whole supply chain"]
data = pd.DataFrame(columns=["country", "year", "loss_percentage", "GDP", "temperature"])
for index, row in food_loss_whole_chain.iterrows():
    addition = {}
    addition["country"] = row["country"]
    addition["year"] = row["year"]
    addition["loss_percentage"] = row["loss_percentage"]
   # addition["temperature"] = temperature[addition["country"]][addition["year"]] # nu maar tot 2015
    addition["GDP"] = GDP2021[addition["country"]][addition['2021']]
    data.append(addition)

print(data.head())
