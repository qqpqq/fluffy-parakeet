import json


def json_parser(json_file_path: str):
    with open(json_file_path) as json_file:
        json_data = json.load(json_file)

    return json_data
