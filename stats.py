import string
import re
import pandas as pd
import numpy as np
import time
import datetime

import argparse

class RideStats:

    def __init__(self):

        self.distance = ""
        self.moving_time = ""
        self.total_time = ""
        self.average_speed = ""
        self.max_speed = ""
        self.ascent = ""
        self.list = []

    def get_stats(self):

        df = pd.read_csv("Route.csv", index_col='time', parse_dates=True)

        v = df['vel'].loc[np.equal(df['moving'], 1)]

        self.distance = "<br>&nbspDistance: {0:.2f}&nbspkm".format(df['s'].iat[-1])
        self.moving_time = "<br>&nbspMoving Time: {0}".format(str(datetime.timedelta(seconds=df['elapsed'].iat[-1])))

        time_series = df.index.to_series()
        self.total_time = "<br>&nbspTotal Time: {0}".format(time_series.iat[-1] - time_series.iat[0])

        self.average_speed = "<br>&nbspAverage Speed: {0:.2f}&nbspkm/h".format(df['s'].iat[-1] * 3600 / df['elapsed'].iat[-1])

        self.max_speed = "<br>&nbspMax Speed: {0:.2f}&nbspkm/h".format(v.max())

        self.ascent = "<br>&nbspAscent: {0:.0f}&nbspm".format(df['asc'].iat[-1])

        self.list = (self.distance, self.moving_time, self.total_time, self.average_speed, self.max_speed, self.ascent)
        self.list = str(self.list).replace("'", "")
        self.list = str(self.list).replace("(", "")
        self.list = str(self.list).replace(")", "")
        self.list = str(self.list).replace(",", "")

        return self.list