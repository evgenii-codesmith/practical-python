import IPython
from collections import defaultdict

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)

]

holdings = defaultdict(list)

for name, shares, price in portfolio:
    holdings[name].append((shares, price))


IPython.embed()
