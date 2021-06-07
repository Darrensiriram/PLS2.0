import csv
import json
import User as classUser
import PublicLibary as publicLibrary
import Book as book
import LoanItem as loan

def start():
    while(True):    
        print("                       Welcome to the Public library system                ")
        print("---------------------------------------------------------------------------")
        print("Enter 1. To search for a book")
        print("Enter 2. To loan a book")
        print("Enter 3. To add a new customer")
        print("Enter 4. To add a new book")
        print("Enter 5. To make a backup")
        print("Enter 6. To restore the backup")
        print("Enter 7. To exit the application")
        try:
            pbl = publicLibrary.PublicLibrary()
            x = int(input("Select a choice from 1...: "))
            print()
            if x == 1:
                name = str(input("Choose here your book: "))
                value = pbl.searchBook(name)
                print(value)
            elif x == 2:
                bookTitle = str(input("Enter a title: "))
                if loan.LoanItem.loan == "Book has been added as borrowed.":
                    return bookTitle + " is borrowed"
                else:
                    return bookTitle + " has already been borrowed."
            elif x == 3:
                nameSet = str(input("Nameset: "))
                gender = str(input("Gender: "))
                firstname = str(input("Firstname: "))
                surname = str(input("Surname: "))
                zipCode = str(input("Zipcode: "))
                city = str(input("City: "))
                emailAddress = str(input("Email address: "))
                telephoneNumber = str(input("Phone number: "))
                age = str(input("age: "))
                address = str(input("Address: "))

                newUser = classUser.User(nameSet, gender, firstname, surname, zipCode, city, emailAddress, telephoneNumber, age, address)

                newUser.addNewUser()
                print('User '+ firstname + ' ' +surname  + ' Has been added')
            elif x == 4:
                bookTitle = str(input("Title: "))
                bookId = str(input("Nameset: "))
                bookCountry = str(input("Country: "))
                bookLangue = str(input("Language: "))
                bookLink = str(input("Link: "))
                bookPages = str(input("Pages: "))
                bookYear = str(input("Year: "))
                bookImageLink = str(input("Image link: "))
                bookAuthor = str(input("Book author: "))
                newBook = book.Book(bookTitle, bookId, bookCountry, bookLangue, bookLink, bookPages, bookYear,
                                    bookImageLink, bookAuthor)
                newBook.addNewBook()

                print('Book ' + bookTitle + ' Has been added')
            elif x == 5:
                pbl.backUp()

                print("Back up has been done")
            elif x == 6:
                pbl.restoreBackUp()

                print("Back up has been restored")
            elif x == 7:
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from 1...")
        except ValueError:
            print("Please input as suggested." + ValueError)
start()
3