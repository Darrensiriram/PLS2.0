import os

from controllers.UserHelper import UserHelper
from controllers.BookHelper import BookHelper
from controllers.SystemHelper import SystemHelper
from controllers.LoanHelper import LoanHelper

cache = dict()


class PageHelper:

    @staticmethod
    def clear():
        if os.name in ('nt', 'dos'):
            cl = lambda: os.system('cls')
        else:
            cl = lambda: os.system('clear')

        cl()

    @staticmethod
    def menu(dir_path):
        logged_in = 'user' in cache.keys()
        is_customer = logged_in and cache['user']['userCustomer']
        browse_catalog = 'browse_catalog' in cache.keys()
        data_management = 'data_management' in cache.keys()

        PageHelper.clear()
        if browse_catalog:
            print("---------------------------------------------------------------------------")
            print("                   Catalog of the Public library system                    ")
            print("---------------------------------------------------------------------------")
            print("Enter 0. Show books")
            print("Enter 1. Search book")
            print("Enter 2. Leave catalog")

        elif logged_in and is_customer:
            print("---------------------------------------------------------------------------")
            print("            Logged in as customer to the Public library system             ")
            print("---------------------------------------------------------------------------")
            print("Enter 0. Browse catalog")
            print("Enter 1. Loan a book")
            print("Enter 2. Return a book")
            print("Enter 3. To logout")

        elif logged_in and not is_customer and data_management:
            print("---------------------------------------------------------------------------")
            print("                Data management of the Public library system               ")
            print("---------------------------------------------------------------------------")
            print("Enter 0. Backup system")
            print("Enter 1. Restore backup")
            print("Enter 2. Fill system")
            print("Enter 3. Empty system")
            print("Enter 4. Leave data management")

        elif logged_in and not is_customer:
            print("---------------------------------------------------------------------------")
            print("            Logged in as librarian to the Public library system            ")
            print("---------------------------------------------------------------------------")
            print("Enter 0. Browse catalog")
            print("Enter 1. Add Book")
            print("Enter 2. Add customer")
            print("Enter 3. Add librarian")
            print("Enter 4. Loan a book to a customer")
            print("Enter 5. Return a book from a customer")
            print("Enter 6. See the loans of books")
            print("Enter 7. Data Management")
            print("Enter 8. To logout")

        else:
            print("---------------------------------------------------------------------------")
            print("                       Welcome to the Public library system                ")
            print("---------------------------------------------------------------------------")
            print("Enter 0. Browse catalog")
            print("Enter 1. To login")
            print("Enter 2. To register")

        PageHelper.menu_controller(logged_in, is_customer, browse_catalog, data_management, dir_path)

    @staticmethod
    def menu_controller(logged_in, is_customer, browse_catalog, data_management, dir_path):
        try:
            x = int(input("Select a choice from 1...: "))
            PageHelper.clear()

            if browse_catalog:
                if x == 0:
                    BookHelper.get_view_books()
                elif x == 1:
                    item = input("Please enter a title of a book: ")
                    BookHelper.search_book(item, True)
                elif x == 2:
                    cache.pop('browse_catalog')

            elif logged_in and is_customer:
                if x == 0:
                    cache['browse_catalog'] = True
                elif x == 1:
                    LoanHelper.loan_book(cache['user']['userId'])
                elif x == 2:
                    LoanHelper.return_book(cache['user']['userId'])
                elif x == 3:
                    UserHelper.logout(cache)
            elif logged_in and not is_customer and data_management:
                if x == 0:
                    SystemHelper.back_up(dir_path)
                elif x == 1:
                    SystemHelper.restore_back_up(dir_path)
                elif x == 2:
                    SystemHelper.fill_system(dir_path)
                elif x == 3:
                    SystemHelper.empty_system(dir_path)
                elif x == 4:
                    cache.pop('data_management')
            elif logged_in and not is_customer:
                if x == 0:
                    cache['browse_catalog'] = True
                elif x == 1:
                    BookHelper.add_book_item()
                elif x == 2:
                    UserHelper.register(cache)
                elif x == 3:
                    UserHelper.register(cache, False)
                elif x == 4:
                    UserHelper.loan_book_librarian()
                elif x == 5:
                    UserHelper.return_book_librarian()
                elif x == 6:
                    BookHelper.show_loan_books()
                elif x == 7:
                    cache['data_management'] = True
                elif x == 8:
                    UserHelper.logout(cache)
            else:
                if x == 0:
                    cache['browse_catalog'] = True
                elif x == 1:
                    UserHelper.login(cache)
                elif x == 2:
                    UserHelper.register(cache)
        except ValueError as e:
            SystemHelper.error("Please input as suggested.")

