#!/usr/local/bin/python3

import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)
pd.set_option("display.max_rows", 5)

print(reviews.head())

print("\nSelect the description column from reviews and assign the result to the variable desc.")
desc = reviews.description
print(desc)
print(type(desc))

print("\n\nSelect the first value from the description column of reviews, assigning it to variable first_description.")
first_description = reviews.description[0]
print(first_description)

print("\n\nSelect the first row of data (the first record) from reviews, assigning it to the variable first_row.")
first_row = reviews.iloc[0, :]
print(first_row)

print("\n\nSelect the first 10 values from the description column in reviews, assigning the result to variable first_descriptions.")
first_descriptions = reviews.loc[0:9, 'description']
print(first_descriptions)

print("\n\nSelect the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.")
sample_reviews = reviews.iloc[[1, 2, 3, 5, 8]]
print(sample_reviews)

print("\n\nCreate a variable df containing the country, province, region_1, and region_2 columns of the records with the index labels 0, 1, 10, and 100")
df = reviews.loc[[0, 1, 10, 100], ['country', 'province', 'region_1', 'region_2']]
print(df)

print("\n\nCreate a variable df containing the country and variety columns of the first 100 records.")
df = reviews.loc[0:99, ['country', 'variety']]
print(df)

print("\n\nCreate a DataFrame italian_wines containing reviews of wines made in Italy.")
italian_wines = reviews.loc[reviews.country == 'Italy']
print(italian_wines)

print("\n\nCreate a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.")
top_oceania_wines = reviews.loc[reviews.country.isin(['Australia', 'New Zealand']) & (reviews.points >= 95)]
print(top_oceania_wines)
