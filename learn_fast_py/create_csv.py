import csv

with open("test.csv", "w", newline="") as f:
    file_handler = csv.writer(f, delimiter=",")
    file_handler.writerow(["fs", "ww", "33"])
    file_handler.writerow(["3", "ww", "ssf"])
    file_handler.writerow(["43", "fss", "343"])

