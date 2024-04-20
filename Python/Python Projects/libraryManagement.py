'''Q2. Create a class named Book with an __init__ method. Inside the __init__ method, create the instance variables isbn, title, author, publisher, pages, price, copies.

Create these four instance objects from this class.

book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)
Write a method display that prints the isbn, title, price and number of copies of the book.

'''

class Book:

    def __init__(self, isbn, title, author, publisher, pages, price, copies):

        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    def display(self):
        return print(f"isbn: { self.isbn} \ntitle: {self.title}\nprice: { self.price}\nnumber of copies: { self.copies}\n\n")

#'''3. For the Book class that you have created, write a method named in_stock that returns True if number of copies is more than zero, otherwise it returns False.

#Create another method named sell that decreases the number of copies by 1 if the book is in stock, otherwise it prints the message that the book is out of stock.'''

    def in_stock(self):
        result = False
        if self.copies > 0:
            result = True
        else:
            result = False

        return result

    def sell (self):
        return self.copies - 1




book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)


book1.display()
book2.display()
book3.display()
book4.display()

book1.in_stock()
print(book1.in_stock())

if book1.in_stock() == True:
    r=book1.sell()
    print("number of copies: ",r)
else:
    print("Book is out of Stock")

