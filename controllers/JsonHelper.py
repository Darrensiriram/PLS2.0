import json


class JsonHelper:

    @staticmethod
    def write_json(data, filename):
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)