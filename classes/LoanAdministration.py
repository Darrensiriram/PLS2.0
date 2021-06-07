#geeft een output van de mensen die momenteel een boek hebben geleend
import json
class LoanAdministration:
    def __init__(self, bookTitle):
        self.bookTitle = bookTitle
    
    def loanAdministrationOutput():
        with open('../data/loanList.json', 'r') as output:
            data = json.load(output)
            print(json.dumps(data, indent=4, sort_keys= True))