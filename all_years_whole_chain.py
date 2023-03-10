import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
pd.set_option('display.max_colwidth', None)


food_loss = pd.read_csv('Food Loss Data.csv', index_col=1)
temperature = pd.read_csv('matYearCountry.csv', index_col=0)
GDP = pd.read_csv('global_gdp.csv', index_col=0)

food_loss_whole_chain = food_loss[food_loss['food_supply_stage'] == "Whole supply chain"]
food_loss_whole_chain = food_loss_whole_chain[food_loss_whole_chain['year'] < 2014]

thrown = 0
data = pd.DataFrame(columns=["country", "year", "loss_percentage", "GDP", "temperature"])
for index, row in food_loss_whole_chain.iterrows():
    addition = {}
    addition["country"] = row.name
    addition["year"] = row["year"]
    addition["loss_percentage"] = row["loss_percentage"]
    try:
        addition["temperature"] = temperature[addition["country"]][addition["year"]] # nu maar tot 
        addition["GDP"] = GDP[str(addition["year"])][addition["country"]] # dit moet nog uit de df
        addition_df = pd.DataFrame(addition, index=[0])
        data = pd.concat([data, addition_df])
    except KeyError:
        thrown += 1
        pass
    
##
data = data.set_index('country')
data = data.drop(columns=["year"])
    
print(thrown)

data=data.join(GDP['Country Code'])

fig_data = pd.DataFrame(columns=["Country Code", "loss_percentage"])
for code in data["Country Code"].unique():
    addition = {"Country Code": code}
    addition["loss_percentage"] = np.average(data[data["Country Code"] == code]["loss_percentage"])
    addition_df = pd.DataFrame(addition, index=[0])
    fig_data = pd.concat([fig_data, addition_df])


fig = px.choropleth(
    fig_data,
    locations="Country Code",
    color="loss_percentage",
    # hover_name="country"
    # labels={"Value": "GDP per capita"}
)

fig.show()