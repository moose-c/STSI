import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
pd.set_option('display.max_colwidth', None)
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression

def calculate_pvalues(df):
    dfcols = pd.DataFrame(columns=df.columns)
    pvalues = dfcols.transpose().join(dfcols, how='outer')
    for r in df.columns:
        for c in df.columns:
            tmp = df[df[r].notnull() & df[c].notnull()]
            pvalues[r][c] = pearsonr(tmp[r], tmp[c])
    return pvalues

food_loss = pd.read_csv('Food Loss Data.csv', index_col=1)
temperature = pd.read_csv('matYearCountry.csv', index_col=0)
GDP = pd.read_csv('GDP_per_capita.csv', index_col=0)

food_loss = food_loss[food_loss['year'] < 2014]

thrown = 0
data = pd.DataFrame(columns=["country", "year", "loss_percentage", "GDP", "temperature"])
for index, row in food_loss.iterrows():
    addition = {}
    addition["country"] = row.name
    addition["year"] = row["year"]
    addition["loss_percentage"] = row["loss_percentage"]
    try:
        addition["temperature"] = temperature[addition["country"]][addition["year"]] 
        addition["GDP"] = GDP[str(addition["year"])][addition["country"]] 
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
    addition["loss_percentage"] = np.mean(data[data["Country Code"] == code]["loss_percentage"])
    addition_df = pd.DataFrame(addition, index=[0])
    fig_data = pd.concat([fig_data, addition_df])

highest = fig_data["loss_percentage"].max()

print(data.corr())

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



data = data.drop(columns = ["Country Code"])
print(calculate_pvalues(data).to_string())


# regression gdp & loss
data = data.dropna()
regression_gdp_loss = LinearRegression()
regression_gdp_loss.fit(np.array(data["GDP"]).reshape(-1,1), np.array(data["loss_percentage"]).reshape(-1,1))
Y_pred = regression_gdp_loss.predict(np.array(data["GDP"]).reshape(-1,1))

print(f'gdp & loss score {regression_gdp_loss.score(np.array(data["GDP"]).reshape(-1,1), np.array(data["loss_percentage"]).reshape(-1,1))}') # R^2
print(f'gdp and loss slope {regression_gdp_loss.coef_}')  #Slope
print(f'gdp and loss intercept {regression_gdp_loss.intercept_}')  # Intercept

plt.scatter(data['GDP'],data['loss_percentage'], alpha=0.3) 
plt.plot(data["GDP"], Y_pred, color="red")
plt.title('Scatterplot of GDP and Loss Percentage, for all measurements')
plt.ylabel("Loss Percentage [%]")
plt.xlabel("GDP per Capita [Current USD]")
plt.savefig("GDP & Loss", bbox_inches="tight")
plt.show()

# regression temp & loss

regression_temp_loss = LinearRegression()
regression_temp_loss.fit(np.array(data["temperature"]).reshape(-1,1), np.array(data["loss_percentage"]).reshape(-1,1))
Y_pred = regression_temp_loss.predict(np.array(data["temperature"]).reshape(-1,1))

print(f'temp & loss score {regression_temp_loss.score(np.array(data["temperature"]).reshape(-1,1), np.array(data["loss_percentage"]).reshape(-1,1))}') # R^2
print(f'temp and loss slope {regression_temp_loss.coef_}')  #Slope
print(f'temp and loss intercept {regression_temp_loss.intercept_}')  # Intercept

plt.scatter(data['temperature'],data['loss_percentage'], alpha=0.3) 
plt.plot(data["temperature"], Y_pred, color="red")
plt.title('Scatterplot of Temperature and Loss Percentage, for all measurements')
plt.ylabel("Loss Percentage [%]")
plt.xlabel("Temperature [°C]")
plt.savefig("Temperature & Loss", bbox_inches="tight")
plt.show()

# regression gdp & loss

regression_temp_gdp = LinearRegression()
regression_temp_gdp.fit(np.array(data["temperature"]).reshape(-1,1), np.array(data["GDP"]).reshape(-1,1))
Y_pred = regression_temp_gdp.predict(np.array(data["temperature"]).reshape(-1,1))

print(f'gdp & temp score {regression_temp_gdp.score(np.array(data["temperature"]).reshape(-1,1), np.array(data["GDP"]).reshape(-1,1))}') # R^2
print(f'gdp and temp slope {regression_temp_gdp.coef_}')  #Slope
print(f'gdp and temp intercept {regression_temp_gdp.intercept_}')  # Intercept

plt.scatter(data['temperature'],data['GDP'], alpha=0.3) 
plt.plot(data["temperature"], Y_pred, color="red")
plt.title('Scatterplot of temperature and GDP, for all measurements')
plt.ylabel("GDP per Capita [Current USD]")
plt.xlabel("Temperature [°C]")
plt.savefig("GDP & temp", bbox_inches="tight")
plt.show()