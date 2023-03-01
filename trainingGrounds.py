helplist = {'Help': 'Displays list of actions', 'Calculator': 'Opens calculator!', 'Catalog': 'Opens the catalog!'}
cataloglist = dict()


def getfile():
	file = input('What file would you like to access? ') + '.txt'
	return file


def readfile():
	file = getfile()
	fhand = open(file, 'r')
	print(fhand.read())


def appendfile():
	file = getfile()
	fhand = open(file, 'a')
	newcontent = input('What text would you like to add to ' + file + '?')
	fhand.write('\n' + newcontent)
	print('Content, "' + newcontent + '", has been added to ' + file + '!')


def clearfile():
	file = getfile()
	fhand = open(file, 'w')
	fhand.write("")


def accessfile():
	ftask = input('Would you like to read, write to, or clear a file? ')
	if ftask == 'read':
		readfile()
		accessfile()
	elif ftask == 'write':
		appendfile()
		accessfile()
	elif ftask == 'clear':
		clearfile()
		accessfile()
	elif ftask == 'back':
		directory()
	else:
		print('I am not sure what you are asking?')
		accessfile()


def compute():
	print('Welcome to Calculator!')
	number1 = input('Please type the first number: ')
	number2 = input('Please type the second number: ')
	mathsign = input('Would you like to add, subtract, multiply, or divide? ')

	if mathsign == 'add':
		answer = (int(number1) + int(number2))
	elif mathsign == 'subtract':
		answer = (int(number1) - int(number2))
	elif mathsign == 'multiply':
		answer = (int(number1) * int(number2))
	elif mathsign == 'divide':
		if number2 == '0':
			answer = 'Cannot divide by zero!'
		else:
			answer = (int(number1) / int(number2))
	elif mathsign == 'titan':
		answer = 'Dispensing crayons...'
	elif mathsign == 'warlock':
		answer = 'Go up...'
	elif mathsign == 'hunter':
		answer = 'Shatterskate go brrr...'
	else:
		answer = 'I cannot do that.'
	print(answer)


def catalog():
	global cataloglist
	ctask = input('Would you like to view, append to, delete item from, or clear the catalog? ')
	if ctask == 'view':
		if cataloglist == {}:
			print('This catalog is empty!')
		else:
			print(cataloglist)
	elif ctask == 'append':
		cname = input('What would you like to name this entry? ')
		cvalue = input('What value would you like to give this entry? ')
		cataloglist[cname] = cvalue
		print('Entry ' + cname + ' added to catalog!')
	elif ctask == 'delete':
		if cataloglist == {}:
			print('This catalog is empty!')
		else:
			print(cataloglist)
			cname = input('Which entry would you like to delete? ')
			del cataloglist[cname]
			print('Entry ' + cname + ' delete from catalog!')
	elif ctask == 'clear':
		print('Catalog cleared!')
		cataloglist = {}
	elif ctask == 'sort':
		cataloglist = sorted(cataloglist.items())
		print('Catalog sorted!')
	elif ctask == 'back':
		directory()
	else:
		print('Unknown command...')
	catalog()


def directory():
	task = input('What would you like to do? ')
	if task == 'help':
		print(helplist)
	elif task == 'calculator':
		compute()
	elif task == 'catalog':
		print('Welcome to the catalog!')
		catalog()
	elif task == 'file':
		print('Welcome to file access!')
		accessfile()
	else:
		print('I am not sure what you are asking. For a list of actions type help in the prompt.')
	directory()
	

directory()
