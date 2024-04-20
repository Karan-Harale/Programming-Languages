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