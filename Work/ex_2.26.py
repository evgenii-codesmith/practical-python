import csv
from pprint import pprint


def read_portfolio(filename):
    file = open(filename)
    file_data = csv.reader(file)
    headers = next(file_data)
    converted = []
    types = [str, float, str, str, float, float, float, float, int]
    record = {}

    for line in file_data:
        record = {name: f(val) for name, f, val in zip(headers, types, line)}
        converted.append(record)

    return converted


pprint(read_portfolio('Work/Data/dowstocks.csv'))
