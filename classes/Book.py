import json
class Book:
    def __init__(self,bookTitle,bookCountry,bookLangue,bookLink,bookPages,bookYear,bookImageLink,bookAuthor):
        self.bookTitle = bookTitle
        self.bookCountry = bookCountry
        self.bookLanguage = bookLangue
        self.bookLink = bookLink
        self.bookPages = bookPages
        self.bookYear = bookYear
        self.bookImageLink = bookImageLink
        self.bookId = hash(bookTitle +bookCountry+bookLangue+bookLink+bookPages+bookYear+bookImageLink+bookAuthor)
        self.bookAuthor = bookAuthor
        

    def addNewBook(self):
        def write_json(data, filename='data/book.json'):
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)

        result = False
        with open('data/book.json', 'r') as json_file:
            data = json.load(json_file)
            for book in data['newBook']:
                if book['bookId'] == self.bookId:
                    result = True
        if not result:
            with open('data/book.json') as json_file:
                data = json.load(json_file)
                temp = data['newBook']

                newBook = {
                    'bookAuthor': self.bookAuthor,
                    'bookTitle': self.bookTitle,
                    'bookId': self.bookId,
                    'bookCountry': self.bookCountry,
                    'bookLanguage': self.bookLanguage,
                    'bookLink': self.bookLink,
                    'bookPages': self.bookPages,
                    'bookYear': self.bookYear,
                    'bookImageLink': self.bookImageLink,
                }
                temp.append(newBook)
            write_json(data)
        else:
            return False


    def deleteBook(self):
        with open('data/booksset1.json', '+') as delete_jsonFile:
            for oldBook in delete_jsonFile.readlines():
                data = json.load(delete_jsonFile)
                if data['bookTitle'] == self.bookTitle:
                    del oldBook['bookTitle']
                    del oldBook['bookYear']
                    del oldBook['bookPages']
                    del oldBook['bookLink']
                    del oldBook['bookLanguage']
                    del oldBook['bookImagelink']
                    del oldBook['bookCountry']
                    del oldBook['bookAuthor']
        return "Perfectly deleted the Book! "

    def displayBookDetails(self):
        with open('data/booksset1.json', 'r') as json_file:
                data = json.load(json_file)
                print(json.dumps(data, indent=4, sort_keys= True))




