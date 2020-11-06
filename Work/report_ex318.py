import csv
import fileparse_ex317 as fileparse


def read_prices(filename):
    """
    returns prices: dict
    """

    prices = fileparse.parse_csv(
        filename, has_headers=False, types=[str, float])
    return dict(prices)


def read_portfolio(filename):
    """
    filename: filename string
    returns portfolio: list of dicts [{'name':name, 'shares':shares,
    'price':price}]
    """

    portfolio = fileparse.parse_csv(filename,
                                    select=['name', 'price', 'shares'],
                                    types=[str, float, int])
    return portfolio


def make_report(stocks, prices):
    """
    stocks: List [{},{}] of stocks data
    prices: Dict {} of prices
    returns list of tuples [(Name, Shares, Price, Change)]
    """

    output = []

    for stock in stocks:
        current_stock_price = prices.get(stock['name'], 0)
        price_change = current_stock_price - float(stock['price'])
        price_change = round(price_change, 2)
        output.append((stock['name'], int(stock['shares']),
                       current_stock_price, price_change))

    return output


def print_table(data):

    # Print a table with shares, prices and prices changes
    headers = ('Name', 'Shares', 'Price', 'Change')

    print(
        f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print((10 * '-' + ' ') * len(headers))

    for name, shares, price, change in data:
        print(f'{name:>10s} {shares:^10d} {price:>10.2f} {change:>10.2f}')


def main(argv):
    prices = read_prices(argv[2])
    portfolio = read_portfolio(argv[1])
    data = make_report(portfolio, prices)

    print_table(data)


if __name__ == '__main__':
    import sys
    main(sys.argv)
