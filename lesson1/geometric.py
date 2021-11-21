from shapely.geometry import (
    Point, 
    LineString, 
    Polygon, 
    MultiPoint, 
    MultiLineString, 
    MultiPolygon, 
    box
)

if __name__ == "__main__":
    # Create Point geometric object(s) with coordinates
    point1 = Point(2.2, 4.2)
    point2 = Point(7.2, -25.1)
    point3 = Point(9.26, -2.456)
    point3D = Point(9.26, -2.456, 0.57)
    poly = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
    poly2 = Polygon([[p.x, p.y] for p in [point1, point2, point3]])

    # Create a MultiPoint object of our points 1,2 and 3
    multi_point = MultiPoint([point1, point2, point3])

    # It is also possible to pass coordinate tuples inside
    multi_point2 = MultiPoint([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

    # We can also create a MultiLineString with two lines
    line1 = LineString([point1, point2])

    line2 = LineString([point2, point3])

    multi_line = MultiLineString([line1, line2])

    # MultiPolygon can be done in a similar manner
    # Let's divide our world into western and eastern hemispheres with a hole on the western hemisphere
    # --------------------------------------------------------------------------------------------------
    # Let's create the exterior of the western part of the world
    west_exterior = [(-180, 90), (-180, -90), (0, -90), (0, 90)]

    # Let's create a hole --> remember there can be multiple holes, thus we need to have a list of hole(s).
    # Here we have just one.
    west_hole = [[(-170, 80), (-170, -80), (-10, -80), (-10, 80)]]

    # Create the Polygon
    west_poly = Polygon(shell=west_exterior, holes=west_hole)

    # Let's create the Polygon of our Eastern hemisphere polygon using bounding box
    # For bounding box we need to specify the lower-left corner coordinates and upper-right coordinates
    min_x, min_y = 0, -90

    max_x, max_y = 180, 90

    # Create the polygon using box() function
    east_poly_box = box(minx=min_x, miny=min_y, maxx=max_x, maxy=max_y)

    # Let's create our MultiPolygon. We can pass multiple Polygon -objects into our MultiPolygon as a list
    multi_poly = MultiPolygon([west_poly, east_poly_box])

    print("MultiPoint:", multi_point)
    print("MultiLine: ", multi_line)
    print("Bounding box: ", east_poly_box)
    print("MultiPoly: ", multi_poly)

    # Convex Hull of our MultiPoint --> https://en.wikipedia.org/wiki/Convex_hull
    convex = multi_point.convex_hull

    # How many lines do we have inside our MultiLineString?
    lines_count = len(multi_line)

    # Let's calculate the area of our MultiPolygon
    multi_poly_area = multi_poly.area

    # We can also access different items inside our geometry collections. We can e.g. access a single polygon from
    # our MultiPolygon -object by referring to the index
    # Let's calculate the area of our Western hemisphere (with a hole) which is at index 0
    west_area = multi_poly[0].area

    # We can check if we have a "valid" MultiPolygon. MultiPolygon is thought as valid if the individual polygons
    # does notintersect with each other. Here, because the polygons have a common 0-meridian, we should NOT have
    # a valid polygon. This can be really useful information when trying to find topological errors from your data
    valid = multi_poly.is_valid

    print("Convex hull of the points: ", convex)
    print("Number of lines in MultiLineString:", lines_count)
    print("Area of our MultiPolygon:", multi_poly_area)
    print("Area of our Western Hemisphere polygon:", west_area)
    print("Is polygon valid?: ", valid)
