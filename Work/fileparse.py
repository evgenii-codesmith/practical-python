# fileparse.py
#
# Exercise 3.3
import csv
from pprint import pprint


def parse_csv(filename, select=None, types=None):
    """
    Parse a CSV file into a list of records
    """

    with open(filename) as f:
        data = csv.reader(f)

        headers = next(data)
        records = []
        indexes = None

        if select:
            indexes = [headers.index(colname) for colname in select]

        for line in data:
            if not line:
                continue
            if indexes:
                line = [line[i] for i in indexes]
                if types:
                    line = [f(val) for f, val in zip(types, line)]
                record = dict(zip(select, line))
            else:
                record = dict(zip(headers, line))

            records.append(record)

    return records


pprint(parse_csv('Work/Data/portfolio.csv',
                 select=['name', 'price', 'shares'], types=[str, float, int]))


pprint(parse_csv('Work/Data/portfolio.csv',
                 select=['name', 'price', 'shares'], types=[str, float, int]))

pprint(parse_csv('Work/Data/portfolio.csv',
                 select=['name', 'price', 'shares']))
