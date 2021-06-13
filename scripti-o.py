# my_file = open('test.txt')

# print(my_file.read())
# my_file.seek(0)
# print(my_file.readlines())
# my_file.seek(0)
# print(my_file.readline())

# my_file.close()

# r+ read and write, overwrite over the existing file
# w write, overwrite all the the file
# a append, add to the end of the file
# r read, only read

# with open('test.txt', mode = 'r+') as my_file:
# 	text = my_file.write('hey it\'s me')
# 	# print(my_file.readlines())
try:
	with open('teswfdst.txt', mode = 'r') as my_file:
		print(my_file.read())
except FileNotFoundError as err:
	print('file does not exists')
	raise err