# report.py
#
# Exercise 2.4
import csv
from pprint import pprint


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(f)

        for row in rows:
            shares_dict = {}
            shares_dict['name'] = row[0]
            shares_dict['shares'] = int(row[1])
            shares_dict['price'] = float(row[2])
            portfolio.append(shares_dict)

    return portfolio


pprint(read_portfolio('Data/portfolio.csv'))
