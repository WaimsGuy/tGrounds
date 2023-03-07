helplist = {'Help': 'Displays list of actions', 'Calculator': 'Opens calculator!', 'Catalog': 'Opens the catalog!'}
cataloglist = dict()


# create initial global variable currency
def initgold():
	currency = 500
	return currency


# grab initial currency variable
def grabgold():
	gold = initgold()
	return gold


# reset shopkeep.txt to original state
def resetshop():
	fhand = open('shopkeep.txt', 'w')
	fhand.write('Sword,3,120\nDagger,2,60\nPotion,0,25')  # note: change this code not shopkeep.txt


# split each shopkeep.txt line into a list then nest each list into another list shopstock
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
# note: quantitycheck func does same thing, redundant func?
def itemcheck(item):
	shopstock = itemsplit()
	for i in range(len(shopstock)):
		if item != shopstock[i][0]:
			continue
		elif item == shopstock[i][0]:
			if int(shopstock[i][1]) > 0:
				return 'true'
			else:
				return 'false'


# function to check if user specified quantity is less than or equal to shopstock qty
# fucntion also calculates total price and finds position of specified item
# note: does this func do too many things?
def quantitycheck(item, quantity):
	shopstock = itemsplit()
	for i in range(len(shopstock)):
		if not (item == shopstock[i][0]):
			continue
		elif item == shopstock[i][0] and int(quantity) <= int(shopstock[i][1]):
			hasqty = 'true'
			price = int(shopstock[shopstock.index(shopstock[i])][2]) * int(quantity)  # finds user specified item price
			position = shopstock.index(shopstock[i])  # finds position of specified item, used for updatestock func
			return [hasqty, price, position]
		else:
			hasqty = 'false'
			return hasqty


# function to update shopstock after purchase
def updatestock(item, quantity, position):
	shopstock = itemsplit()
	if quantitycheck(item, quantity)[0] == 'true':
		newqty = int(shopstock[position][1]) - int(quantity)
		shopstock[position][1] = str(newqty)
		fhand = open('shopkeep.txt', 'w')
		for i in range(len(shopstock)):
			fhand.write(shopstock[i][0] + ',' + shopstock[i][1] + ',' + shopstock[i][2] + '\n')


# main function interface for buying items
def sbuy(currentgold):
	print(currentgold)
	displayitems()  # display available items that are in stock
	buyitem = input('What would you like to purchase?\n')
	if itemcheck(buyitem) == 'true':  # check if user specified item exists with qty > 0
		buyqty = input('How many would you like to buy?\n')
		if quantitycheck(buyitem, buyqty)[0] == 'true':  # check if user specified qty exceeds available stock
			price = quantitycheck(buyitem, buyqty)[1]  # grab total cost value from quantitycheck func
			position = quantitycheck(buyitem, buyqty)[2]  # grab position of specified item within parent list
			if currentgold >= price:  # check if player has enough gold
				print("You have enough gold! Enjoy!")
				currentgold -= price  # update player gold after purchase
				updatestock(buyitem, buyqty, position)
				shop(currentgold)  # return to shop function with new gold value
			else:
				print("Sorry Link, I can't GIVE credit. Come back when you're a little mmmm RICHER!")
		elif quantitycheck(buyitem, buyqty)[0] == 'false':
			print("I don't have that many of that item!")
	elif itemcheck(buyitem) == 'false':  # when user tries to force buy item with qty 0
		print('That item is out of stock!')
	else:
		print("I don't have that item.")
	shop(currentgold)


# main shop directory
# note: need to implement sell and inventory func
def shop(currency):
	currentgold = currency
	print('Welcome adventurer! Have you come to browse my wares?')
	print('*You currently have ', currentgold, ' gold*')
	action = input('[B]uy | [S]ell | Check [I]nventory \n')
	if action == 'B':
		sbuy(currentgold)


# does this need a comment?
def getfile():
	file = input('What file would you like to access? ') + '.txt'
	return file


# grab file and print contents
def readfile():
	file = getfile()
	fhand = open(file, 'r')
	print(fhand.read())


# take user input and append to file specified by getfile func
def appendfile():
	file = getfile()
	fhand = open(file, 'a')
	newcontent = input('What text would you like to add to ' + file + '?')
	fhand.write(newcontent + '\n')
	print('Content, "' + newcontent + '", has been added to ' + file + '!')


# does this need a comment?
def clearfile():
	file = getfile()
	fhand = open(file, 'w')
	fhand.write("")


# main file access feature directory
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


# calculator feature
# note: should I add a main directory for this?
def compute():
	print('Welcome to Calculator!')
	number1 = input('Please type the first number: ')
	number2 = input('Please type the second number: ')
	mathsign = input('Would you like to add, subtract, multiply, or divide? ')  # case sensitive
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
	else:
		answer = 'I cannot do that.'
	print(answer)


# early function, grabs cataloglist (which is actually a dictionary) from top of file, could be reworked
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


# main program directory to access various features.
def directory():
	task = input('What would you like to do? ')
	if task == 'help':
		print(helplist)  # could be a function, grabs dictionary helplist
	elif task == 'calculator':
		compute()
	elif task == 'catalog':
		print('Welcome to the catalog!')  # prints before calling func to prevent repeated printing within func
		catalog()
	elif task == 'file':
		print('Welcome to file access!')  # prints before calling func to prevent repeated printing within func
		accessfile()
	elif task == 'shop':  # resets changes made if shop feature was ran previously before running
		initgold()
		resetshop()
		gold = grabgold()
		shop(gold)  # could I just do shop(grabgold())?
	else:
		print('I am not sure what you are asking. For a list of actions type help in the prompt.')
	directory()
	

directory()  # the first and only func this program calls automatically upon startup
