import json
import controllers.SystemHelper as SystemHelper
import controllers.JsonHelper as JsonHelper


class LoanHelper:
    @staticmethod
    def get_available_loan_book():
        print('TODO')

    @staticmethod
    def get_available_loan_book_item():
        print('TODO')

    @staticmethod
    def get_loan_book_():
        print('TODO')

    @staticmethod
    def get_loan_book_user():
        print('TODO')

    @staticmethod
    def set_loan_book_item(book_id, user_id):
        filename = 'data/loanList.json'
        with open(filename, 'r') as json_file:
            data = json.load(json_file)

            temp = data['results']

            new_data = {
                "userId": user_id,
                "bookId": book_id,
            }
            temp.append(new_data)
        JsonHelper.JsonHelper.write_json(temp, filename)

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
    def return_loan_book_item():
        print('TODO')


    @staticmethod
    def get_search_results(books, user_id, return_book=False):
        print("---------------------------------------------------------------------------")
        print(f"Amount of results {len(books)}")
        for book in books:
            print("---------------------------------------------------------------------------")
            print(f"Title: {book['bookTitle']}")
            print(f"Author: {book['bookAuthor']}")
            print(f"Year: {book['bookYear']}")

            if not return_book:
                if not LoanHelper.get_status_loan_book_item(book['bookId']):
                    if SystemHelper.SystemHelper.yes_or_no("Loan this book?"):
                        LoanHelper.set_loan_book_item(book['bookId'], user_id)
                else:
                    input("Book already lent")
            else:
                if SystemHelper.SystemHelper.yes_or_no("Return this book?"):
                    LoanHelper.set_loan_book_item(book['bookId'], user_id)
