'''Q8. For the following class Product, create a read only property named selling_price that is calculated by deducting discount from the marked_price. The instance variable discount represents discount in percent.

class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self.discount = discount

    def display(self):
        print(self.id,  self.marked_price,  self.discount)

p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)


Q9. Suppose after some time, you want to give an additional 2% discount on a product, if its price is above 500. To incorporate this change, implement discount as a property in your Product class.
'''

class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self.discount = discount

    def display(self):
        print(self.id, self.marked_price, self.discount)

    @property

    def selling_price(self):
        return self.marked_price - (self.marked_price * (self.discount / 100))

    @property

    def addiscount(self):
        selling_price = self.selling_price
        if selling_price > 500:
            return selling_price * 0.02






p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)

print(p1.id, p1.selling_price)
print(p2.id, p2.selling_price)
print(p3.id, p3.selling_price)
print(p4.id, p4.selling_price)