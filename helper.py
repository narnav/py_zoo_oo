import json

def save(json_lst,my_data_file):
    with open(my_data_file, 'w') as f:
        json.dump(json_lst, f)

def load(my_data_file):
    with open(my_data_file) as f:
        return json.load(f)