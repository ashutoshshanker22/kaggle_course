#!/usr/local/bin/python3

import pandas as pd

print("==============")
print("Data Frame as Integer")
df1 = pd.DataFrame({'Yes': [50, 21],
		    'No': [131, 2]})
print(df1)

print("==============")
print("Data Frame as String")
df2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
		    'Sue': ['Pretty good.', 'Bland.']})
print(df2)
print("==============")

print("==============")
print("Row Labels: Index")
df3 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
		    'Sue': ['Pretty good.', 'Bland.']},
		   index=['Product A', 'Product B'])
print(df3)
print("==============")
