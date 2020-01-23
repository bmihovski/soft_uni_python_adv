import json

with open("test.json") as json_cont:
    test_vals = json.load(json_cont)
print(test_vals)
