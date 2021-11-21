from shapely.geometry import Point, LineString, Polygon

if __name__ == "__main__":
    # Create Point geometric object(s) with coordinates
    point1 = Point(2.2, 4.2)
    point2 = Point(7.2, -25.1)
    point3 = Point(9.26, -2.456)
    point3D = Point(9.26, -2.456, 0.57)

    # Create a LineString from our Point objects
    line = LineString([point1, point2, point3])

    # It is also possible to use coordinate tuples having the same outcome
    line2 = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])


    print(line)
    print(line2)
    type(line)

    # Get x and y coordinates of the line
    lxy = line.xy

    print(lxy)

    # Extract x coordinates
    line_x = lxy[0]
    # Extract y coordinates straight from the LineObject by referring to a array at index 1
    line_y = line.xy[1]

    print(line_x)
    print(line_y)

    # Get the lenght of the line
    l_length = line.length

    # Get the centroid of the line
    l_centroid = line.centroid

    # What type is the centroid?
    centroid_type = type(l_centroid)

    # Print the outputs
    print("Length of our line: {0:.2f}".format(l_length))
    print("Centroid of our line: ", l_centroid)
    print("Type of the centroid:", centroid_type)
