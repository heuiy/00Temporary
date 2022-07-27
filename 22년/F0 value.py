import numpy as np
import pandas as pd

hd = pd.read_csv("https://raw.githubusercontent.com/heuiy/data/main/21_22Y/Toy/21_23Y/220721_PQP22167/HD.csv", skiprows=6, sep='\t')

hd_g = hd.iloc[:, 2:]

for col in hd_g.columns:
    print(col)

len(hd_g["1"])

range(len(hd_g["1"]))

hd_g["1"][300]

z = 10.0
b = 121.1
t = 1/6

for i in hd_g["1"]:
    sum = 0
    sum = (10**(i-b)/z) * t + sum
print (sum)

sum = 0

for i in range(len(hd_g["1"])):
    for j in hd_g["1"][i]:
        sum = sum + (10**(j-b)/z) * t
        print(sum)


