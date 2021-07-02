class User:
    def __init__(self, name_set, password, gender, firstname, surname, zip_code, city, email_address,
                 tele_phone_number, age, address, customer):
        self.userId = hash(name_set + gender + firstname + surname + zip_code +
                           city + email_address + tele_phone_number + age + address)
        self.userNameSet = name_set
        self.userPassword = password
        self.userGender = gender
        self.userFirstname = firstname
        self.userSurname = surname
        self.userZipCode = zip_code
        self.userCity = city
        self.userEmailAddress = email_address
        self.userTelephoneNumber = tele_phone_number
        self.userAge = age
        self.userAddress = address
        self.userCustomer = customer
