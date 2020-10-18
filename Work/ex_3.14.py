from report import read_portfolio


def print_total_cost(filename):
    total = 0
    portfolio = read_portfolio(filename)
    for item in portfolio:
        total += item[1] * item[2]

    return total


print('Total cost:', print_total_cost('Work/Data/portfolio.csv'))
