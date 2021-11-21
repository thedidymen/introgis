from shapely.geometry import Point, LineString, Polygon


if __name__ == "__main__":
    # Create Point geometric object(s) with coordinates
    point1 = Point(2.2, 4.2)
    point2 = Point(7.2, -25.1)
    point3 = Point(9.26, -2.456)
    point3D = Point(9.26, -2.456, 0.57)
    line = LineString([point1, point2, point3])
    line2 = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])


    # Create a Polygon from the coordinates
    poly = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

    # We can also use our previously created Point objects (same outcome)
    # --> notice that Polygon object requires x,y coordinates as input
    poly2 = Polygon([[p.x, p.y] for p in [point1, point2, point3]])


    # Geometry type can be accessed as a String
    poly_type = poly.geom_type

    # Using the Python's type function gives the type in a different format
    poly_type2 = type(poly)

    # Let's see how our Polygon looks like
    print(poly)
    print(poly2)
    print("Geometry type as text:", poly_type)
    print("Geometry how Python shows it:", poly_type2)

    # Let's create a bounding box of the world and make a whole in it
    # First we define our exterior
    world_exterior = [(-180, 90), (-180, -90), (180, -90), (180, 90)]

    # Let's create a single big hole where we leave ten decimal degrees at the boundaries of the world
    # Notice: there could be multiple holes, thus we need to provide a list of holes
    hole = [[(-170, 80), (-170, -80), (170, -80), (170, 80)]]

    # World without a hole
    world = Polygon(shell=world_exterior)

    # Now we can construct our Polygon with the hole inside
    world_has_a_hole = Polygon(shell=world_exterior, holes=hole)

    print(world)
    print(world_has_a_hole)
    print(type(world_has_a_hole))

    # Get the centroid of the Polygon
    world_centroid = world.centroid

    # Get the area of the Polygon
    world_area = world.area

    # Get the bounds of the Polygon (i.e. bounding box)
    world_bbox = world.bounds

    # Get the exterior of the Polygon
    world_ext = world.exterior

    # Get the length of the exterior
    world_ext_length = world_ext.length

    print("Poly centroid: ", world_centroid)
    print("Poly Area: ", world_area)
    print("Poly Bounding Box: ", world_bbox)
    print("Poly Exterior: ", world_ext)
    print("Poly Exterior Length: ", world_ext_length)
