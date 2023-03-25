import csv
from shapely.wkt import loads
from shapely.geometry import Point

with open('california.wkt', 'r') as f:
    california_poly = loads(f.read())

with open('/Volumes/Untitled/ca_snow_data_raw.csv', 'r') as input_file, open('/Volumes/Untitled/ca_snow_data.csv', 'w', newline='') as output_file:
    reader = csv.DictReader(input_file)
    writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
    writer.writeheader()

    # Filter out points outside California polygon
    deleted_rows = 0
    total_rows = 0
    for row in reader:
        point = Point(float(row['longitude']), float(row['latitude']))
        if california_poly.contains(point):
            writer.writerow(row)
        else:
            deleted_rows += 1
        total_rows += 1

# Print results
print(f"Rows filtered: {deleted_rows}")
print(f"Total rows: {total_rows}")
