from shapely.geometry import Point, LineString, Polygon

# Problem 1: Creating basic geometries

# Write your codes into a single create_geometries.py -file and upload the script 
# to your personal GitHub Exercise-1 repository.

#     Create a function called createPointGeom() that has two parameters (x_coord, y_coord). 
#     Function should create a shapely Point geometry object and return that. Demonstrate the 
#     usage of the function by creating Point -objects with the function.

def createPointGeom(x, y):
    return Point(x, y)

#     Create a function called createLineGeom() that takes a list of Shapely Point objects 
#     as parameter and returns a LineString object of those input points. Function should 
#     first check that the input list really contains Shapely Point(s). Demonstrate the usage 
#     of the function by creating LineString -objects with the function.

def createLineGeom(pointlist):
    try:
        for point in pointlist:
            if not isinstance(point, Point):
                raise TypeError
    except TypeError:
        print(f"{type(point)} not of type: {Point}")

    return LineString(pointlist)

#     Create a function called createPolyGeom() that takes a list of coordinate tuples OR 
#     a list of Shapely Point objects and creates/returns a Polygon object of the input data. 
#     Both ways of passing the data to the function should be working. Demonstrate the usage 
#     of the function by passing data first with coordinate-tuples and then with Point -objects.

def createPolyGeom(coords):
    if isinstance(coords[0], Point):
        return Polygon([[p.x, p.y] for p in coords])
    return Polygon(coords)


if __name__ == "__main__":
    coords = [
        (2.2, 4.2),
        (7.2, -25.1),
        (9.26, -2.456),
    ]
    points = [createPointGeom(x, y) for x, y in coords]
    lines = createLineGeom(points)
    lines = createLineGeom(coords)
    poly = createPolyGeom(points)
    poly = createPolyGeom(coords)