import csv
import json
from pathlib import Path


def flatten_data(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def main():
    # your code here
    p = Path('./data/')
    
    json_files = p.glob('**/*.json')
    
    for json_path in json_files:
        with open(json_path,'r') as file:
            json_dict = json.load(file)
        flatten_dict = flatten_data(json_dict)
        fields = list(flatten_dict.keys())
        new_file_path = json_path.with_suffix('.csv')
        with open(new_file_path, 'w+') as new_f:
            writer = csv.DictWriter(new_f, fields)
            writer.writeheader()
            writer.writerow(flatten_dict)


if __name__ == '__main__':
    main()
