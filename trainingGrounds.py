helplist = {'Help': 'Displays list of actions', 'Calculator': 'Opens calculator!', 'Catalog': 'Opens the catalog!'}
cataloglist = dict()


# create global variable currency
def initgold():
	currency = 500
	return currency


# grab global currency variable
def grabgold():
	global gold
	gold = initgold()
	return gold


# reset shopkeep.txt to original state
def resetshop():
	fhand = open('shopkeep.txt', 'w')
	fhand.write('Sword,3,120\nDagger,2,60\nPotion,0,25')


# split each shopkeep.txt line into a list then nest each list into shopstock
def itemsplit():
	fhand = open('shopkeep.txt', 'r')
	grabshop = fhand.read().splitlines()
	shopstock = list()
	for i in range(len(grabshop)):
		shopitem = grabshop[i].split(",")
		shopstock.append(shopitem)
	return shopstock


# display shop items using itemsplit for user to purchase
def displayitems():
	print('Here is what I have for sale!')
	shopitem = itemsplit()
	for i in range(len(shopitem)):
		if shopitem[i][1] != '0':
			print(shopitem[i][0] + '(' + shopitem[i][1] + ')' + ': ' + shopitem[i][2] + 'g')


# checks if user specified item is in shopstock created by itemsplit func
def itemcheck(item):
	shopstock = itemsplit()
	for i in range(len(shopstock)):
		if item != shopstock[i][0]:
			continue
		elif item == shopstock[i][0]:
			return 'true'


# function to check if user specified quantity is less than or equal to shopstock qty
def quantitycheck(item, quantity):
	shopstock = itemsplit()
	for i in range(len(shopstock)):
		if item == shopstock[i][0] and int(quantity) <= int(shopstock[i][1]):
			hasqty = 'true'
			price = int(shopstock[i][2]) * int(shopstock[i][1])
			position = shopstock[i].index(item)
			return [hasqty, price, position]
		else:
			hasqty = 'false'
			return hasqty


# function to update shopstock after purchase
def updatestock(item, quantity, position):
	shopstock = itemsplit()
	if quantitycheck(item, quantity)[0] == 'true':
		print(shopstock)
		print(shopstock[position][1])
		newqty = int(shopstock[position][1]) - int(quantity)
		print(newqty)
		shopstock[position][1] = str(newqty)
		print(shopstock[0][0] + ',' + shopstock[0][1] + ',' + shopstock[0][2])
		fhand = open('shopkeep.txt', 'w')
		for i in range(len(shopstock)):
			fhand.write(shopstock[i][0] + ',' + shopstock[i][1] + ',' + shopstock[i][2] + '\n')


def sbuy(currentgold):
	print(currentgold)
	displayitems()
	buyitem = input('What would you like to purchase?\n')
	if itemcheck(buyitem) == 'true':
		buyqty = input('How many would you like to buy?\n')
		if quantitycheck(buyitem, buyqty)[0] == 'true':
			price = quantitycheck(buyitem, buyqty)[1]
			position = quantitycheck(buyitem, buyqty)[2]
			if currentgold >= price:
				print("You have enough gold! Enjoy!")
				currentgold -= price
				updatestock(buyitem, buyqty, position)
				shop(currentgold)
			else:
				print("Sorry Link, I can't GIVE credit. Come back when you're a little mmmm RICHER!")
		else:
			print("I don't have that many of that item!")
	else:
		print("I don't have that item.")
	shop(currentgold)


def shop(currency):
	currentgold = currency
	print('Welcome adventurer! Have you come to browse my wares?')
	print('*You currently have ', currentgold, ' gold*')
	action = input('[B]uy | [S]ell | Check [I]nventory \n')
	if action == 'B':
		sbuy(currentgold)


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
		initgold()
		resetshop()
		gold = grabgold()
		shop(gold)
	else:
		print('I am not sure what you are asking. For a list of actions type help in the prompt.')
	directory()
	

directory()
