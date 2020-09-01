#!/usr/local/bin/python3

import pandas as pd
pd.set_option('max_rows', 5)
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

print("\n======================\nSet Index\n======================\n")
print(reviews.set_index('title'))
