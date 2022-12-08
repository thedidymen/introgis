import logging
import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from fiona.crs import from_epsg
import matplotlib.pyplot as plt

# Problem 2: Points to map (6 points)

# The problem 2 this week continues the process that we started last week, i.e. creating geometric point -objects and 
# putting them into a map. Here our aim is to plot a set of x and y coordinates that we should read from a 
# some_posts.csv comma separated file that contains following kind of data:

# lat,lon,timestamp,userid
# -24.980792492,31.484633302,2015-07-07 03:02,66487960
# -25.499224667,31.508905612,2015-07-07 03:18,65281761
# -24.342578456,30.930866066,2015-03-07 03:38,90916112
# -24.85461393,31.519718439,2015-10-07 05:04,37959089

# The data has 81379 rows and consists of locations and times of social media posts inside Kruger national park 
# in South Africa:

# Column 	Description
# lat 	y-coordinate of the post
# lon 	x-coordinate of the post
# timestamp 	Time when the post was uploaded
# userid 	userid

# Note: although the data is based on real social media data, it is heavily anonymized. Userids and timestamps have been randomized, i.e. they do not not match with real ones, also spatial accuracy of the data have been lowered.



if __name__ == "__main__":
    # level = logging.DEBUG
    # fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    # logging.basicConfig(level=level, format=fmt)

# Read the data into memory using Pandas
    data = pd.read_csv("Data/some_posts.csv")

# Create an empty column called geometry where you will store shapely Point objects
    data['geometry'] = None

# Iterate over the rows of the DataFrame and insert Point objects into column geometry (you need to use .loc indexer 
# to update the row, see materials
    for index, post in data.iterrows():
        data.loc[index, 'geometry'] = Point(data.loc[index, 'lat'], data.loc[index, 'lon'])

# Convert that DataFrame into a GeoDataFrame, see hints
# Update the CRS for coordinate system as WGS84 (i.e. epsg code: 4326)
    geo = gpd.GeoDataFrame(data, geometry='geometry', crs=from_epsg(4326))

# Save the data into a Shapefile called Kruger_posts.shp
    geo.to_file(r"Data/Kruger_posts.shp")

# Create a simple map of those points using a GIS software or using .plot() -funtion in Python. 
# Save it to GitHub as png file.
    geo.plot()
    plt.show()