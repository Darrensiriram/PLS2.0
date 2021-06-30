import json

from controllers.JsonHelper import JsonHelper


class UserHelper:
    @staticmethod
    def get_user():
        print('TODO')

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

        if not UserHelper.user_exist(file, user.userId) and not UserHelper.username_exist(file, user.userNameSet):
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

            JsonHelper.write_json(data, file)
            return True
        else:
            return False

    @staticmethod
    def delete_user():
        print('TODO')

    @staticmethod
    def validate_user(username, password):
        with open('data/user.json') as json_file:
            data = json.load(json_file)
            for line in data['results']:
                if line['userNameSet'] == username and line['userPassword'] == password:
                    return line
        return False
