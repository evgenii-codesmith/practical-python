import csv
from io import IOBase
# from pprint import pprint
from pathlib import Path
import gzip
import sys
import io


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    """
    Parse a CSV file/list into a list of records
    """

    if isinstance(filename, (list, str, io.IOBase)) is False:
        sys.exit('Wrong data or file does not exist')

    if isinstance(filename, (list, io.IOBase)):
        f = filename
    elif Path(filename).suffix == '.gz':
        f = gzip.open(filename, 'rt')
    elif Path(filename).suffix == '.csv':
        f = open(filename)
    else:
        sys.exit(f'Unable to process file {filename}')

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
    try:
        f.close()
    except AttributeError:
        pass
    return records


# pprint(parse_csv('Work/Data/prices.csv',
#                  types=[str, float], has_headers=False))

# pprint(parse_csv('Work/Data/prices.csv', has_headers=False))

# pprint(parse_csv('Work/Data/portfolio.csv',
#                  select=['name', 'price', 'shares'], types=[str, float, int]))


# pprint(parse_csv('Work/Data/portfolio.csv',
#                  select=['name', 'price', 'shares'], types=[str, float, int]))

# pprint(parse_csv('Work/Data/portfolio.csv',
#                  select=['name', 'price', 'shares']))

# pprint(parse_csv('Work/Data/portfolio.dat',
#                  types=[str, int, float], delimiter=' '))
