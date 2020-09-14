import pandas as pd
import numpy as np
import folium
import sys

import argparse

from FolderLocation import *
from gpx2csv import *
from gpxanalysis import *
from stats import RideStats

get_data_frame()
cts = RideStats()
cts.get_stats()
zoom_level = 11

df = pd.read_csv("Route.csv")
name = "Tour.html"

latMin = min(df['lat'])
lonMin = min(df['lon'])
latMax = max(df['lat'])
lonMax = max(df['lon'])
lat_start = df['lat'].iloc[0]
lon_start = df['lon'].iloc[0]
lat_end = df['lat'].iloc[-5]
lon_end = df['lon'].iloc[-5]

m = folium.Map(location=[(latMax + latMin) * 0.5, (lonMax + lonMin) * 0.5],
               zoom_start=zoom_level, tiles='Stamen Watercolor', control_scale=True)

n = 100

colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
          'white', 'pink', 'lightblue', 'gray', 'black', 'lightgray']

for _, day in df.groupby(df.index.dayofyear):
    p = list(zip(day['lat'].to_numpy()[::n], day['lon'].to_numpy()[::n]))
    folium.PolyLine(p, color=colors.pop(0), weight=4, opacity=1).add_to(m)


text = f"<b>&nbspTour details:</b><br>{cts.get_stats()}"
folium.map.Marker(
    [53.519856, -2.186120],
    icon=DivIcon(
        icon_size=(350, 36),
        icon_anchor=(150, 0),
        html='<div style="font-size: 14pt; '
             'background: white;'
             'color: black; '
             'font-family: courier new;'
             'border: 2px solid black">%s</div>;' % text,
    )
).add_to(m)

folium.Marker(
    location=[lat_start, lon_start],
    icon=folium.Icon(color='green', prefix='fa', icon='bicycle'),
).add_to(m)

folium.Marker(
    location=[lat_end, lon_end],
    icon=folium.Icon(color='red', prefix='fa', icon='bicycle'),
).add_to(m)

m.save(name)

print()
