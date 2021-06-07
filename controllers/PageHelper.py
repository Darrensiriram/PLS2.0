import os
import models.User as UserModel
import controllers.UserHelper as UserHelper
import controllers.BookHelper as BookHelper
import controllers.SystemHelper as SystemHelper
import controllers.LoanHelper as LoanHelper

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
    def menu():
        logged_in = 'user' in cache.keys()
        is_customer = logged_in and cache['user']['userCustomer']
        browse_catalog = 'browse_catalog' in cache.keys()

        PageHelper.clear()
        if browse_catalog:
            print("---------------------------------------------------------------------------")
            print("                   Catalog of the Public library system                    ")
            print("---------------------------------------------------------------------------")
            print("Enter 0. Leave Catalog")

        elif logged_in and is_customer:
            print("---------------------------------------------------------------------------")
            print("            Logged in as customer to the Public library system             ")
            print("---------------------------------------------------------------------------")
            print("Enter 0. Browse catalog")
            print("Enter 1. Loan a book")
            print("Enter 2. Return a book")
            print("Enter 3. To logout")

        elif logged_in and not is_customer:
            print("---------------------------------------------------------------------------")
            print("            Logged in as librarian to the Public library system            ")
            print("---------------------------------------------------------------------------")
            print("Enter 0. Browse catalog")
            print("Enter 1. Add Book")
            print("Enter 2. Add User") # ToDO CUSTOMER OR librarian
            print("Enter 3. Loan a book to a customer")
            print("Enter 4. Return a book from a customer")
            print("Enter 5. See the loans of books")
            print("Enter 6. Data Management")
            print("Enter 7. To logout")

        else:
            print("---------------------------------------------------------------------------")
            print("                       Welcome to the Public library system                ")
            print("---------------------------------------------------------------------------")
            print("Enter 0. Browse catalog")
            print("Enter 1. To login")
            print("Enter 2. To register")

        PageHelper.menu_controller(logged_in, is_customer, browse_catalog)

    @staticmethod
    def menu_controller(logged_in, is_customer, browse_catalog):
        try:
            x = int(input("Select a choice from 1...: "))
            PageHelper.clear()

            if browse_catalog:
                if x == 0:
                    cache.pop('browse_catalog')

            elif logged_in and is_customer:
                if x == 0:
                    cache['browse_catalog'] = True
                elif x == 1:
                    PageHelper.loan_book()
                elif x == 2:
                    PageHelper.return_book()
                elif x == 3:
                    PageHelper.logout()
            elif logged_in and not is_customer:
                if x == 0:
                    cache['browse_catalog'] = True
                elif x == 1:
                    print("---------------------------------------------------------------------------")
                elif x == 2:
                    print("---------------------------------------------------------------------------")
                elif x == 3:
                    print("---------------------------------------------------------------------------")
                elif x == 4:
                    print("---------------------------------------------------------------------------")
                elif x == 5:
                    print("---------------------------------------------------------------------------")
                elif x == 6:
                    print("---------------------------------------------------------------------------")
                elif x == 7:
                    PageHelper.logout()
            else:
                if x == 0:
                    cache['browse_catalog'] = True
                elif x == 1:
                    PageHelper.login()
                elif x == 2:
                    PageHelper.register()
        except ValueError as e:
            SystemHelper.SystemHelper.error("Please input as suggested.")

    @staticmethod
    def login(username="", password=""):
        print("---------------------------------------------------------------------------")
        print("Login")
        print("---------------------------------------------------------------------------")
        username = username if username != "" else str(input("Username: "))
        password = password if password != "" else str(input("Password: "))
        result = UserHelper.UserHelper.validate_user(username, password)
        if not result:
            PageHelper.clear()
            print("---------------------------------------------------------------------------")
            print("Username and password combination not found.")
            print("---------------------------------------------------------------------------")
            PageHelper.login()
        else:
            cache['user'] = result

    @staticmethod
    def logout():
        cache.pop('user')

    @staticmethod
    def register():
        name_set = str(input("Username: "))
        password = str(input("Password: "))
        gender = str(input("Gender: "))
        firstname = str(input("Firstname: "))
        surname = str(input("Surname: "))
        zip_code = str(input("Zipcode: "))
        city = str(input("City: "))
        email_address = str(input("Email address: "))
        tele_phone_number = str(input("Phone number: "))
        age = str(input("age: "))
        address = str(input("Address: "))
        customer = str(input("Customer: "))  # checkbox TODO
        user = UserModel.User(name_set, password, gender, firstname, surname, zip_code, city, email_address,
                              tele_phone_number, age, address, True)

        PageHelper.clear()
        if UserHelper.UserHelper.register_user(user):
            PageHelper.login(name_set, password)
        else:
            print("---------------------------------------------------------------------------")
            print("User already exist")
            print("---------------------------------------------------------------------------")
            PageHelper.register()

    @staticmethod
    def loan_book():
        PageHelper.clear()
        print("---------------------------------------------------------------------------")
        search = str(input("Search for book, year or author: "))
        books = BookHelper.BookHelper.search_book(search)
        if books:
            LoanHelper.LoanHelper.get_search_results(books, cache['user']['userId'])
        else:
            SystemHelper.SystemHelper.error("Sorry we couldn't find your search, please try again!")
            PageHelper.loan_book()

    @staticmethod
    def return_book():
        print("---------------------------------------------------------------------------")
        print("Return book")
