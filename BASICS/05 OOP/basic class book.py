# book1 = Book("Ola Kowalska", "Podróże", "DGUAGD&*AS", 2020)
# book1.printData() ERRORRRRR

class Book:
    def __init__(self, author, title, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year

    # def __init__(self, author):
    #     self.author = author         TYLKO 1 KONSTRUKTOR INACZEJ TEN PÓŹNIEJSZY NADPISZE WCZEŚNIEJSZY

    def printData(self):
        print(self.author, self.title, self.isbn, self.year)


book1 = Book("Ola Kowalska", "Podróże", "DGUAGD&*AS", 2020)
book1.printData()

book1 = Book("Ola Kowalska", "Podróże", "DGUAGD&*AS", 2020)
book1.printData()

