import gpxpy
import pandas as pd
import argparse
import sys
import datetime
from tkinter import filedialog

from FolderLocation import *
from gpxanalysis import *

files = getFolderList()


def get_data_frame():

    dfs = []
    for f in files:
        with open(f, 'r') as gpx_file:
            gpx = gpxpy.parse(gpx_file)

        points = gpx.tracks[0].segments[0].points

        df = pd.DataFrame.from_records(({'time' : pd.to_datetime(x.time), 'lon': x.longitude, 'lat' : x.latitude, 'alt' : x.elevation} for x in points), columns=['time', 'lon', 'lat', 'alt'], index='time')

        dfs.append(df)

    df = pd.concat(dfs, axis=0)
    df.sort_index(inplace=True)
    df = gpxAnalyse(df)

    df.to_csv("Route.csv", index=False)


    






