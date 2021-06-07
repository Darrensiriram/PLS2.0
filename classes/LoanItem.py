import json
class LoanItem:
    def checkBoekAvailable(self, bookTitle):
        with open('data/book.json', 'r') as json_file:
            data = json.load(json_file)
            temp = data['newBook']
            value = (list(filter(
                lambda x: x["bookId"] == bookTitle,
                temp)))
            if value != []:
                return bookTitle
            else:
                bookTitle = int(input("We didnt found any results try again: "))
                self.checkBoekAvailable(bookTitle)


    def checkUserAvaiable(self, userId):
        with open('data/user.json', 'r') as json_file:
            data = json.load(json_file)
            temp = data['results']
            value = (list(filter(
                lambda x: x["userId"] == userId,
                temp)))

            if value != []:
                return userId
            else:
                input("We didnt found any results try again")
                userId = str(input("user id: "))
                self.checkUserAvaiable(userId)



    def loan(self,userId,bookTitle):
        def write_json(data, filename='user.json'):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

        with open('data/loanList.json') as json_file:
            data = json.load(json_file)

            temp = data['results']

            newData = {
                "userId":   userId,
                "bookId":   bookTitle,
            }
            temp.append(newData)

        write_json(data)