# Data Processor

import csv
import json

def read_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    print(1)
    return data

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    csv_data = read_csv("sample_data.csv")
    print("CSV Data:", csv_data)
    json_data = read_json("config.json")
    print("JSON Data:", json_data)
