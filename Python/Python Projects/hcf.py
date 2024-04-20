'''1. This is a function to find the highest common factor of two numbers

 def hcf(x,y):
        x=abs(x)
        y=abs(y)
        smaller = y if x>y else x
        s = smaller
        while s>0:
            if x%s==0 and y%s==0:
                break
            s-=1
        return s
Make it a static method in the Fraction class that you had written in earlier exercise.'''


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

    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1
        return s


f1 = Fraction(2, 3)
f2 = Fraction(3, 4)

print(Fraction.hcf(f2.nr, f2.dr))




