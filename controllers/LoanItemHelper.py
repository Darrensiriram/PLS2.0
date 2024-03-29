import json
import controllers.PublicLibraryHelper as PublicLibraryHelper
import controllers.JsonHelper as JsonHelper
import controllers.BookHelper as BookHelper
import controllers.PageHelper as PageHelper


class LoanItemHelper:

    @staticmethod
    def get_loan_book_user(user_id):
        file = 'data/loanList.json'
        results = []
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            for loan in data['results']:
                if loan['userId'] == user_id:
                    results.append(BookHelper.BookHelper.get_book_item(loan['bookId']))
        return results

    @staticmethod
    def set_loan_book_item(book_id, user_id):
        filename = 'data/loanList.json'
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            new_data = {
                "userId": user_id,
                "bookId": book_id,
            }
            data['results'].append(new_data)
        JsonHelper.JsonHelper.write_json(data, filename)

    @staticmethod
    def get_status_loan_book_item(book_id):
        file = 'data/loanList.json'
        with open(file) as json_file:
            data = json.load(json_file)
            for book in data['results']:
                if book['bookId'] == book_id:
                    return True
        return False

    @staticmethod
    def return_loan_book_item(book_id, user_id):
        file = 'data/loanList.json'
        count = 0
        with open(file, 'r') as source_file:
            data = json.load(source_file)
            for line in data['results']:
                if line['userId'] == user_id and line['bookId'] == book_id:
                    del data['results'][count]
                    JsonHelper.JsonHelper.write_json(data, file)
                    return True
                else:
                    count = count + 1
        return False

    @staticmethod
    def get_search_results(books, user_id, return_book=False):
        print("---------------------------------------------------------------------------")
        print(f"Amount of results {len(books)}")
        PublicLibraryHelper.PublicLibraryHelper.press_to_continue()
        PageHelper.PageHelper.clear()
        for book in books:
            if not return_book:
                PageHelper.PageHelper.clear()
                print("---------------------------------------------------------------------------")
                print(f"Title: {book['bookTitle']}")
                print(f"Author: {book['bookAuthor']}")
                print(f"Year: {book['bookYear']}")

                if not LoanItemHelper.get_status_loan_book_item(book['bookId']):
                    if PublicLibraryHelper.PublicLibraryHelper.yes_or_no("Loan this book?"):
                        LoanItemHelper.set_loan_book_item(book['bookId'], user_id)
                        PublicLibraryHelper.PublicLibraryHelper.error("Book correctly lent.", False)
                else:
                    input("Book already on lent")
            else:
                if PublicLibraryHelper.PublicLibraryHelper.yes_or_no("Return this book?"):
                    if LoanItemHelper.return_loan_book_item(book['bookId'], user_id):
                        PublicLibraryHelper.PublicLibraryHelper.error("Book correctly returned.", False)

    @staticmethod
    def loan_book(user):
        PageHelper.PageHelper.clear()
        print("---------------------------------------------------------------------------")
        search = str(input("Search for book, year or author: "))
        books = BookHelper.BookHelper.search_book(search)
        if books:
            LoanItemHelper.get_search_results(books, user)
        else:
            PublicLibraryHelper.PublicLibraryHelper.error("Sorry we couldn't find your search, please try again!")
            LoanItemHelper.loan_book(user)

    @staticmethod
    def return_book(user):
        print("---------------------------------------------------------------------------")
        print("Return book")
        books = LoanItemHelper.get_loan_book_user(user)
        if books:
            LoanItemHelper.get_search_results(books, user, True)
        else:
            PublicLibraryHelper.PublicLibraryHelper.error("Sorry you have no returns.")
