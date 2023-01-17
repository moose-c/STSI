import pandas as pd
import matplotlib.pyplot as plt

food_loss = pd.read_csv('Food Loss Data.csv')
temperature = pd.read_csv('matYearCountry.csv')


food_loss.plot()
countries = food_loss["country"]
print(countries.unique())
plt.show()
# https://datahub.io/core/global-temp#python