import geopandas as gpd
import matplotlib.pyplot as plt
from fiona.crs import from_epsg

def make_projection(title, color, data):
    # Plot the data
    data.plot(facecolor=color)
    # Add title
    plt.title(title)
    # Remove empty white space around the plot
    plt.tight_layout()


if __name__ == "__main__":
    # Filepath to the Europe borders Shapefile
    fp = "Data/Europe_borders.shp"

    # Read data
    data = gpd.read_file(fp)
    # print(data.head())
    # print(data.crs)

    # Let's take a copy of our layer
    data_proj = data.copy()

    # Reproject the geometries by replacing the values with projected ones
    data_proj = data_proj.to_crs(epsg=3035)
    # Determine the CRS of the GeoDataFrame
    data_proj.crs = from_epsg(3035)

    # Let's see what we have
    print(data_proj.crs)


    make_projection(title="WGS84 projection", color='gray', data=data)
    make_projection(title="ETRS Lambert Azimuthal Equal Area projection", color='blue', data=data_proj)

    # plt.show()

    # Ouput file path
    outfp = r"Data/Europe_borders_epsg3035.shp"

    # Save to disk
    data_proj.to_file(outfp)
