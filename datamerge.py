import csv

dataset_1 = []
dataset_2 = []

with open('Sample_1.csv', 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row[1:])

with open("Sample2_Sorted.csv", "r", encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

headers = headers_2 + headers_1
planet_data = []
for index, data_row in enumerate(planet_data_2):
    planet_data.append(planet_data_2[index] + planet_data_1[index])

with open("Final.csv", "w", encoding='utf-8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)