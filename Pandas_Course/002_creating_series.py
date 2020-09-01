#!/usr/local/bin/python3

import pandas as pd

print("==============")
print("Series")
s1 = pd.Series([1, 2, 3, 4, 5])
print(s1)
print("==============")

print("Series column and name")
s2 = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(s2)
print("==============")
