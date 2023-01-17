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

food_loss['food_supply_stage'].value_counts()

food_loss_whole_chain = food_loss[food_loss['food_supply_stage'] == "Whole supply chain"]
food_loss_whole_chain['country'].value_counts()
food_loss_whole_chain['year'].value_counts()
food_loss_whole_chain['loss_percentage']



# food_loss['year'].shape[0] #nb of rows

# print(countries.unique())

# investige row 'activity' (whole supply chain)