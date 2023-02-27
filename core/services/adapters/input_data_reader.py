import csv


def read_data(file_path, delimiter):
    raw_data = []
    with open(file_path, newline='') as input_file:
        rows = csv.DictReader(input_file, delimiter=delimiter)
        for row in rows:
            raw_data.append(row)
    return raw_data
