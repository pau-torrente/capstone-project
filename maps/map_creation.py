import folium
from folium.plugins import HeatMap
import pandas as pd
import json
import numpy as np

gener_info = pd.read_csv('data/2021_01_Gener_BicingNou_INFORMACIO.csv')
locations = gener_info[['name', 'lat', 'lon']].groupby('name').mean().reset_index()

frequencies = pd.DataFrame(np.transpose(np.unique(gener_info['station_id'], return_counts=True)))
frequencies.columns = ['station_id', 'frequency']

stations = pd.DataFrame(np.unique(gener_info[['station_id','lat', 'lon']], axis = 0))
stations.columns = ['station_id', 'lat', 'lon']

frequencies  = pd.merge(left = frequencies, right = stations, on = 'station_id', how = 'left')
heatmap_data = [(locations.loc[i]['lat'], locations.loc[i]['lon'], frequencies.loc[i]['frequency']) for i in range(locations.shape[0])]

map = folium.Map(location=[41.3870154, 2.1700471], zoom_start=13)

for i in range(locations.shape[0]):
    folium.Marker([locations.loc[i]['lat'], locations.loc[i]['lon']], popup=locations.loc[i]['name']).add_to(map)

with open('data/CARRIL_BICI.geojson') as f:
    bikelane_data = json.load(f)
folium.GeoJson(bikelane_data).add_to(map)

HeatMap(heatmap_data).add_to(map)

map.save('maps/map.html')

######################################

map_no_markers = folium.Map(location=[41.3870154, 2.1700471], zoom_start=13)

folium.GeoJson(bikelane_data).add_to(map_no_markers)

HeatMap(heatmap_data).add_to(map_no_markers)

map_no_markers.save('maps/map_no_markers.html')

