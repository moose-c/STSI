import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
pd.set_option('display.max_colwidth', None)


food_loss = pd.read_csv('Food Loss Data.csv', index_col=1)
temperature = pd.read_csv('matYearCountry.csv')
GDP = pd.read_csv('global_gdp.csv', index_col=0)

food_loss_whole_chain = food_loss#[food_loss['food_supply_stage'] == "Whole supply chain"]

temperature = temperature.astype(str)

temp=temperature.transpose()
temp.columns = temp.iloc[0]
temp = temp[1:]


fl2004=food_loss_whole_chain
fl2004=fl2004[fl2004.year == 2004]
fl2004=fl2004.join(GDP['2004'])
fl2004['GDP2004']=fl2004['2004']
del fl2004['2004']
fl2004=fl2004.join(temp['2004'])
fl2004['Temp2004']= fl2004['2004']
del fl2004['2004']
fl2004=fl2004.join(GDP['Country Code'])

fl2004 = fl2004.rename(columns={"Unnamed: 0": "country"})
fl2004 = fl2004.drop(columns=['m49_code','region', 'cpc_code', 'commodity', 'year', 'loss_quantity', 'loss_percentage_original', 'activity', 'food_supply_stage', 'treatment', 'cause_of_loss', 'sample_size', 'method_data_collection', 'reference', 'url', 'notes'])
fl2004["Temp2004"] = fl2004["Temp2004"].astype(float)

# statistical analysis

fl2004["loss_percentage"].corr(fl2004["Temp2004"])
fl2004.plot.scatter(x="Temp2004", y="loss_percentage")
plt.show()
print(fl2004.corr(method='pearson'))

# wereld kaartje

fig = px.choropleth(
    fl2004,
    locations="Country Code",
    color="loss_percentage",
    # hover_name="country"
    # labels={"Value": "GDP per capita"}
)

#fig.show()