import IPython
from collections import deque
import os

print(os.getcwd())

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)

]

history = deque(maxlen=10)
with open('./Data/portfolio.csv') as f:
    for line in f:
        history.append(line)


IPython.embed()
