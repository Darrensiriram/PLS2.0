import json

import controllers.JsonHelper as JsonHelper
import controllers.PublicLibraryHelper as PublicLibraryHelper
import controllers.PageHelper as PageHelper
import controllers.LoanItemHelper as LoanItemHelper

import models.User as UserModel


class PersonHelper:

    @staticmethod
    def user_exist(file, user_id):
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            for book in data['results']:
                if book['userId'] == user_id:
                    return True
        return False

    @staticmethod
    def username_exist(file, username):
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            for book in data['results']:
                if book['userNameSet'] == username:
                    return True
        return False

    @staticmethod
    def register_user(user):
        file = 'data/user.json'

        if not PersonHelper.user_exist(file, user.userId) and not PersonHelper.username_exist(file, user.userNameSet):
            with open(file, 'r') as json_file:
                data = json.load(json_file)

                temp = data['results']

                new_data = {
                    'userNameSet': user.userNameSet,
                    'userPassword': user.userPassword,
                    'userId': user.userId,
                    'userGender': user.userGender,
                    'userFirstname': user.userFirstname,
                    'userSurname': user.userSurname,
                    'userZipCode': user.userZipCode,
                    'userCity': user.userCity,
                    'userEmailAddress': user.userEmailAddress,
                    'userTelephoneNumber': user.userTelephoneNumber,
                    'userAge': user.userAge,
                    'userAddress': user.userAddress,
                    'userCustomer': user.userCustomer,
                }
                temp.append(new_data)

            JsonHelper.JsonHelper.write_json(data, file)
            return True
        else:
            return False

    @staticmethod
    def validate_user(username, password):
        with open('data/user.json') as json_file:
            data = json.load(json_file)
            for line in data['results']:
                if line['userNameSet'] == username and line['userPassword'] == password:
                    return line
        return False

    @staticmethod
    def login(cache, username="", password=""):
        print("---------------------------------------------------------------------------")
        print("Login")
        print("---------------------------------------------------------------------------")
        username = username if username != "" else str(input("Username: "))
        password = password if password != "" else str(input("Password: "))
        result = PersonHelper.validate_user(username, password)
        if not result:
            PublicLibraryHelper.PublicLibraryHelper.error("Username and password combination not found.")
        else:
            cache['user'] = result

    @staticmethod
    def logout(cache):
        cache.pop('user')

    @staticmethod
    def register(cache, customer=True):
        PageHelper.PageHelper.clear()
        print("---------------------------------------------------------------------------")
        if customer:
            print("Register customer")
        else:
            print("Register librarian")

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
        user = UserModel.User(name_set, password, gender, firstname, surname, zip_code, city, email_address,
                              tele_phone_number, age, address, customer)

        PageHelper.PageHelper.clear()
        if PersonHelper.register_user(user):
            PersonHelper.login(cache, name_set, password)
        else:
            print("---------------------------------------------------------------------------")
            print("User/Username already exist")
            print("---------------------------------------------------------------------------")
            PersonHelper.register(cache)

    @staticmethod
    def search_user():
        PageHelper.PageHelper.clear()
        print("---------------------------------------------------------------------------")
        value = str(input("Enter the username of the user: "))

        filename = 'data/user.json'
        with open(filename, 'r') as source_file:
            data = json.load(source_file)
            for line in data['results']:
                if line['userNameSet'] in value:
                    PageHelper.PageHelper.clear()
                    print("---------------------------------------------------------------------------")
                    print(f"Username: {line['userNameSet']}")
                    print(f"Firstname: {line['userFirstname']}")
                    print(f"Surname: {line['userSurname']}")
                    if PublicLibraryHelper.PublicLibraryHelper.yes_or_no("Select this user?"):
                        return line['userId']
        PublicLibraryHelper.PublicLibraryHelper.error("User not found")
        PersonHelper.search_user()



