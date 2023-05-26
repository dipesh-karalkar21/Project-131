#Kindly Run Clean.py first 

import csv
import pandas as pd

df = pd.read_csv("new2.csv")


df['Radius'] = df['Radius'].apply(lambda x: x.replace(',', ''))
df['Mass'] = df['Mass'].apply(lambda x: str(x).replace(',', '').replace('<','').replace('<',''))

final_mass = []
final_rad = []

for i , d in enumerate(df["Mass"]):
    data = str(d).split("-")
    if len(data) == 2:
        avg =  (float(data[0])+float(data[1]))/2
        final_mass.append(avg)
    else:
        final_mass.append(data[0])

for i , d in enumerate(df["Radius"]):
    data = d.split("-")
    if len(data) == 2:
        avg =  (float(data[0])+float(data[1]))/2
        final_rad.append(avg)
    else:
        final_rad.append(data[0])

print(final_mass)
print(final_rad)

df["Mass"] = final_mass
df["Radius"] = final_rad

radius = df["Radius"].to_list()
mass = df["Mass"].to_list()
gravity = []

for i , d in enumerate(radius):
    radius[i] = float(radius[i])*6.957e+8
    print(i)
    mass[i] = float(mass[i])*1.989e+30

df["Mass"] = mass
df["Radius"] = radius

for i , d in enumerate(radius):
    g = (float(mass[i])/float(radius[i]))*6.67e-11
    gravity.append(g)

df["Gravity"] = gravity

df.to_csv("final.csv")
