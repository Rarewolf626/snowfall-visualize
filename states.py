import os
import shapefile
from shapely.geometry import shape, Polygon

# Open the shapefile
sf = shapefile.Reader("/Users/elijahsaltzman/fire/state_borders/tl_2022_us_state.shp")

# Create the output directory if it doesn't exist
if not os.path.exists("states"):
    os.makedirs("states")

# Loop over each record in the shapefile
conus_polygons = []
for i in range(sf.numRecords):
    # Extract the state name from the record
    state = sf.record(i)[6].lower().replace(' ', '_')
    if state == 'nebraska':

        # Extract the shape data from the record and convert to shapely object
        shape_data = shape(sf.shape(i))
        
        # If the shape data is a multipolygon, find the largest polygon
        if shape_data.geom_type == 'MultiPolygon':
            largest_area = 0
            for polygon in shape_data.geoms:
                area = polygon.area
                if area > largest_area:
                    largest_area = area
                    largest_polygon = polygon
            shape_data = largest_polygon

        # Save the CONUS border as a WKT file
        with open("nebraska.wkt", "w") as f:
            f.write(shape_data.wkt)
