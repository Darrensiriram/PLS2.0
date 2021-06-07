import json
from controllers.JsonHelper import JsonHelper


class BookHelper:
    @staticmethod
    def add_book_item(nb):
        result = False
        file = 'data/book.json'
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            for book in data['newBook']:
                if book['bookId'] == nb.bookId:
                    result = True
        if not result:
            with open('data/book.json') as json_file:
                data = json.load(json_file)
                temp = data['newBook']

                newBook = {
                    'bookAuthor': nb.bookAuthor,
                    'bookTitle': nb.bookTitle,
                    'bookId': nb.bookId,
                    'bookCountry': nb.bookCountry,
                    'bookLanguage': nb.bookLanguage,
                    'bookLink': nb.bookLink,
                    'bookPages': nb.bookPages,
                    'bookYear': nb.bookYear,
                    'bookImageLink': nb.bookImageLink,
                }
                temp.append(newBook)
            JsonHelper.write_json(data, file)
        else:
            return False

    @staticmethod
    def delete_book_item(id):
        count = 0
        with open('data/book.json', 'r') as source_file:
            data = json.load(source_file)
            for line in data['newBook']:
                if line['bookId'] == id:
                    del data['newBook'][count]
                    JsonHelper.write_json(data, 'data/book.json')
                    return True
                else:
                   count = count + 1
            return False

    @staticmethod
    def get_book_item(id):
        with open('data/book.json', 'r') as source_file:
            data = json.load(source_file)
            for line in data['newBook']:
                if line['bookId'] == id:
                    return line

    @staticmethod
    def get_all_book_item():
        with open('data/book.json', 'r') as source_file:
            return json.load(source_file)

    @staticmethod
    def search_book(value):
        filename = 'data/book.json'
        temp = []
        with open(filename, 'r') as source_file:
            data = json.load(source_file)
            for line in data['newBook']:
                if line['bookTitle'] in value or line['bookAuthor'] in value or line['bookYear'] in value:
                    temp.append(line)
        return temp
