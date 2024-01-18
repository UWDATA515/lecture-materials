# Read a CSV file (manually)
def read_csv(file_name):
    with open(file_name) as file:
        rows = []
        header = file.readline().rstrip('\n').split(',')
        for line in file:
            cols = line.rstrip('\n').split(',')
            row = {}
            for i in range(len(header)):
                row[header[i]] = cols[i]
            rows.append(row)
        return rows

def write_csv(rows, columns, output_file_name):
    with open(output_file_name, 'w') as file:
        # Print the header (column names) first
        print(f"{','.join(columns)}", file=file)
        for row in rows:
            values = []
            for col in columns:
                values.append(row[col])
            print(f"{','.join(values)}", file=file)
            # Or if you wanted to do this in one line with a map:
            # print(f"{','.join(map(lambda c : row[c], columns))}", file=file)

if __name__ == '__main__':
    file_rows = read_csv('pronto.csv')
    columns_we_want = [
        'trip_id',
        'starttime',
        'stoptime',
        'bikeid',
        'tripduration',
        'from_station_name',
        'to_station_name',
        'from_station_id',
        'to_station_id',
    ]
    write_csv(file_rows, columns_we_want, "output.csv")
