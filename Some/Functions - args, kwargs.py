def employee_info(*args, **kwargs):
	print(args)
	print(kwargs)

to_do = ['SCRUM', 'DEBUG']
info = {'name': 'John', 'age': '19'}

employee_info(to_do, info)
employee_info(*to_do, **info)