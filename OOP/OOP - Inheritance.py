class Employee:

	raise_amount = 1.02

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = "{}.{}@mail.com".format(first, last).lower()

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
	# pass
	raise_amount = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):

	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_empolyee(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_empolyee(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('--->', emp.fullname())

dev_1 = Developer("Simeon", "Chakarov", 47000, "Python")
dev_2 = Developer("Ivaylo", "Draganov", 51000, "Java")
dev_3 = Developer("Bobby", "Ivanov", 80000, "Pascal")

# print(dev_1.email)
# print(dev_1.prog_lang)


# print(help(Developer))

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

mgr_1 = Manager("Ekaterina", "Chakarova", 70000, [dev_1])
print(mgr_1.email)
mgr_1.print_emps()

print("######")
mgr_1.add_empolyee(dev_1)
mgr_1.add_empolyee(dev_2)
mgr_1.add_empolyee(dev_3)
# mgr_1.remove_empolyee(dev_2)

mgr_1.print_emps()

# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer))

# print(issubclass(Manager, Employee))
# print(issubclass(Developer, Employee))
# print(issubclass(Developer, Manager))
