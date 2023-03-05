helplist = {'Help': 'Displays list of actions', 'Calculator': 'Opens calculator!', 'Catalog': 'Opens the catalog!'}
cataloglist = dict()
currency = 500
grabshop = open('shopkeep.txt', 'r').read().splitlines()
shopstock = dict()


def itemsplit(item):



def shoplist():
	for i in range(len(grabshop)):
		shopitem = grabshop[i].split(",")
		shopstock


def displayitems():
	for i in range(len(grabshop)):
		shopitem = grabshop[i].split(",")
		if shopitem[1] != '0':
			print(shopitem[0] + '(' + shopitem[1] + ')' + ': ' + shopitem[2] + 'g')


def itemcheck(item):
	for i in range(len(grabshop)):
		shopitem = grabshop[i].split(",")
		if item != shopitem[0]:
			continue
		elif item == shopitem[0]:
			return 'true'
		else:
			return 'false'


def sbuy():
	global currency
	print(currency)
	print('Here is what I have for sale!')
	displayitems()
	buyitem = input('What would you like to purchase?\n')
	if itemcheck(buyitem) == 'true':

		for i in range(len(grabshop)):
			shopitem = grabshop[i].split(",")
			buyqty = input('How many would you like to buy?\n')
			if buyqty <= shopitem[1]:
				price = int(shopitem[2]) * int(buyqty)
				if currency >= price:
					print("You have enough gold! Enjoy!")
					currency -= price
					print(currency)
					break
				else:
					print("Sorry Link, I can't GIVE credit. Come back when you're a little mmmm RICHER!")
					break
			else:
				print("I don't have that many of that item!")
	else:
		print("I don't have that item.")


def shop():
	print('Welcome adventurer! Have you come to browse my wares?')
	print('*You currently have ' + ' gold*')
	action = input('[B]uy | [S]ell | Check [I]nventory \n')


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
	elif task == 'shop':
		sbuy()
	else:
		print('I am not sure what you are asking. For a list of actions type help in the prompt.')
	directory()
	

directory()
