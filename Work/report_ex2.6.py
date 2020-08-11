import csv
from pprint import pprint


def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as file:
        data = csv.reader(file)
        for row in data:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


pprint(read_prices('Data/prices.csv'))
