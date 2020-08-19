import csv
from pprint import pprint


def read_portfolio(filename):
    file = open(filename)
    data = csv.reader(file)
    headers = next(data)
    types = [str, int, float]
    converted = []
    for line in data:
        converted.append({x: f(val)
                          for x, f, val in zip(headers, types, line)})

    return converted


pprint(read_portfolio('Work/Data/portfolio.csv'))
