#!/usr/local/bin/python3

import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print("\n=================\niloc example 1: get row with iloc\n==================\n")
print(reviews.iloc[0])

print("\n=================\niloc example 2: get column with iloc\n==================\n")
print(reviews.iloc[:, 0])

print("\n=================\niloc example 3: get column and first, second and third rows with iloc\n==================\n")
print(reviews.iloc[:3, 0])

print("\n=================\niloc example 4: get column and second and third rows with iloc\n==================\n")
print(reviews.iloc[1:3, 0])

print("\n=================\niloc example 5: get column and second, third and forth rows with iloc\n==================\n")
print(reviews.iloc[[1, 2, 3], 0])

print("\n=================\niloc example 6: get last 5 rows with iloc\n==================\n")
print(reviews.iloc[-5:])

print("\n=================\nloc example 1: first row and country column\n==================\n")
print(reviews.loc[0, 'country'])

print("\n=================\nloc example 2: all rows and taster_name, taster_twitter_handle and points column\n==================\n")
print(reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])
