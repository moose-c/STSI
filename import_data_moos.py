import pandas as pd
import matplotlib.pyplot as plt
import datetime
from dateutil.relativedelta import relativedelta
pd.set_option('display.max_colwidth', None)

food_loss = pd.read_csv('Food Loss Data.csv')
GDP = pd.read_csv('global_gdp.csv', index_col=0)
globaltempbycountry = pd.read_csv('GlobalLandTemperaturesByCountry.csv')
temperature_anomalies = pd.read_csv('Environment_Temperature_change_E_All_Data_(Normalized).csv', encoding= 'unicode_escape')

# for country in globaltempbycountry["Country"].unique():
#     rows = globaltempbycountry[globaltempbycountry["Country"] == country]
#     useful_rows = [row for index, row in rows.iterrows() if 1951 <= int(row["dt"].split("-")[0]) <= 1980]
# list = []
# date = datetime.datetime(1959, 12, 1)
# while date < datetime.datetime(1981, 1, 1):
#     list.append(date.strftime('%Y-%m-%d'))
#     date += relativedelta(months=1)
# # useful_rows = rows[1951 <= int(rows["dt"].split("-")[0]) <= 1980]
# useful_rows = rows[rows['dt'].isin(list)]

# print(GDP.head(5))
 
food_loss.head(5)
countries = food_loss["country"]

# see which year has the most information
counts = food_loss['year'].value_counts()
counts[counts > 100]

food_loss['food_supply_stage'].value_counts()

food_loss_whole_chain = food_loss[food_loss['food_supply_stage'] == "Whole supply chain"]

food_loss_whole_chain['country'].value_counts()
food_loss_whole_chain['year'].value_counts()
food_loss_whole_chain['loss_percentage']



# food_loss['year'].shape[0] #nb of rows

# print(countries.unique())

# investige row 'activity' (whole supply chain)

# decipher temperature data
# temperature['Albania'][2010]

# make usable dataset
data = pd.DataFrame(columns=["country", "year", "loss_percentage", "GDP", "temperature"])
for index, row in food_loss_whole_chain.iterrows():
    addition = {}
    addition["country"] = row["country"]
    addition["year"] = row["year"]
    addition["loss_percentage"] = row["loss_percentage"]
    # addition["temperature"] = temperature[addition["country"]][addition["year"]] # nu maar tot 2015
    addition["GDP"] = 0 # dit moet nog uit de df
    data.append(addition)