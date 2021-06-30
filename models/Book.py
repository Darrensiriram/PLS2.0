class Book:
    def __init__(self, book_title,bookCountry,bookLangue,bookLink,bookPages,bookYear,bookImageLink,bookAuthor):
        self.bookId = hash(book_title +bookCountry+bookLangue+bookLink+bookPages+bookYear+bookImageLink+bookAuthor)
        self.bookTitle = book_title
        self.bookCountry = bookCountry
        self.bookLanguage = bookLangue
        self.bookLink = bookLink
        self.bookPages = bookPages
        self.bookYear = bookYear
        self.bookImageLink = bookImageLink
        self.bookAuthor = bookAuthor