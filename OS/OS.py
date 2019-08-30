import os
from datetime import datetime
# print(dir(os))
os.chdir("C:/Users/simeon.chakarov/Desktop")

print(os.getcwd())
print(os.listdir())

if not os.path.exists('C:/Users/simeon.chakarov/Desktop/dir'):
	os.mkdir('dir') #makedirs -> for subdirectory and more

if not os.path.exists('C:/Users/simeon.chakarov/Desktop/dir/hello'):
	os.makedirs('dir/hello')

os.rmdir("C:/Users/simeon.chakarov/Desktop/dir/hello")

if not os.path.exists('C:/Users/simeon.chakarov/Desktop/dir1'):
	os.rename('dir', 'dir1')
print(os.stat('dir1'))
print(os.stat('dir1').st_size)

mod_time = os.stat('dir').st_mtime
print(datetime.fromtimestamp(mod_time))

for dirpath, dirnames, filenames in os.walk("C:/Users/simeon.chakarov/Desktop/"):
	print('Current path: ', dirpath)
	print('Directories: ', dirnames)
	print('Files: ', filenames)
print("$$$$$$$$$$$$$$$")
print(os.environ.get('HOMEPATH'))

dir_path = os.path.join(os.environ.get('HOMEPATH'), 'dir')
print(dir_path)
print(os.path.splitext("/tmp/test/test.txt")) # to take extensions or the file name itself
