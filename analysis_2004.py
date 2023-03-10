import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
pd.set_option('display.max_colwidth', None)
# from sklearn.linear_model import LinearRegression


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
fig_data = pd.DataFrame(columns=["Country Code", "loss_percentage"])
for code in fl2004["Country Code"].unique():
    addition = {"Country Code": code}
    addition["loss_percentage"] = np.mean(fl2004[fl2004["Country Code"] == code]["loss_percentage"])
    addition_df = pd.DataFrame(addition, index=[0])
    fig_data = pd.concat([fig_data, addition_df])

highest = fig_data["loss_percentage"].max()

fig = px.choropleth(
    fig_data,
    locations="Country Code",
    color="loss_percentage",
    range_color=(0,highest),
    labels={"loss_percentage" : "Average Loss Percentage [%]"}
)

fig.update_layout(
    title={
        'text':"Average loss percentage values for all countries, over all years",
    },
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
    )

fig.show()

sns.regplot(x='GDP2004',y='loss_percentage',data=fl2004,fit_reg=True) 
plt.title('Scatterplot of GDP and Loss Percentage, for all measurements')
plt.xlabel('GDPx')
plt.ylabel("Loss Percentage")
plt.show()
