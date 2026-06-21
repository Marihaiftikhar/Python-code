class library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
        print(book, " is added")
    def issue_book(self , book):
        if book in self.books:
            self.books.remove(book)
            print(book,"issued")
        else:
            print("book is not found")
    def return_book(self,book):
        self.books.append(book)
        print( book,"returned")
    def show_books(self):
        for book in self.books:
            print (book)
lib = library()

lib.add_book("Python")
lib.add_book("Java")
lib.add_book("C++")

lib.show_books()

lib.issue_book("Java")

lib.show_books()

lib.return_book("Java")

lib.show_books()
            
        
    
              
             

            
        