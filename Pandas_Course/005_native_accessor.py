#!/usr/local/bin/python3

import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option('max_rows', 5)
print(reviews)

print("\n=====================\nNatvie Accessor 1\n======================\n")
print(reviews.country)

print("\n=====================\nNatvie Accessor 2\n======================\n")
print(reviews['country'])

print("\n=====================\nNatvie Accessor 3\n======================\n")
print(reviews['country'][0])
