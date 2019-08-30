import datetime


class Employee:

	raise_amount = 1.02
	num_of_emps = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = "{}.{}@mail.com".format(first, last).lower()
		Employee.num_of_emps += 1

	def return_fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod #alternative constructor
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, int(pay))
	
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

emp_1 = Employee("Simeon", "Chakarov", 47000)
emp_2 = Employee("Ivaylo", "Draganov", 51000)

Employee.set_raise_amt(1.05)
print(Employee.raise_amount)
emp_1.raise_amount = 1.03
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)

emp_str_1 = "Simeon-Simeonov-35000"
emp_str_2 = "Svetoslav-Simeonov-70000"
emp_str_3 = "Lady-Gaga-51000"

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print('{} - {}'.format(id(emp_1.first), id(new_emp_1.first)))
print('{} - {}'.format(id(emp_2.pay), id(new_emp_3.pay)))

new_emp_3.apply_raise()
print("**********{}".format(new_emp_3.pay))

some_date = datetime.date(2000, 4, 25)
print(Employee.is_workday(some_date)) 