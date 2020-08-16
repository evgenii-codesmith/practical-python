import csv
import sys


def portfolio_cost(filename):
    """
    Calculates cost of portfolio

    filename: file name string
    Returns: total as float
    """
    total = 0

    f = open(filename)

    rows = csv.reader(f)
    next(rows)

    for rowno, row in enumerate(rows):
        try:
            total += float(row[1]) * float(row[2])
        except ValueError:
            print(f'Row {rowno}: {row}')

    f.close()

    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/missing.csv'

print('Total cost: ', portfolio_cost(filename))
