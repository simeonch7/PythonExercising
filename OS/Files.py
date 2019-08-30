#Not recommended open
f = open('SomeText.txt', 'r')
print("{} -> {}".format(f.name, f.mode))
f.close()

#context manager
with open('SomeText.txt', 'r') as f:	#also throws exception
	pass

	#DIFFERENT WAYS TO READ
	# f_contents = f.read(10)
	# print(f_contents)

	# f_contents = f.read(10) #if EOF => returns empty string
	# print(f_contents)

	# size_to_read = 10

	# f_contents = f.read(size_to_read)
	# print(f_contents)	

	# f.seek(0)

	# f_contents = f.read(size_to_read)
	# print(f_contents)	

	# print(f.tell())


	# while len(f_contents) > 0:
	# 	print(f_contents, end = "*")	
	# 	f_contents = f.read(size_to_read)

	
	# f_contents1 = f.readlines()
	# print(f_contents1)


	# f_contents2 = f.readline()
	# print(f_contents2, end='')

	# f_contents2 = f.readline()
	# print(f_contents2, end='')

	# for line in f:
	# 	print(line, end='')

# print(f.closed)

#WRITE IN FILE

# with open('test2.text', 'w') as f:
# 	pass
	# f.write('TEST')
	# f.seek(0)
	# f.write('TEST')


#copy textfile

with open('SomeText.txt', 'r') as rf:
	with open('SomeText_Copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)

#copy picture
with open('pic.jpeg', 'rb') as rf: #binary
	with open('pic_Copy.jpeg', 'wb') as wf:
		for line in rf:
			wf.write(line)

#copy picture 
with open('pic.jpeg', 'rb') as rf: #binary
	with open('pic_Copy.jpeg', 'wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)
