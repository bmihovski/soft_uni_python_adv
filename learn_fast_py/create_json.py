import json

with open("test.json", "w") as file:
    contents = ["fsfsd", 3, "fsww"]
    json.dump(contents, file)

