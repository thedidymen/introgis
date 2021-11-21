from shapely.geometry import Point, LineString, Polygon
from functools import reduce
import pandas as pd
# from p1 import createLineGeom, createPointGeom, createPolyGeom

# Problem 3: Reading coordinates from a file and creating a geometries

# Write your codes into a single file_coords_to_geom.py -file and upload the 
# script to your personal GitHub Exercise-1 repository.

# One of the "classical" problems in GIS is the situation where you have a set 
# of coordinates in a file and you need to get them into a map (or into a 
# GIS-software). Python is a really handy tool to solve this problem as with 
# Python it is basically possible to read data from any kind of input datafile 
# (such as csv-, txt-, excel-, or gpx-files (gps data) or from different 
# databases). So far, I haven't faced any kind of data or file that would be 
# impossible to read with Python.

# Thus, let's see how we can read data from a file and create Point -objects from 
# them that can be saved e.g. as a new Shapefile (we will learn this next week). 
# Our dataset travelTimes_2015_Helsinki.txt consist of travel times between specific 
# locations in Helsinki Region. The first four rows of our data looks like this:

#    from_id;to_id;fromid_toid;route_number;at;from_x;from_y;to_x;to_y;total_route_time;route_time;route_distance;route_total_lines
#    5861326;5785640;5861326_5785640;1;08:10;24.9704379;60.3119173;24.8560344;60.399940599999994;125.0;99.0;22917.6;2.0
#    5861326;5785641;5861326_5785641;1;08:10;24.9704379;60.3119173;24.8605682;60.4000135;123.0;102.0;23123.5;2.0
#    5861326;5785642;5861326_5785642;1;08:10;24.9704379;60.3119173;24.865102;60.4000863;125.0;103.0;23241.3;2.0

# Thus, we have many columns of data, but the few important ones are:
# Column 	Description
# from_x 	x-coordinate of the origin location (longitude)
# from_y 	y-coordinate of the origin location (latitude)
# to_x 	x-coordinate of the destination location (longitude)
# to_y 	y-coordinate of the destination location (latitude)
# total_route_time 	Travel time with public transportation at the route

# Tasks

#     Save the travelTimes_2015_Helsinki.txt into your computer.
#     Read 4 columns, i.e. 'from_x', 'from_y', 'to_x', 'to_y' from the data into Python using Pandas.
#     Create two lists called orig_points and dest_points
#     Iterate over the rows of your DataFrame and add Shapely Point -objects into the orig_points 
#       -list and dest_point -list representing the origin locations and destination locations accordingly.

def make_lines(orgin, dest):
    return [LineString([x, y]) for x, y in zip(orgin, dest)]

def lines_length_average(lines):
    return sum([line.length for line in lines]) / len(lines)


if __name__ == "__main__":
    df = pd.read_csv('travelTimes_2015_Helsinki.txt', sep=';')
    # print(df.head())

    # fr = df[["from_x", "from_y"]]
    # print(fr.head())
    
    orig_points = [Point(x, y) for x, y in zip(df["from_x"], df["from_y"])]
    dest_points = [Point(x, y) for x, y in zip(df['to_x'], df['to_y'])]

# Problem 4: Creating LineStrings that represent the movements (optional task for advanced students):

# This is an optional extra task for those who likes to learn even more. Write your codes into the same 
# file as in previous Problem (3).

#     Create a list called lines
#     Iterate over the origin and destination lists and create a Shapely LineString -object between the 
#       origin and destination point
#     Add that line into the lines -list.
#     Find out what is the average (Euclidian) distance of all the origin-destination LineStrings that 
#       we just created, and print it out.
#     To make things more reusable: write creation of the LineString and calculating the average 
#       distance into dedicated functions and use them.

    lines = [LineString([x, y]) for x, y in zip(orig_points, dest_points)]
    l_l_a = sum([line.length for line in lines]) / len(lines)

    print(l_l_a)

