import datetime


class Employee:

	raise_amount = 1.02

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = "{}.{}@mail.com".format(first, last).lower()

	def return_fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

	def __str__(self):
		return'{} - {}'.format(self.return_fullname(), self.email)

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.return_fullname())


emp_1 = Employee("Simeon", "Chakarov", 47000)
emp_2 = Employee("Ivaylo", "Draganov", 51000)

# print(repr(emp_1))
# print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

print(1+2)

print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

print(emp_1 + emp_2)


print(len('test'))
print('test'.__len__())

print(len(emp_1))
print(emp_1.__len__())
