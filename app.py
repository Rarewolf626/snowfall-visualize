import csv
import mysql.connector as database
from dotenv import dotenv_values
from shapely import Polygon, Point
from shapely.wkt import loads

config = dotenv_values('.env')

connection = database.connect(user=config['USERNAME'], password=config['PASSWORD'], host=config['HOST'], database='weather')
cursor = connection.cursor()

# cursor.execute("""
#     SELECT time_start, latitude, longitude, sde 
#     FROM weather
#     WHERE ST_Contains(
#         ST_GeomFromText(
#             LOAD_FILE('california.wkt')
#         ),
#         POINT(longitude, latitude)
#     );
# """)

cursor.execute("""
    SELECT time_start, latitude, longitude, sde 
    FROM weather
    LIMIT 108000;
""")

## SELECT 108K rows and see if any fall in CA
   
results = cursor.fetchall()
print(len(results))

with open('california.wkt', 'r') as wkt_file:
    wkt_string = wkt_file.read()
california = loads(wkt_string)

in_ca = []

for row in results:
    point = Point(row[2], row[1]) # Lng, lat
    if california.contains(point):
        in_ca.append(row)

print(len(in_ca))
    

# with open('/Volumes/Untitled/ca_snow_data.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['time_start', 'latitude', 'longitude', 'sde'])
#     for row in results:
#         writer.writerow(row)

if connection:
    cursor.close()
    connection.close()
    print('MySQL connection is closed')