import json
from os import linesep
import controllers.JsonHelper as JsonHelper
import controllers.LoanHelper as LoanHelper
import controllers.SystemHelper as SystemHelper
import controllers.PageHelper as PageHelper

import models.Book as BookModel


class BookHelper:


    @staticmethod
    def add_book_item():
        PageHelper.PageHelper.clear()
        print("---------------------------------------------------------------------------")
        print("Add here your book")
        book_title = str(input("Title: "))
        book_country = str(input("Country: "))
        book_language = str(input("Language: "))
        book_link = str(input("Link: "))
        book_pages = str(input("Pages: "))
        book_year = str(input("Year: "))
        book_image_link = str(input("Image link: "))
        book_author = str(input("Book author: "))
        new_book = BookModel.Book(book_title, book_country, book_language, book_link, book_pages, book_year,
                                  book_image_link, book_author)

        result = False
        file = 'data/book.json'
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            for book in data['newBook']:
                if book['bookId'] == new_book.bookId:
                    result = True
        if not result:
            with open('data/book.json') as json_file:
                data = json.load(json_file)
                temp = data['newBook']

                new = {
                    'bookAuthor': new_book.bookAuthor,
                    'bookTitle': new_book.bookTitle,
                    'bookId': new_book.bookId,
                    'bookCountry': new_book.bookCountry,
                    'bookLanguage': new_book.bookLanguage,
                    'bookLink': new_book.bookLink,
                    'bookPages': new_book.bookPages,
                    'bookYear': new_book.bookYear,
                    'bookImageLink': new_book.bookImageLink,
                }
                temp.append(new)
            JsonHelper.JsonHelper.write_json(data, file)
            print('Book ' + new_book.bookTitle + ' Has been added')
        else:
            print('This book is already initialized')
        SystemHelper.SystemHelper.press_to_continue()

    @staticmethod
    def delete_book_item(id):
        count = 0
        with open('data/book.json', 'r') as source_file:
            data = json.load(source_file)
            for line in data['newBook']:
                if line['bookId'] == id:
                    del data['newBook'][count]
                    JsonHelper.JsonHelper.write_json(data, 'data/book.json')
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
    def search_book(value, search=False):
        filename = 'data/book.json'
        temp = []
        with open(filename, 'r') as source_file:
            data = json.load(source_file)
            for line in data['newBook']:
                if line['bookTitle'] in value or line['bookAuthor'] in value or line['bookYear'] in value:
                    print("---------------------------------------------------------------------------")
                    print("I found ur book: ")
                    print("---------------------------------------------------------------------------")
                    print(f"Title: {line['bookTitle']}")
                    print(f"Author: {line['bookAuthor']}")
                    print(f"Year: {line['bookYear']}")
                    temp.append(line)
        if len(temp)==0:
            print("i am sorry, it seems we cannont find ur book ")
        else:
            if not search:
                return temp

        SystemHelper.SystemHelper.press_to_continue()


    @staticmethod
    def get_view_books():
        PageHelper.PageHelper.clear()
        data = BookHelper.get_all_book_item()

        print("---------------------------------------------------------------------------")
        print(f"List of books (Amount: {len(data['newBook'])})")

        for line in data['newBook']:
            print("---------------------------------------------------------------------------")
            print(f"Title: {line['bookTitle']}")
            print(f"Author: {line['bookAuthor']}")
            print(f"Year: {line['bookYear']}")
            print(f"Rented: {LoanHelper.LoanHelper.get_status_loan_book_item(line['bookId'])}")
            SystemHelper.SystemHelper.press_to_continue()

    @staticmethod
    def get_loan_id():
        with open('data/loanList.json', 'r') as loanFile:
            return json.load(loanFile)

    @staticmethod
    def show_loan_books():
        data = BookHelper.get_loan_id()
        bookinfo = BookHelper.get_all_book_item()
        print("---------------------------------------------------------------------------")
        print(f"List of books that are currently loaned (Amount: {len(data['results'])})")
        for line in data['results']:
            print("---------------------------------------------------------------------------")
            print(f"BookId: {line['bookId']}")
            for x in bookinfo['newBook']:
                if line['bookId'] == x['bookId']:
                    print(f"BookId: {x['bookTitle']}")
        SystemHelper.SystemHelper.press_to_continue()        
        
