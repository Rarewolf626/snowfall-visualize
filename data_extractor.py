import csv
import mysql.connector as database
from dotenv import dotenv_values
from shapely import wkt
from shapely.geometry import MultiPoint, Point, Polygon

class DataExtractor:
    def __init__(self, state, start_time=1665792000, end_time=None, increment=24 * 60 * 60):
        self.state = state
        self.start_time = start_time
        self.end_time = end_time
        self.increment = increment # defaults to one day between data points
        self.config = dotenv_values('.env')
        self.connection = database.connect(
            user=self.config['USERNAME'], 
            password=self.config['PASSWORD'], 
            host=self.config['HOST'], 
            database='weather'
        )
        with open(f'states/{self.state}.wkt', 'r') as wkt_file:
            self.wkt_string = wkt_file.read()
        self.state_polygon = wkt.loads(self.wkt_string)
        # Create a bounding box around the state polygon
        self.bbox = Polygon(self.state_polygon.envelope)
        self.query = f"""
            SELECT time_start, latitude, longitude, sde 
            FROM weather
            WHERE time_start > {self.start_time}
            AND MOD(time_start - {self.start_time}, {self.increment}) = 0
            AND latitude > {self.bbox.bounds[1]}
            AND latitude < {self.bbox.bounds[3]}
            AND longitude > {self.bbox.bounds[0]}
            AND longitude < {self.bbox.bounds[2]}
        """

    
    def in_state(self, lng, lat):
        point = Point(lng, lat)
        return self.state_polygon.contains(point)

    def extract_data(self):
        if self.end_time is not None:
            query += f" AND time_start < {self.end_time}"

        # Execute the SQL query and write the results to a CSV file
        cursor = self.connection.cursor()
        cursor.execute(self.query)
        with open(f'snow_csv_data/{self.state}_snow_data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['time_start', 'latitude', 'longitude', 'sde'])
            batch_size = 100
            while True:
                results = cursor.fetchmany(batch_size)
                if not results:
                    break
                for row in results:
                    # Reduce rows to just rows within the exact state polygon, not just bbox used in query
                    if self.in_state(row[2], row[1]): # lng, lat
                        writer.writerow(row)

states = ['alabama', 'arkansas', 'connecticut', 'delaware', 'florida', 'georgia', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'michigan', 'minnesota', 'mississippi', 'missouri', 'nebraska', 'new_hampshire', 'new_jersey', 'new_york', 'north_carolina', 'north_dakota', 'ohio', 'oklahoma', 'pennsylvania', 'rhode_island', 'south_carolina', 'south_dakota', 'tennessee', 'texas', 'vermont', 'virginia', 'west_virginia', 'wisconsin']


for state in states:
    print(state)
    extractor = DataExtractor(state)
    extractor.extract_data()