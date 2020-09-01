#!/usr/local/bin/python3

import pandas as pd

print("\n=================\nPrint shape of Dataframe\n================\n")
wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")
print(wine_reviews.shape)

print("\n=================\nPrint first 5 rows of csv in dataframe\n================\n")
wine_reviews_head = wine_reviews.head()
print(wine_reviews_head)

print("\n=================\nPrint first 5 rows of csv in dataframe and use built-in index column\n================\n")
wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
wine_reviews_head = wine_reviews.head()
print(wine_reviews_head)
