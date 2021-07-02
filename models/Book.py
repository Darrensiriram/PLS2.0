class Book:
    def __init__(self, book_title, book_country, book_language, book_link,
                 book_pages, book_year, book_image_link, book_author):
        self.bookId = hash(book_title + book_country + book_language + book_link +
                           book_pages + book_year + book_image_link + book_author)
        self.bookTitle = book_title
        self.bookCountry = book_country
        self.bookLanguage = book_language
        self.bookLink = book_link
        self.bookPages = book_pages
        self.bookYear = book_year
        self.bookImageLink = book_image_link
        self.bookAuthor = book_author
