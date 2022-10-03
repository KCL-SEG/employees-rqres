"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, total_pay, type, salary, hourly_pay, hours, commission, number_contracts):
        self.name = name
        self.total_pay = total_pay
        self.type = type
        self.salary = salary
        self.hourly_pay = hourly_pay
        self.hours = hours
        self.commission = commission
        self.number_contracts = number_contracts

    @classmethod
    def as_hourly_worker(cls, name, hourly_pay, hours, commission=0, number_contracts=0):
        pay = hourly_pay * hours + commission * (number_contracts if number_contracts != 0 else 1)
        return cls(name, pay, "hourly", -1, hourly_pay, hours, commission, number_contracts)

    @classmethod
    def as_salary_worker(cls, name, salary, commission=0, number_contracts=0):
        pay = salary + commission * ( number_contracts if number_contracts != 0 else 1 )
        return cls(name, pay, "salary", salary, -1, -1, commission, number_contracts)

    def get_pay(self):
        return self.total_pay

    def __str__(self):
        string = f"{self.name} works on a " + f"{f'monthly salary of {self.salary}' if self.type =='salary' else f'contract of {self.hours} hours at {self.hourly_pay}/hour'}"

        if self.commission > 0 and self.number_contracts <= 0:
            string += f" and receives a bonus commission of {self.commission}."
        elif self.commission > 0 and self.number_contracts > 0:
            string += f" and receives a commission for {self.number_contracts} contract(s) at {self.commission}/contract."
        else:
            string += "."
        
        string += f"  Their total pay is {self.total_pay}."

        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee.as_salary_worker('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee.as_hourly_worker('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee.as_salary_worker('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee.as_hourly_worker('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee.as_salary_worker('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee.as_hourly_worker('Ariel', 30, 120, 600)
