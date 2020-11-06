import csv
import fileparse_ex317 as fileparse
from stock_ex4_1 import Stock

# class Stock:
#     def __init__(self, name, price, shares):
#         self.name = name
#         self.shares = shares
#         self.price = price

#     def sell(self, shares):
#         self.shares -= shares

#     def cost(self):
#         return self.price * self.shares


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
    returns portfolio: list of objects
    """

    portfolio = fileparse.parse_csv(filename,
                                    select=['name', 'price', 'shares'],
                                    types=[str, float, int])
    portfolio = [Stock(item['name'], item['price'], item['shares'])
                 for item in portfolio]
    return portfolio


def portfolio_report(portfolio, prices):
    """
    stocks: List [object1,object2] of stocks data
    prices: Dict {} of prices
    returns list of tuples [(Name, Shares, Price, Change)]
    """

    output = []
    prices = read_prices(prices)
    portfolio = read_portfolio(portfolio)

    for stock in portfolio:
        current_stock_price = prices.get(stock.name, 0)
        price_change = current_stock_price - stock.price
        price_change = round(price_change, 2)
        output.append((stock.name, int(stock.shares),
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
    prices = argv[2]
    portfolio = argv[1]
    data = portfolio_report(portfolio, prices)
    print_table(data)


if __name__ == '__main__':
    import sys
    main(sys.argv)

# Usage example:
# python report_ex4_4.py ./Data/portfolio.csv ./Data/prices.csv
# report = portfolio_report('Work/Data/portfolio.csv', 'Work/Data/prices.csv')
# print_table(report)
