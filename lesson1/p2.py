from binascii import Error
from shapely.geometry import Point, LineString, Polygon
from p1 import createLineGeom, createPointGeom, createPolyGeom

# Problem 2: Attributes of geometries

# Write your codes into a single read_attributes.py -file and upload the script to your personal 
# GitHub Exercise-1 repository.

#     Create a function called getCentroid() that takes any kind of Shapely's geometric -object as 
#     input and returns a centroid of that geometry. Demonstrate the usage of the function.

def getCentroid(shp):
    return shp.centroid

#     Create a function called getArea() that takes a Shapely's Polygon -object as input and returns 
#     the area of that geometry. Demonstrate the usage of the function.

def getArea(shp):
    return shp.area

#     Create a function called getLength() takes either a Shapely's LineString or Polygon -object as 
#     input. Function should check the type of the input and returns the length of the line if input 
#     is LineString and length of the exterior ring if input is Polygon. If something else is passed 
#     to the function, it should tell the user --> "Error: LineString or Polygon geometries 
#     required!". Demonstrate the usage of the function.

def getLength(shp):
    if isinstance(shp, LineString) or isinstance(shp, Polygon):
        return shp.length
    raise Error("LineString or Polygon geometries required")


if __name__ == "__main__":
    coords = [
        (2.2, 4.2),
        (7.2, -25.1),
        (9.26, -2.456),
    ]
    point = Point(coords[0])
    line = LineString(coords)
    poly = Polygon(coords)

    shps = [point, line, poly]
    funcs = [getArea, getCentroid, getLength]
    for shp in shps:
        print()
        for func in funcs:
            try:
                print(func(shp))
            except Error as err:
                print(f"Error: {err}")
        