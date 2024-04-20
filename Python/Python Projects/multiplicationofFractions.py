'''Q7. Define a method named multiply that multiples two Fraction instance objects. For multiplying two fractions, you have to multiply the numerator with numerator and denominator with the denominator.

Inside the method, create a new instance object that is the product of the two fractions and return it. Write your method in such a way that it supports multiplication of a Fraction by an integer also.

Similarly define a method named add to add two Fraction instance objects. Sum of two fractions n1/d1 and n2/d2 is (n1*d2 + n2*d1) / (d1*d2). This method should also support addition of a Fraction by an integer.

Test your fraction class with this code.

f1 = Fraction(2,3)
f1.show()
f2 = Fraction(3,4)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5)
f3.show()
f3 = f1.multiply(5)
f3.show()
The output that you should get is given below.

2/3

3/4

6/12

17/12

17/3

10/3'''

class Fraction:

    def __init__(self , nr, dr = 1):

        if dr < 0:
            nr = -nr
            dr = -dr

        self.nr = nr
        self.dr = dr


    def show(self):
        return f"{self.nr}/{self.dr}"

    def multiply(self, f):

        p = Fraction(f)

        resultnr = self.nr * f.nr
        resultdr = self.dr * f.dr

        return f"Multiplication: {resultnr}/{resultdr}"

    def add(self , n):

        n2 = Fraction(n)

        resultnr = (self.nr * n.dr)+(n.nr * self.dr)
        resultdr = self.dr * n.dr
        return f"Addition: {resultnr}/{resultdr}"


f1=Fraction(2,3)
f2=Fraction(3,4)

print(f1.show())
print(f2.show())
print(f1.multiply(f2))
print(f1.add(f2))