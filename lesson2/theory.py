
import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
from fiona.crs import from_epsg


if __name__ == "__main__":
    fp = "Data/DAMSELFISH_distributions.shp"
    data = gpd.read_file(fp)
    # print(type(data))
    # print(data.head())
    # data.plot()
    # plt.show()

    # # Create a output path for the data
    # out = r"Data/DAMSELFISH_distributions_SELECTION.shp"
    # # Select first 50 rows
    # selection = data[0:50]
    # # Write those rows into a new Shapefile (the default output file format is Shapefile)
    # selection.to_file(out)

    # selection = data[0:5]

    # for index, row in selection.iterrows():
    #     poly_area = row['geometry'].area
    #     print("Polygon area at index {0} is: {1:.3f}".format(index, poly_area))

    # data['area'] = data.area
    # print(data['area'].head(2))

    # # Maximum area
    # max_area = data['area'].max()
    # # Mean area
    # mean_area = data['area'].mean()

    # print("Max area: %s\nMean area: %s" % (round(max_area, 2), round(mean_area, 2)))

    # newdata = gpd.GeoDataFrame()
    # # print(newdata)

    # coordinates = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
    # # Create a Shapely polygon from the coordinate-tuple list
    # poly = Polygon(coordinates)
    # newdata.loc[0, 'geometry'] = poly
    # newdata.loc[0, 'Location'] = 'Senaatintori'
    # # Set the GeoDataFrame's coordinate system to WGS84
    # newdata.crs = from_epsg(4326)

    # # Let's see how the crs definition looks like
    # print(newdata.crs)

    # # Determine the output path for the Shapefile
    # outfp = r"Data/Senaatintori.shp"

    # # Write the data into that Shapefile
    # newdata.to_file(outfp)

    grouped = data.groupby('BINOMIAL')
    # # print(grouped)

    # for key, values in grouped:
    #     individual_fish = values
    #     print(individual_fish)
    #     print(key)

    # Determine outputpath
    outFolder = r"Data"

    # Create a new folder called 'Results' (if does not exist) to that folder using os.makedirs() function
    resultFolder = os.path.join(outFolder, 'Results')
    if not os.path.exists(resultFolder):
        os.makedirs(resultFolder)

    # Iterate over the
    for key, values in grouped:
        # Format the filename (replace spaces with underscores)
        outName = "%s.shp" % key.replace(" ", "_")

        # Print some information for the user
        print("Processing: %s" % key)

        # Create an output path
        outpath = os.path.join(resultFolder, outName)

        # Export the data
        values.to_file(outpath)