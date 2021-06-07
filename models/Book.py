class Book:
    def __init__(self,bookTitle,bookCountry,bookLangue,bookLink,bookPages,bookYear,bookImageLink,bookAuthor):
        self.bookId = hash(bookTitle +bookCountry+bookLangue+bookLink+bookPages+bookYear+bookImageLink+bookAuthor)
        self.bookTitle = bookTitle
        self.bookCountry = bookCountry
        self.bookLanguage = bookLangue
        self.bookLink = bookLink
        self.bookPages = bookPages
        self.bookYear = bookYear
        self.bookImageLink = bookImageLink
        self.bookAuthor = bookAuthor