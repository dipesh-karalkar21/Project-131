import pandas as pd
import csv

df = pd.read_csv("new.csv")

mass = df["Mass"].to_list()
radius = df["Radius"].to_list()

for i , d in enumerate(radius):
    if str(d) == '?':
        print(i)
        print("================")
        df.drop(index=i,inplace=True)

for i , d in enumerate(mass):
    if str(d) == '?':
        print(i)
        df.drop(index=i,inplace=True)

print()

df.to_csv("new2.csv")

