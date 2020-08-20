# fileparse.py
#
# Exercise 3.3
import csv
from pprint import pprint


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    """
    Parse a CSV file into a list of records
    """

    with open(filename) as f:
        data = csv.reader(f, delimiter=delimiter)
        if has_headers:
            headers = next(data)
        else:
            headers = []

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
                if has_headers:
                    record = dict(zip(headers, line))
                else:
                    if types:
                        record = tuple([f(val) for f, val in zip(types, line)])
                    else:
                        record = tuple(line)

            records.append(record)

    return records


pprint(parse_csv('Work/Data/prices.csv',
                 types=[str, float], has_headers=False))

pprint(parse_csv('Work/Data/prices.csv', has_headers=False))

pprint(parse_csv('Work/Data/portfolio.csv',
                 select=['name', 'price', 'shares'], types=[str, float, int]))


pprint(parse_csv('Work/Data/portfolio.csv',
                 select=['name', 'price', 'shares'], types=[str, float, int]))

pprint(parse_csv('Work/Data/portfolio.csv',
                 select=['name', 'price', 'shares']))

pprint(parse_csv('Work/Data/portfolio.dat',
                 types=[str, int, float], delimiter=' '))
