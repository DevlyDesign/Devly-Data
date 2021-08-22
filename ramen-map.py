#Ramen Data 
# https://www.kaggle.com/milangabriel/ramen-ratings-dataset

import pandas as pd
import geopandas as geopandas
import pycountry
import matplotlib.pyplot as plt

df = pd.read_csv('ramen-ratings.csv')

#The following function will take the country name and generate a country code.

#ALERT: need to clean data so that I do have country codes 
# for countries that this functions does not cover such as 'Taiwan'

def alpha3code(df_column):
    CODE=[]
    for country in df_column:
        try:
            code=pycountry.countries.get(name=country).alpha_3
           # .alpha_3 means 3-letter country code 
           # .alpha_2 means 2-letter country code
            CODE.append(code)
        except:
            CODE.append('None')
    return CODE

df['CODE']=alpha3code(df.Country)
# df[df.CODE=='None']
# # This filters the df to get an idea of how many CODE's there are that are 'None'

#Will need to take into account countrys the function does not have CODEs for

#note to self. can shorten this.
for each_row, row in df.iterrows():
    if row.Country =='Taiwan':
        df.at[each_row, 'CODE']='TWN'

for each_row, row in df.iterrows():
    if row.Country =='USA':
        df.at[each_row, 'CODE']='USA'

for each_row, row in df.iterrows():
    if row.Country =='South Korea':
        df.at[each_row, 'CODE']='KOR'

for each_row, row in df.iterrows():
    if row.Country =='Vietnam':
        df.at[each_row, 'CODE']='VNM'

for each_row, row in df.iterrows():
    if row.Country =='UK':
        df.at[each_row, 'CODE']='GBR'

for each_row, row in df.iterrows():
    if row.Country =='Holland':
        df.at[each_row, 'CODE']='NLD'

for each_row, row in df.iterrows():
    if row.Country =='Sarawak':
        df.at[each_row, 'CODE']='MYS'

for each_row, row in df.iterrows():
    if row.Country =='Dubai':
        df.at[each_row, 'CODE']='ARE'

#Using GeoPandas
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.columns=['pop_est', 'continent', 'name', 'CODE', 'gdp_md_est', 'geometry']

merge=pd.merge(world,df,on='CODE')
location=pd.read_csv('https://raw.githubusercontent.com/melanieshi0120/COVID-19_global_time_series_panel_data/master/data/countries_latitude_longitude.csv')
merge=merge.merge(location,on='name').sort_values(by='Stars',ascending=False).reset_index()

# plot confirmed cases world map 
merge.plot(column='Stars', 
           figsize=(100, 80),
           legend=True,cmap='coolwarm')
plt.title('Ramen Scores in Different Countries',fontsize=12)
# add countries names and numbers 
for i in range(0,2320):
    plt.text(float(merge.longitude[i]),float(merge.latitude[i]),"{}\n{}".format(merge.name[i],merge.Stars[i]),size=5)
plt.show()

##This graph is not the best way to display Top Ramen scores.
#Included is a graphic of how the graph looks like on tableau
#Moving on im interested in the average and count of 5 star ramens for each country 

#From the images included its actually shocking to see that Japan is not the highest average rated high frequency curry country,
#


