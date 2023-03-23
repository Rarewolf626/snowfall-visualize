import csv
import mysql.connector as database
from dotenv import dotenv_values

config = dotenv_values('.env')

connection = database.connect(user=config['USERNAME'], password=config['PASSWORD'], host=config['HOST'], database='weather')
cursor = connection.cursor()

cursor.execute("""
    SELECT time_start, latitude, longitude, sde 
    FROM weather
    WHERE MBRContains(
        GeomFromText(
            LOAD_FILE('california.wkt')
        ),
        POINT(longitude, latitude)
    );
""")
               
# Write column names to csv file
with open('/Volumes/Untitled/ca_snow_data.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['time_start', 'latitude', 'longitude', 'sde'])

# Write query rows to CSV in batches of 1000 to avoid memory/performance issues
batch_size = 1000
while True:
    rows = cursor.fetchmany(batch_size)
    if not rows:
        break
    with open('/Volumes/Untitled/ca_snow_data.csv', 'a', newline='') as csvfile: # Open CSV in append mode
        writer = csv.writer(csvfile)
        for row in rows:
            writer.writerow(row)

if connection:
    cursor.close()
    connection.close()
    print('MySQL connection is closed')