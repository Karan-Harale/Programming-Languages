'''Create a list named books that contains the 4 Book instance objects that you have created in question 2. Iterate over this list using a for loop and call display() for each object in the list.'''


class Book:

    def __init__(self, isbn, title, author, publisher, pages, price, copies):

        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price =  price
        self.copies = copies

    @property
    def price(self):
        return self._price  # Getter method to retrieve the price

    @price.setter
    def price(self, value):
        if 50 <= value <= 1000:
            self._price = value
        else:
            raise ValueError("Price must be between 50 and 1000")

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

    def findAuthor(self,authname):
        if self.author == authname:
            return self.title
        else:
            None




book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)


books = [book1,book2,book3,book4]

for i in range(len(books)):
    print(books[i].display())

#'''Write a list comprehension to create another list that contains title of books written by Jack.'''

jacksbooks = []

for i in range(len(books)):
    jacksbooks.append(books[i].findAuthor("Jack"))

while jacksbooks.__contains__(None):
    jacksbooks.remove((None))

print(jacksbooks)


# In the Book class, create a property named price such that the price of a book cannot be less than 50 or more than 1000.

