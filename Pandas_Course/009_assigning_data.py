#!/usr/local/bin/python3

import pandas as pd
pd.set_option('max_rows', 5)
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

print("\n====================\nAssigning a constant value\n======================\n")
reviews['critic'] = 'everyone'
print(reviews['critic'])

print("\n====================\nAssigning iterable values\n======================\n")
reviews['index_backwards'] = range(len(reviews), 0, -1)
print(reviews['index_backwards'])
