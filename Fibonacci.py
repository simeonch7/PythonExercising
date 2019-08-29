a, b = 0, 1

for i in range(0, 10):
	print(a)
	a, b = b, a + b
	# c = a + b
	# a = b
	# b = c