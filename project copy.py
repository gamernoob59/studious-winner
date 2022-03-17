import csv

rows = []

with open("main.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
data_rows = rows[1:]

star=data_rows[0]

mass=star[8]*1.989e+30
radius=star[9]*6.957e+8

gravity=6.67430e-11*(mass/(radius*radius))

print(gravity)