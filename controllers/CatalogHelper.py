
import controllers.BookHelper as BookHelper
import controllers.LoanItemHelper as LoanItemHelper
import controllers.PublicLibraryHelper as PublicLibraryHelper
import controllers.PageHelper as PageHelper


class CatalogHelper:

    @staticmethod
    def get_view_books():
        PageHelper.PageHelper.clear()
        data = BookHelper.BookHelper.get_all_book_item()

        print("---------------------------------------------------------------------------")
        print(f"List of books (Amount: {len(data['newBook'])})")

        for line in data['newBook']:
            print("---------------------------------------------------------------------------")
            print(f"Title: {line['bookTitle']}")
            print(f"Author: {line['bookAuthor']}")
            print(f"Year: {line['bookYear']}")
            print(f"Rented: {LoanItemHelper.LoanItemHelper.get_status_loan_book_item(line['bookId'])}")
            PublicLibraryHelper.PublicLibraryHelper.press_to_continue()

    @staticmethod
    def get_search_book():
        item = input("Please enter a title of a book: ")
        BookHelper.BookHelper.search_book(item, True)
