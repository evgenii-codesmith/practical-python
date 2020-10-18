import csv


def portfolio_cost(filename):
    """
    Calculates cost of portfolio

    filename: file name string
    Returns: total as float
    """

    total = 0

    f = open(filename)

    rows = csv.reader(f)
    headers = next(rows)

    for rowno, row in enumerate(rows, start=1):
        try:
            record = dict(zip(headers, row))
            nshares = int(record['shares'])
            price = float(record['price'])
            total += nshares * price

        except ValueError:
            print(f'Row {rowno}: Row: {row}')

    f.close()
    return total


def main(argv):
    print('Total cost: ', portfolio_cost(argv[1]))


if __name__ == '__main__':
    import sys
    main(sys.argv)
