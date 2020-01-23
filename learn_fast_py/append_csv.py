import csv

with open("test.csv", "a", newline="") as f:
    handler = csv.writer(f, delimiter=",")
    handler.writerow(["ffs", "fsw2", "4343"])

