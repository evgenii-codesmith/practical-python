import csv
from pprint import pprint


def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as file:
        data = csv.reader(file)
        for row in data:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(f)

        for row in rows:
            shares_dict = {}
            shares_dict['name'] = row[0]
            shares_dict['shares'] = int(row[1])
            shares_dict['price'] = float(row[2])
            portfolio.append(shares_dict)

    return portfolio


def make_report(stocks, prices):
    """
    :stocks List [] of stocks
    :prices Dict {} of prices
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


stocks = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# Print a table with shares, prices and prices changes
headers = ('Name', 'Shares', 'Price', 'Change')

print(
    f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print((10 * '-' + ' ') * len(headers))
for name, shares, price, change in make_report(stocks, prices):
    print(f'{name:>10s} {shares:^10d} {price:>10.2f} {change:>10.2f}')
