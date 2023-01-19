import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_colwidth', None)


food_loss = pd.read_csv('Food Loss Data.csv', index_col=1)
temperature = pd.read_csv('matYearCountry.csv')
GDP = pd.read_csv('global_gdp.csv', index_col=0)

# print(GDP.head(5))
 
food_loss.head(5)
#countries = food_loss["country"]

# see which year has the most information
counts = food_loss['year'].value_counts()
counts[counts > 100]

food_loss['year'].shape[0] #nb of rows

#print(countries.unique())

# GDP
# Total number of datapoints
counts=GDP['2021'].value_counts()
counts

#GDP2021= pd.DataFrame()
#GDP2021['Country']=GDP['Country Name']
#GDP2021['2021']=GDP['2021']
#print(GDP2021.head())

food_loss_whole_chain = food_loss[food_loss['food_supply_stage'] == "Whole supply chain"]
#print(food_loss_whole_chain['loss_percentage'].head())


#data = pd.DataFrame(columns=[ "year", "loss_percentage", "GDP", "temperature"])
#for index, row in food_loss_whole_chain.iterrows():
    #addition = {}
    
    #addition["year"] = row["year"]
    #addition["loss_percentage"] = row["loss_percentage"]
   # addition["temperature"] = temperature[addition["country"]][addition["year"]] # nu maar tot 2015
    #addition["GDP"] = GDP[addition['year']]
   
    #data.append(addition)

temperature = temperature.astype({'year':'int'})
temp=temperature.transpose()
temp.rename(columns=temp.iloc[0], inplace = True)
temp.drop(temp.index[0], inplace = True)

print(temp.head())

FL=food_loss_whole_chain.join(GDP['2021'])
FL['GDP2021']=FL['2021']

fl2=food_loss_whole_chain
fl2=fl2[fl2.year == 2002]

FL2=fl2.join(GDP['2002'],temp['2002'])
print(FL2)


#FL2.to_csv('out.csv')