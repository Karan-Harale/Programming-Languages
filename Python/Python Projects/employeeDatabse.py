
class Employee:
    domains = set()

    def __init__(self ,name ,email ):
        self.name = name
        self.email = email
        self._add_domain()

    def display(self):
        print(self.name, self.email)

    def _add_domain(self):
        domain = self.email.split('@')[1] if '@' in self.email else None
        if domain:
            Employee.domains.add(domain)

e1 = Employee('John' ,'john@gmail.com')
e2 = Employee('Jack' ,'jack@yahoo.com')
e3 = Employee('Jill' ,'jill@outlook.com')
e4 = Employee('Ted' ,'ted@yahoo.com')
e5 = Employee('Tim' ,'tim@gmail.com')
e6 = Employee('Mike' ,'mike@yahoo.com')


print(Employee.domains)
