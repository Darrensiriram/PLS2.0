import json
class PublicLibrary:
    def __init__(self):
        self.isBackUp = False

    def backUp(self):
        with open('../data/user.json') as json_file:
            data = json.load(json_file)

        with open('../backup/backupUser.json', 'a') as json_file:
            json.dump(data, json_file, indent=4)

        with open('../data/loanList.json') as json_file:
            data = json.load(json_file)

        with open('../backup/loanList.json', 'a') as json_file:
            json.dump(data, json_file, indent=4)

        with open('../data/import/booksset1.json') as json_file:
            data = json.load(json_file)

        with open('../backup/booksset1.json', 'a') as json_file:
            json.dump(data, json_file, indent=4)
        self.isBackUp = True

    def restoreBackUp(self):
        with open('../backup/user.json') as json_file:
            data = json.load(json_file)

        with open('../data/backupUser.json', 'a') as json_file:
            json.dump(data, json_file, indent=4)

        with open('../backup/loanList.json') as json_file:
            data = json.load(json_file)

        with open('../data/loanList.json', 'a') as json_file:
            json.dump(data, json_file, indent=4)

        with open('../backup/booksset1.json') as json_file:
            data = json.load(json_file)

        with open('../data/import/booksset1.json', 'a') as json_file:
            json.dump(data, json_file, indent=4)

    def searchBook(self, name):
        with open('../data/import/booksset1.json', 'r') as json_file:
            data = json.load(json_file)
            value = (list(filter(
                lambda x: x["title"] == name or ["country"] == name or ["language"] == name,
                data)))

            if value != []:
                return value
            else:
                name = str(input("We didnt found any results try again: "))
                self.searchBook(name)



