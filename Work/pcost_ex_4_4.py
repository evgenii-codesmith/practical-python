import csv
from report_ex4_4 import read_portfolio


def portfolio_cost(filename):
    """
    Calculates cost of portfolio

    filename: file name string
    Returns: total as float
    """

    total = 0

    portfolio = read_portfolio(filename)

    for rowno, stock in enumerate(portfolio, start=1):
        try:

            nshares = stock.shares
            price = stock.price
            total += nshares * price

        except ValueError:
            print(f'Row {rowno}: Row: {stock}')

    return total


def main(argv):
    print('Total cost: ', portfolio_cost(argv[1]))


if __name__ == '__main__':
    import sys
    main(sys.argv)
