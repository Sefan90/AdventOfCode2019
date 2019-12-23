def Part1():
	cards = [i for i in range(10007)]#10007
	file = open("input.txt")
	actions = file.read().split('\n')
	#actions = ["deal with increment 7","deal into new stack","deal into new stack"]
	#actions = ["cut 6","deal with increment 7","deal into new stack"]
	#actions = ["deal with increment 7","deal with increment 9","cut -2"]
	#actions = ["deal into new stackcut -2","deal with increment 7","cut 8","cut -4","deal with increment 7","cut 3","deal with increment 9","deal with increment 3","cut -1"]
	for item in actions:
		if item.split()[1] == 'into': #deal into new stack
			cards.reverse()
		elif item.split()[0] == 'cut':
			tmpInt = int(item.split()[1])
			if tmpInt < 0:
				for _ in range(0,abs(tmpInt)):
					cards = [cards[-1]] + cards[:-1]
			else:
				for _ in range(0,tmpInt):
					cards = cards[1:] + [cards[0]]
		elif item.split()[1] == 'with': #deal with increment
			tmpInt = int(item.split()[3])
			tmpList = [0 for i in cards]
			for i in range(len(cards)):
				tmpList[i*tmpInt%len(cards)] = cards[i]
			cards = tmpList

	for i in range(len(cards)):
		if cards[i] == 2019:
			print(i)
			break

def Part2():
	card = 2020
	totalCards = 119315717514047
	shuffle = 101741582076661
	file = open("input.txt")
	actions = file.read().split('\n')

	for i in range(shuffle):
		for item in actions:
			if item.split()[1] == 'into': #deal into new stack
				card = totalCards - card
			elif item.split()[0] == 'cut':
				card -= int(item.split()[1])
			elif item.split()[1] == 'with': #deal with increment
				card = card*int(item.split()[3])%totalCards
		#print(card)
	print(card)

Part2()
#7123 to big
#3309 to low