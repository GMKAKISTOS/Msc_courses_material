import decimal

class classinfo:
    firstname: str
    lastname: str
    age: int
    salary: decimal.Decimal

    def __init__(
        self,
        firstname="panagiwths",
        lastname="chronopoulos",
        age=27,
        salary=1250.50
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.salary = decimal.Decimal(str(salary))

    def netsalary(self):
        return self.salary

    def grosssalary(self):
        return self.netsalary() - (self.netsalary() * 50/100)

    def coststatus(self):
        status = "expensive!" if self.grosssalary() >= 10000 else "medium!" if self.grosssalary() >= 5000 and self.grosssalary() < 10000 else "cheap!"
        print(status)

    def __str__(self):
        return (
            f"Firstname: {self.firstname.capitalize()}\n"
            f"Lastname: {self.lastname.capitalize()}\n"
            f"Age: {self.age}\n"
            f"Salary: {self.grosssalary():.2f}"
        )

class classinfo2(classinfo):
    #pass

    def test(self):
        print("we are in classinfo2!")
