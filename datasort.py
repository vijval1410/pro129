import csv
import pandas as pd

data = pd.read_csv("brown.csv")

headers = []
for header in data.columns:
    headers.append(header)

del headers[0]
for x in headers:
    data = data[data[x].notna()]

temp_mass = []
for Mvalue in data['Mass']:
    Mvalue = float(Mvalue)
    Mvalue = Mvalue*0.000954588
    temp_mass.append(Mvalue)
data['Mass'] = temp_mass

temp_radius = []
for Rvalue in data['Radius']:
    Rvalue = float(Rvalue)
    Rvalue = Rvalue*0.102763
    temp_radius.append(Rvalue)
data['Radius'] = temp_radius

data = data.drop('Unnamed: 0', axis=1)
df = pd.DataFrame(data)

df.to_csv('brown2.csv', index=False)