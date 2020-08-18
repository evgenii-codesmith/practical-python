import csv
from pprint import pprint


def read_portfolio(filename):
    """
    filename: filepath string
    returns portfolio: list of dicts [{'price':price, 'name':name,\
         'shares':shares}]
    """

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        selected_headers = ['price', 'name', 'shares']

        indices = [headers.index(colname) for colname in selected_headers]

        return [{colname: row[index] for colname, index in
                 zip(selected_headers, indices)} for row in rows]


pprint(read_portfolio('Work/Data/portfoliodate.csv'))
