import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
pd.set_option('display.max_colwidth', None)


food_loss = pd.read_csv('Food Loss Data.csv', index_col=1)
temperature = pd.read_csv('matYearCountry.csv')
GDP = pd.read_csv('global_gdp.csv', index_col=0)

food_loss_whole_chain = food_loss[food_loss['food_supply_stage'] == "Whole supply chain"]
food_loss_whole_chain = food_loss_whole_chain[food_loss_whole_chain['year'] < 2014]

data = pd.DataFrame(columns=["country", "year", "loss_percentage", "GDP", "temperature"])
for index, row in food_loss_whole_chain.iterrows():
    addition = {}
    addition["country"] = row.name
    addition["year"] = row["year"]
    addition["loss_percentage"] = row["loss_percentage"]
    addition["temperature"] = temperature[addition["country"]][addition["year"]] # nu maar tot 2014
    addition["GDP"] = GDP[addition["year"]][addition["country"]] # dit moet nog uit de df
    data.append(addition)