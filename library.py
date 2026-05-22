class Book:

    def __init__(self, title , author, available=True):
        self.title = title
        self.author = author
        self.__available = available
        

    def borrow_book(self):
        if self.__available:
            
            self.__available = False
            print("Book Borrowed")
        else:
            print("Book not available")

    def return_book(self):

        if  not self.__available:

            self.__available = True
            print("Book Returned")
        else:
            print("Book already available!!")
        
    def show_details(self):
        print(f"Title : {self.title}")
        print(f"Author: {self.author} ")
        print(f"Available : {self.__available}")
      

b1 = Book("Atomic Habits", "James Clear")
b1.borrow_book()
b1.return_book()
b1.show_details()

        