
def start():
    while(True):


        print("Enter 1. To add a book")
        print("Enter 2. To add a customer")
        print("Enter 3. To add a client")

        result = BookHelper.BookHelper.search_book("asdf")

        # print("Enter 1. To search for a book")
        # print("Enter 2. To loan a book")
        # print("Enter 3. To add a new customer")
        # print("Enter 4. To add a new book")
        # print("Enter 5. To make a backup")
        # print("Enter 6. To restore the backup")
        # print("Enter 7. To exit the application")
        try:
            x = int(input("Select a choice from 1...: "))
            pbl = publicLibrary.PublicLibrary()
            x = int(input("Select a choice from 1...: "))
            if x > 0:
                PageHelper.PageHelper.clear()
            if x == 1:
                bookTitle = str(input("Title: "))
                bookCountry = str(input("Country: "))
                bookLangue = str(input("Language: "))
                bookLink = str(input("Link: "))
                bookPages = str(input("Pages: "))
                bookYear = str(input("Year: "))
                bookImageLink = str(input("Image link: "))
                bookAuthor = str(input("Book author: "))
                newBook = Book.Book(bookTitle, bookCountry, bookLangue, bookLink, bookPages, bookYear,
                                    bookImageLink, bookAuthor)
                BookHelper.BookHelper.add_book_item(newBook)
                if result == False:
                    print('This book is already initialized')
                else:
                    print('Book ' + bookTitle + ' Has been added')

                str(input("Please enter a key to continue"))
            elif x == 2:
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

                result = newUser.addNewUser('customer')
                if result == False:
                    print('This customer is already initialized')
                else:
                    print('Customer ' + firstname + ' ' + surname + ' has been added')

                str(input("Please enter a key to continue"))

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

                newUser = classUser.User(nameSet, gender, firstname, surname, zipCode, city, emailAddress,
                                         telephoneNumber, age, address)

                result = newUser.addNewUser('client')
                if result == False:
                    print('This client is already initialized')
                else:
                    print('Client ' + firstname + ' ' + surname + ' has been added')
                str(input("Please enter a key to continue"))
            PageHelper.PageHelper.clear()
            # if x == 1:
            #     name = str(input("Choose here your book: "))
            #     value = pbl.searchBook(name)
            #     print(value)
            # elif x == 2:
            #     newLoonItem = loan.LoanItem()
            #
            #     bookTitle = int(input("Enter a id book: "))
            #
            #     newBook = newLoonItem.checkBoekAvailable(bookTitle)
            #
            #     userid = int(input("user id: "))
            #     newUser = newLoonItem.checkUserAvaiable(userid)
            #     newLoonItem.loan(newUser, newBook)
            #
            #     print('Job succeeded')
            # elif x == 3:
            #     nameSet = str(input("Nameset: "))
            #     gender = str(input("Gender: "))
            #     firstname = str(input("Firstname: "))
            #     surname = str(input("Surname: "))
            #     zipCode = str(input("Zipcode: "))
            #     city = str(input("City: "))
            #     emailAddress = str(input("Email address: "))
            #     telephoneNumber = str(input("Phone number: "))
            #     age = str(input("age: "))
            #     address = str(input("Address: "))
            #
            #     newUser = classUser.User(nameSet, gender, firstname, surname, zipCode, city, emailAddress, telephoneNumber, age, address)
            #
            #     newUser.addNewUser()
            #     print('User '+ firstname + ' ' +surname  + ' Has been added')
            # elif x == 4:
            #     bookTitle = str(input("Title: "))
            #     bookCountry = str(input("Country: "))
            #     bookLangue = str(input("Language: "))
            #     bookLink = str(input("Link: "))
            #     bookPages = str(input("Pages: "))
            #     bookYear = str(input("Year: "))
            #     bookImageLink = str(input("Image link: "))
            #     bookAuthor = str(input("Book author: "))
            #     newBook = book.Book(bookTitle, bookCountry, bookLangue, bookLink, bookPages, bookYear,
            #                         bookImageLink, bookAuthor)
            #     newBook.addNewBook()
            #
            #     print('Book ' + bookTitle + ' Has been added')
            # elif x == 5:
            #     pbl.backUp()
            #
            #     print("Back up has been done")
            # elif x == 6:
            #     pbl.restoreBackUp()
            #
            #     print("Back up has been restored")
            # elif x == 7:
            #     print("Thank you for using library management system")
            #     break
            # else:
            #     print("Please enter a valid choice from 1...")
        except ValueError:
            print("Please input as suggested." + ValueError)