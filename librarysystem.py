class Book:
    def __init__(self, title , author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed == True
            print(self.title, "has been borrowed")
        else:
            print(self.title, "has already been borrowed")
    
    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed == False
            print(self.title, "has been returned")
        else:
            print(self.title, "was not borrowed")
        
book1 = Book("A tale of two cities", "Charles Dickens")
book2 = Book("Harry potter and the prisoner of azkaban", "JK Rowling")
book3 = Book("Christmas Carol", "Charles Dickens")

book1.borrow()
book2.borrow()
book3.borrow()

book1.return_book()
book2.return_book()
book3.return_book()
        