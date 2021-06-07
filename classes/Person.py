
import json

class Person():
    def __init__(self, id):
        self.PersonId = id

    def returnBook(self, bookId):
        json_lines = []
        found = False
        with open("../data/loanList.json", 'r') as open_file:
            for line in open_file.readlines():
                j = json.loads(line)
                if j['userId'] == self.PersonId and j['bookId'] == bookId:
                    found = True
                else:
                    json_lines.append(line)

        if (found == True):
            return "Correctly returnd"
        else:
            with open("../data/loanList.json", 'a') as open_file:
                open_file.writelines('\n'.join(json_lines))
            return "Cant find book for user"


