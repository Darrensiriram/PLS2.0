import json
import csv

class User:
    def __init__(self,  nameSet, gender, firstname, surname, zipCode, city, emailAddress, telephoneNumber, age, address):
        self.userId = hash(nameSet + gender + firstname + surname + zipCode + city + emailAddress + telephoneNumber + age + address)
        self.userNameSet = nameSet
        self.userGender = gender
        self.userFirstname = firstname
        self.userSurname = surname
        self.userZipCode = zipCode
        self.userCity = city
        self.userEmailAddress = emailAddress
        self.userTelephoneNumber = telephoneNumber
        self.userAge = age
        self.userAddress = address

    def addNewUser(self, set):

        result = False
        with open('data/'+set+'.json', 'r') as json_file:
            data = json.load(json_file)
            for book in data['results']:
                if book['userId'] == self.userId:
                    result = True

        if not result:
            with open('data/'+set+'.json') as json_file:
                data = json.load(json_file)

                temp = data['results']

                new_data = {
                    'userNameSet': self.userNameSet,
                    'userId': self.userId,
                    'userGender': self.userGender,
                    'userFirstname': self.userFirstname,
                    'userSurname': self.userSurname,
                    'userZipCode': self.userZipCode,
                    'userCity': self.userCity,
                    'userEmailAddress': self.userEmailAddress,
                    'userTelephoneNumber': self.userTelephoneNumber,
                    'userAge': self.userAge,
                    'userAddress': self.userAddress,
                }
                temp.append(new_data)

            write_json(data)
        else:
            return False


    def fillUsers(self):
        def write_json(data, filename='data/user.json'):
            with open(filename, 'a') as f:
                json.dump(data, f, indent=4)

        jsonArray = []

        # read csv file
        with open('data/FakeNameSet20.csv', encoding='utf-8') as csvf:
            # load csv file data using csv library's dictionary reader
            csvReader = csv.DictReader(csvf)

            # convert each csv row into python dict
            for row in csvReader:
                # add this python dict to json array
                jsonArray.append(row)

        # convert python jsonArray to JSON String and write to file
        with open('data/user.json') as json_file:
            data = json.load(json_file)

            temp = data['results']
            temp.append(jsonArray)
        write_json(data, 'user.json')