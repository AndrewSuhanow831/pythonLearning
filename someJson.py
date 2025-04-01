import json
from pprint import pprint

def read_json(): 
    with open("data.json", encoding="UTF-8") as file_in:
        records = json.load(file_in)
    pprint(records)

def edit_with_save_json():
    with open("data.json", encoding="UTF-8") as file_in:
        records = json.load(file_in)
    records[1]["group_number"] = 2
    with open("data.json", "w", encoding="UTF-8") as file_out:
        json.dump(records, file_out, ensure_ascii=False, indent=2)

def learn_json():
    records = {1 : "First", 2 : "Second", 3 : "Third"}
    
    with open("output.json", "w", encoding="UTF-8") as file_out:
        json.dump(records, file_out, indent=None)

learn_json()
