from collections import Counter

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)

]

total_shares = Counter()

for name, shares, price in portfolio:
    total_shares[name] += shares
