#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install geopandas


# In[7]:


import geopandas as gpd

path_to_shapefile19T1 = r"C:\Users\e105286\Desktop\DS and ML\2019_1T_CARRIL_BICI"
path_to_shapefile19T2 = r"C:\Users\e105286\Desktop\DS and ML\2019_2T_CARRIL_BICI"
path_to_shapefile19T3 = r"C:\Users\e105286\Desktop\DS and ML\2019_3T_CARRIL_BICI"
path_to_shapefile19T4 = r"C:\Users\e105286\Desktop\DS and ML\2019_4T_CARRIL_BICI"

gdf19T1 = gpd.read_file(path_to_shapefile19T1)
gdf19T2 = gpd.read_file(path_to_shapefile19T2)
gdf19T3 = gpd.read_file(path_to_shapefile19T3)
gdf19T4 = gpd.read_file(path_to_shapefile19T4)


# In[4]:


gdf19T1


# In[8]:


gdf19T2


# In[9]:


gdf19T3


# In[10]:


gdf19T4


# In[ ]:




