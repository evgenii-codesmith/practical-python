import csv


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


def calculate_initial_tcost(portfolio):
    total_cost = 0

    for line in portfolio:
        total_cost += line['price'] * line['shares']

    return total_cost


def calculate_current_tcost(portfolio, prices):
    total_cost = 0
    for line in portfolio:
        total_cost += prices.get(line['name'], 0) * line['shares']
    return total_cost


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

initial_tcost = calculate_initial_tcost(portfolio)
current_tcost = calculate_current_tcost(portfolio, prices)

if current_tcost > initial_tcost:
    print('Gain: ', current_tcost - initial_tcost)
else:
    print('Loss: ', initial_tcost - current_tcost)
