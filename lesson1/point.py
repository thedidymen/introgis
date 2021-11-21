from shapely.geometry import Point, LineString, Polygon

if __name__ == "__main__":

    # Create Point geometric object(s) with coordinates
    point1 = Point(2.2, 4.2)
    point2 = Point(7.2, -25.1)
    point3 = Point(9.26, -2.456)
    point3D = Point(9.26, -2.456, 0.57)

    # What is the type of the point?
    point_type = type(point1)

    print(point1)
    print(point3D)
    print(type(point1))

    point_coords = point1.coords
    xy = point_coords.xy
    x = point1.x
    y = point1.y
    print(type(point_coords))
    print(xy)
    print(x)
    print(y)

    point_dist = point1.distance(point2)
    print("Distance between the points is {0:.2f} decimal degrees".format(point_dist))
