#!/usr/local/bin/python3

import pandas as pd

pd.set_option('max_rows', 5)

print("\n============\nExercise 1\n============\n")
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})
print(fruits)

print("\n============\nExercise 2\n============\n")
fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])
print(fruit_sales)

print("\n============\nExercise 3\n============\n")
ingredients= pd.Series(['4 cups', '1 cup', '2 large', '1 can1'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')
print(ingredients)

print("\n============\nExercise 4\n============\n")
reviews = pd.read_csv("winemag-data_first150k.csv", index_col=0)
print(reviews.head())

print("\n============\nExercise 5\n============\n")
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
print("Save the dataframe to cows_and_goats.csv")
animals.to_csv('cows_and_goats.csv')
