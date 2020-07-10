import unittest
class Library():
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self): # przejrzenie zasobu
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook): # przeywrócenie książki do zasobu
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service :)")
 
class Customer():
    book = ""
    haveBook = False
    def requestBook(self, book):
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self):
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False
 
 
def setup():
    size(220,100)
 
    if __name__ == '__main__':
        unittest.main()
   
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20) # do wypożyczania
    rect(100,40,100,20) # do zwracania
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)
 
def mouseClicked():
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Madzia.requestBook("Naocznosc"))
        if mouseY >40 and mouseY <60:
            library.addBook(Madzia.returnBook())
 
class testCaseOne(unittest.TestCase):
    Madzia = Customer()
    def testHasBook(self):
        self.assertTrue(self.Madzia.haveBook == False)
        
class testCaseTwo(unittest.TestCase):
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
    library = Library(books)
    def testUniqueBooks(self):
        unique = True
        for i in range(len(self.books)):
            for j in range(len(self.books)):
                if i == j:
                    continue
                if self.books[i] == self.books[j]:
                    unique = False
                    break
            if not unique:
                break
        self.assertTrue(unique)
