import csv
from pprint import pprint
import fileparse2


def read_prices(filename):
    """
    filename: string
    returns: dict of prices {'name': price}
    """
    prices = fileparse2.parse_csv(
        filename, has_headers=False, types=[str, float])
    return dict(prices)


def read_portfolio(filename):
    # """
    # filename: filename string
    # returns portfolio: list of dicts [{'name':name, 'date':date,'time':time, \
    #     'shares':shares,'price':price}]
    # """

    portfolio = fileparse2.parse_csv(filename)
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


stocks = read_portfolio('Work/Data/portfoliodate.csv')
prices = read_prices('Work/Data/prices.csv')

# Print a table with shares, prices and prices changes
headers = ('Name', 'Shares', 'Price', 'Change')

print(
    f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print((10 * '-' + ' ') * len(headers))

for name, shares, price, change in make_report(stocks, prices):
    print(f'{name:>10s} {shares:^10d} {price:>10.2f} {change:>10.2f}')
