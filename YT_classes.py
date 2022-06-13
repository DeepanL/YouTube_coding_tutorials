# Classes and Instances

class Employee:
    # when we create methods within a class they recieve the first instance automatically
    # by convention this is self

    # this is a class variable
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first_name, last_name, pay):
        self.first = first_name
        self.last = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'
        Employee.num_of_emp +=1
         # initalize method or co 
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# These are called instance variables
print(Employee.num_of_emp)

emp_1 = Employee('Corey', 'Schafer', 500000) # instance of class Employee
emp_2 = Employee('Deepan', 'Lobo', 90000)

print(Employee.num_of_emp)

# emp_1.raise_amount = 1.05
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)

# # print(emp_1.email)
# # print(emp_2.email)

# print(emp_1.fullname())
# print(emp_2.fullname())

# print(Employee.fullname(emp_1)) # this is same as emp1.fullname()