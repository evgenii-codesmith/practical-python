import csv


def portfolio_cost(filename):
    total = 0
    f = open(filename)
    rows = csv.reader(f)

    next(rows)

    for row in rows:
        total += float(row[1]) * float(row[2])

    f.close()

    return total


print(portfolio_cost('./Data/portfolio.csv'))
