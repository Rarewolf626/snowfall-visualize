import csv

start_time = 1665802800
increment = 24 * 60 * 60  # 24 hours in seconds

with open('ca_snow_data.csv', 'r') as csvfile_in, open('data_final.csv', 'w', newline='') as csvfile_out:
    reader = csv.reader(csvfile_in)
    writer = csv.writer(csvfile_out)
    header = next(reader)  # skip header row
    writer.writerow(header)  # write header row to output
    for row in reader:
        time_start = int(row[0])
        if (time_start - start_time) % increment == 0:
            writer.writerow(row)
