
import json
class BookItem():
    def __init__(self, bookTitle):
       self.bookTitle = bookTitle
    def changeItemState(self,bookTitle):
        State = False
        with open("../data/import/booksset1.json", "+") as f:
            data = f.readlines()



