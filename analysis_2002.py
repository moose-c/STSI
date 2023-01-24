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


fl2002=food_loss_whole_chain
fl2002=fl2002[fl2002.year == 2002]
fl2002=fl2002.join(GDP['2002'])
fl2002['GDP2002']=fl2002['2002']
del fl2002['2002']
fl2002=fl2002.join(temp['2002'])
fl2002['Temp2002']= fl2002['2002']
del fl2002['2002']
fl2002=fl2002.join(GDP['Country Code'])

fl2002 = fl2002.rename(columns={"Unnamed: 0": "country"})
fl2002 = fl2002.drop(columns=['m49_code','region', 'cpc_code', 'commodity', 'year', 'loss_quantity', 'loss_percentage_original', 'activity', 'food_supply_stage', 'treatment', 'cause_of_loss', 'sample_size', 'method_data_collection', 'reference', 'url', 'notes'])
fl2002["Temp2002"] = fl2002["Temp2002"].astype(float)

# statistical analysis

fl2002["loss_percentage"].corr(fl2002["Temp2002"])
fl2002.plot.scatter(x="Temp2002", y="loss_percentage")
plt.show()
print(fl2002.corr(method='pearson'))

# wereld kaartje

fig = px.choropleth(
    fl2002,
    locations="Country Code",
    color="loss_percentage",
    # hover_name="country"
    # labels={"Value": "GDP per capita"}
)

fig.show()