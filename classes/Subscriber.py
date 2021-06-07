import json
class Subscriber:
    def __init__(self, personId):
        self.personId = personId

    def checkSubscriberStatus(self,personId):
        status = False
        json_lines = []
        with open("../data/user.json", "r") as sub:
            for x in sub.readlines():
                data = json.load(x)
                if data['userId'] == self.personId:
                    status = True
                else:
                    json_lines.append(x)
        if status == True:
            return "U are subscribed"
        else:
            with open("../data/user.json", "a") as sub:
                sub.writelines('\n'.join(json_lines))
            return "U are not subscriberd"
              
