import csv
import json


def get_data():
    result = {}
    with open('./whitelist.csv') as f:
        rows = csv.DictReader(f)
        for row in rows:
            result[row['address']] = str(int(row['amount']) * (10 ** 18))
    return result


if __name__ == '__main__':
    with open('./whitelist.json', 'w') as f:
        json.dump(get_data(), f, ensure_ascii=False, indent=4)
    pass
