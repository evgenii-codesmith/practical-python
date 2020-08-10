import csv
import sys


def portfolio_cost(filename):
    total = 0

    f = open(filename)

    rows = csv.reader(f)

    next(rows)

    for row in rows:
        try:
            total += float(row[1]) * float(row[2])
        except ValueError as e:
            print(e)

    f.close()

    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

print('Total cost: ', portfolio_cost(filename))
