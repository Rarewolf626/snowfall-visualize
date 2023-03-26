import csv
import mysql.connector as database
from dotenv import dotenv_values

config = dotenv_values('.env')

connection = database.connect(
    user=config['USERNAME'], 
    password=config['PASSWORD'], 
    host=config['HOST'], 
    database='weather'
)

cursor = connection.cursor()

with open('california.wkt', 'r') as wkt_file:
    wkt_string = wkt_file.read()

cursor.execute(f"""
    SELECT time_start, latitude, longitude, sde 
    FROM weather
    WHERE time_start > 1665792000
    AND ST_Contains(
        ST_GeomFromText(
            '{wkt_string}'
        ),
        POINT(longitude, latitude)
    );
""") # selects points in CA bounding box after October 15, 2022

with open('/Volumes/Untitled/ca_snow_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['time_start', 'latitude', 'longitude', 'sde'])
    batch_size = 10000
    while True:
        results = cursor.fetchmany(batch_size)
        if not results:
            break
        for row in results:
            writer.writerow(row)

if connection:
    cursor.close()
    connection.close()
    print('MySQL connection is closed')