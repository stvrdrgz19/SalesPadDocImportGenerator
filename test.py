import json

with open("configuration/settings.json", "r") as file:
    data = json.load(file)

next_doc_num = data["next_doc_num"]
print(f'Next Doc Num: {next_doc_num}')

next_doc_num += 1
data["next_doc_num"] = next_doc_num

with open("configuration/settings.json", "w") as file:
    json.dump(data, file, indent=4)

with open("configuration/settings.json", "r") as file:
    data = json.load(file)

new_doc_num = data["next_doc_num"]
print(f'New Doc Num: {new_doc_num}')

