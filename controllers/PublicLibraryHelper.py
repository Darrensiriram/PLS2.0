import controllers.PageHelper as PageHelper
import controllers.PersonHelper as PersonHelper
import controllers.BookHelper as BookHelper
import models.Book as Book
import models.User as UserModel
import json
import csv
import os


class PublicLibraryHelper:
    @staticmethod
    def yes_or_no(question):
        while "the answer is invalid":
            reply = str(input(question + ' (y/n): ')).lower().strip()
            if reply[:1] == 'y':
                return True
            elif reply[:1] == 'n':
                return False
            else:
                print("Only y/n allowed")


    @staticmethod
    def error(text, clear=True):
        if clear:
            PageHelper.PageHelper.clear()
        print("---------------------------------------------------------------------------")
        print(text)
        PublicLibraryHelper.press_to_continue()

    @staticmethod
    def back_up(dir_path):
        print("---------------------------------------------------------------------------")
        with open(dir_path+'/data/user.json') as json_file:
            data = json.load(json_file)

        with open(dir_path+'/data/backup/backupUser.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        with open(dir_path+'/data/loanList.json') as json_file:
            data = json.load(json_file)

        with open(dir_path+'/data/backup/loanList.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        with open(dir_path + '/data/book.json') as json_file:
            data = json.load(json_file)

        with open(dir_path + '/data/backup/book.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print("Backup completed")
        PublicLibraryHelper.press_to_continue()

    @staticmethod
    def restore_back_up(dir_path):
        print("---------------------------------------------------------------------------")
        if os.path.isfile(dir_path+'/data/backup/backupUser.json') and os.path.isfile(dir_path+'/data/backup/loanList.json') and os.path.isfile(dir_path+'/data/backup/book.json'):
            with open(dir_path+'/data/backup/backupUser.json') as json_file:
                data = json.load(json_file)

            with open(dir_path+'/data/user.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

            with open(dir_path+'/data/backup/loanList.json') as json_file:
                data = json.load(json_file)

            with open(dir_path+'/data/loanList.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

            with open(dir_path+'/data/backup/book.json') as json_file:
                data = json.load(json_file)

            with open(dir_path+'/data/book.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
            print("Backups has been restored")
        else:
            print("No backups available")
        PublicLibraryHelper.press_to_continue()

    @staticmethod
    def fill_system(dir_path):
        with open(dir_path + '/data/import/booksset1.json') as json_file:
            data = json.load(json_file)
            for res in data:
                nb = Book.Book(res["title"], res["country"], res["language"], res["link"], str(res["pages"]),
                               str(res["year"]), res["imageLink"], res["author"])
                BookHelper.BookHelper.add_book_item(nb)

        # read csv file
        with open(dir_path + '/data/import/FakeNameSet20.csv', encoding='utf-8') as csvf:
            # load csv file data using csv library's dictionary reader
            csvReader = csv.DictReader(csvf)

            # convert each csv row into python dict
            for row in csvReader:
                # add this python dict to json array

                user = UserModel.User(str(row['Username']),
                                      str(row['GivenName']),
                                      str(row['Gender']),
                                      str(row['GivenName']),
                                      str(row['Surname']),
                                      str(row['ZipCode']),
                                      str(row['City']),
                                      str(row['EmailAddress']),
                                      str(row['TelephoneNumber']),
                                      str(0),
                                      str(row['StreetAddress']),
                                      True)
                PersonHelper.PersonHelper.register_user(user)
        print("---------------------------------------------------------------------------")
        print("The system has been filled")
        print("***For the new users from the import they use there givenName as password")
        PublicLibraryHelper.press_to_continue()

    @staticmethod
    def empty_system(dir_path):
        with open(dir_path + '/data/empty/user.json') as json_file:
            data = json.load(json_file)

        with open(dir_path + '/data/user.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        with open(dir_path + '/data/empty/loanList.json') as json_file:
            data = json.load(json_file)

        with open(dir_path + '/data/loanList.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        with open(dir_path + '/data/empty/book.json') as json_file:
            data = json.load(json_file)

        with open(dir_path + '/data/book.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("---------------------------------------------------------------------------")
        print("The system is now emptied")
        PublicLibraryHelper.press_to_continue()

    @staticmethod
    def press_to_continue():
        input("Press enter to continue")
