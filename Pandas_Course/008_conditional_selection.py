#!/usr/local/bin/python3

import pandas as pd
pd.set_option('max_rows', 5)
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

print("\n====================\nChecking if wine is Italian or not\n======================\n")
print(reviews.country == 'Italy')

print("\n====================\nLocate only Italian wine data from wine reviews\n======================\n")
italian_wine_reviews = reviews.loc[reviews.country == 'Italy']
print(italian_wine_reviews)

print("\n====================\nLocate only Italian wine data from wine reviews with above avg points\n======================\n")
italian_wine_reviews_above_avg = reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
print(italian_wine_reviews_above_avg)

print("\n====================\nLocate Italian wine or wine with above avg points\n======================\n")
italian_wine_or_above_avg = reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
print(italian_wine_or_above_avg)

print("\n====================\nLocate wines only from Italy or France\n======================\n")
italian_or_french_wine = reviews.loc[reviews.country.isin(['Italy', 'France'])]
print(italian_or_french_wine)

print("\n====================\nLocate filter out wines lacking a price tag in the dataset\n======================\n")
wine_skip_lack_price_tag = reviews.loc[reviews.price.notnull()]
print(wine_skip_lack_price_tag)
