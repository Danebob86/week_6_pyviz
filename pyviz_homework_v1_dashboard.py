#!/usr/bin/env python
# coding: utf-8

# In[46]:


import panel as pn
pn.extension('plotly')
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from dotenv import load_dotenv

import warnings
warnings.filterwarnings('ignore')

import hvplot.pandas


# In[2]:


load_dotenv()
map_box_api = os.getenv("mapbox_token")
px.set_mapbox_access_token(map_box_api)
type(map_box_api)


# In[ ]:





# In[3]:


# housing units per year

## rental analysis


# In[ ]:





# In[4]:


sfo_data = pd.read_csv("C:/Users/danie/smu_files/sfo_neighborhoods_census_data.csv", index_col="year")
sfo_data.head()


# In[5]:


sfo_mean = sfo_data.groupby("year").mean()
sfo_mean


# In[6]:


housing_units_mean = sfo_mean["housing_units"]
housing_units_mean


# In[7]:


housing_units_plots = housing_units_mean.plot.bar(title='housing units in san francisco from 2010 to 2016')


# In[ ]:





# In[8]:


# housing costs in san francisco per year


# In[ ]:





# In[9]:


sfo_mean[['sale_price_sqr_foot','gross_rent']]


# In[10]:


gross_rent = sfo_mean['gross_rent']


# In[11]:


gross_rents_plot = gross_rent.plot(title= 'average gross rent by year')


# In[12]:


sale_price_sqr_foot=sfo_mean['sale_price_sqr_foot']


# In[13]:


rent_plot = sale_price_sqr_foot.plot(title = "average price per sqft by year")


# In[ ]:





# In[14]:


# average prices by neighborhood


# In[ ]:





# In[15]:


year_neighborhood = sfo_data.groupby(["year","neighborhood"]).mean().reset_index()
year_neighborhood.head(10)


# In[16]:


neighborhood_sales = year_neighborhood.hvplot.line(x='year',y='sale_price_sqr_foot', groupby='neighborhood')


# In[17]:


neighborhood_sales


# In[18]:


neighborhood_rents = year_neighborhood.hvplot.line(x='year',y='gross_rent', groupby='neighborhood')


# In[19]:


neighborhood_rents


# In[ ]:





# In[20]:


# top 10 most expensive neighborhoods in SFO


# In[ ]:





# In[21]:


ten_most_expensive=sfo_data.groupby(["neighborhood"]).mean().sort_values('sale_price_sqr_foot', ascending = False).head(10).reset_index()
ten_most_expensive


# In[22]:


top_10 = ten_most_expensive.hvplot.bar(x='neighborhood',y='sale_price_sqr_foot', title = 'top 10 expensive neighborhoods in SFO', rot = 45, height = 500)


# In[23]:


top_10


# In[ ]:





# In[24]:


# comparing cost to purchase versus rental income


# In[ ]:





# In[25]:


year_neighborhood.head()


# In[26]:


side_by_side=year_neighborhood.drop(['housing_units'], axis=1)
side_by_side.head()


# In[ ]:





# In[27]:


side_plot = side_by_side.hvplot.bar('year', groupby = 'neighborhood', rot=90, title = 'average price per square foot versus average monthly rent by year by neighborhood', height = 400)


# In[28]:


side_plot


# In[ ]:





# In[29]:


# neighborhood map


# In[ ]:





# In[30]:


coordinates = pd.read_csv('C:/Users/danie/smu_files/neighborhoods_coordinates.csv')
coordinates.head()


# In[31]:


map_data = sfo_data.groupby("neighborhood").mean().reset_index()
map_data.head()


# In[32]:


map_data.shape


# In[33]:


combined_map = pd.concat([coordinates,map_data], axis = 1, join = 'inner')
combined_map.head()


# In[34]:


scatter_price = px.scatter_mapbox(combined_map,
                 lat='Lat',
                 lon='Lon',
                 color='Neighborhood',
                 size='sale_price_sqr_foot',
                 zoom=11,
                 title = 'average sale price per square foot in san francisco')


# In[35]:


scatter_price


# In[36]:


scatter_rent = px.scatter_mapbox(combined_map,
                 lat='Lat',
                 lon='Lon',
                 color='Neighborhood',
                 size='gross_rent', 
                 zoom=11,
                 title = 'average rent price per square foot in san francisco')


# In[47]:


scatter_rent


# In[ ]:





# In[38]:


# dashboard 


# In[ ]:





# In[39]:


def get_price_per_sf():
    scatter_price
    return scatter_price


def get_rent_per_sf():
    scatter_rent
    return scatter_rent


# In[40]:


sf_analysis = pn.Column(
    
    '#real estate analysis of san francisco from 2010 to 2016',
    housing_units_plots.get_figure(),
    gross_rents_plot.get_figure(),
    rent_plot.get_figure()
    
)


# In[41]:


neighborhood_analysis = pn.Column(
    
    '#san francisco neighborhood real estate analysis',
    top_10,
    neighborhood_sales,
    neighborhood_rents,
    side_plot
    
)


# In[42]:


price_rent = pn.Column(
    
    '#visual map of average neighborhood prices per square foot in san francisco',
    scatter_price,
    scatter_rent
    
)


# In[43]:


dashboard = pn.Tabs(
    
    ('real estate prices', sf_analysis ),
    ('neighborhood analysis', neighborhood_analysis),
    ('price vs. rent', price_rent)
    
)


# In[48]:


dashboard.servable()


# In[ ]:





# In[45]:


# panel serve pyviz_homework_v1_dashboard.ipynb --log-level debug --show


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




