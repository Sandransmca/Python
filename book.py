class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Publisher:",self.name)
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print( "Title:",self.title)
        print("Author:",self.author)
class Python(Book):
    def __init__(self,name,title,author,price,number_of_pages):
        super().__init__(name,title,author)
        self.price=price
        self.number_of_pages=number_of_pages
    def display(self):
        super().display()
        print("Price:",self.price)
        print("Number of pages:",self.number_of_pages)

book=Python("HarperCollins","The Fifth Mountain","Paulo Coelho",560,213)
book.display()