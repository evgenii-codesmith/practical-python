import csv
from pprint import pprint


def parse_csv(filename, select=None, types=None,
              has_headers=True, delimiter=',',
              silence_errors=False):
    """
    Parse a CSV file into a list of records
    """

    if select and has_headers is False:
        raise RuntimeError('Select needs column headers')

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

        for linenum, line in enumerate(data):
            if not line:
                continue
            if indexes:
                line = [line[i] for i in indexes]
                if types:
                    line = [f(val) for f, val in zip(types, line)]
                record = dict(zip(select, line))
            else:
                if has_headers:
                    if types:
                        try:
                            line = [f(val) for f, val in zip(types, line)]
                        except ValueError as e:
                            if silence_errors:
                                pass
                            else:
                                print(
                                    f'Line: {linenum} Unable to convert {line}')
                                print(f'Line: {linenum} Reason {e}')
                    record = dict(zip(headers, line))
                else:
                    if types:
                        record = tuple([f(val) for f, val in zip(types, line)])
                    else:
                        record = tuple(line)

            records.append(record)

    return records


# pprint(parse_csv('Work/Data/prices.csv',
#                  types=[str, float], has_headers=False))

# pprint(parse_csv('Work/Data/prices.csv', has_headers=False))

pprint(parse_csv('Work/Data/missing.csv', types=[str, int, float]))
pprint(parse_csv('Work/Data/missing.csv',
                 types=[str, int, float], silence_errors=True))
# pprint(parse_csv('Work/Data/portfolio.csv',
#                  select=['name', 'price', 'shares'], types=[str, float, int]))

# pprint(parse_csv('Work/Data/portfolio.csv',
#                  select=['name', 'price', 'shares']))

# pprint(parse_csv('Work/Data/portfolio.dat',
#                  types=[str, int, float], delimiter=' '))
