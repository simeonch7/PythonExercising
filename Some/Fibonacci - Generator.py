def fib_generator(num):
	a, b = 0, 1
	for i in range(0, num):
		yield "{}: {}".format(i+1, a)
		a, b = b, a + b

for item in fib_generator(10):
	print(item)