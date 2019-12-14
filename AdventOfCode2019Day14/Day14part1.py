def Part1():
	startlist = ['9 ORE => 2 A','8 ORE => 3 B','7 ORE => 5 C','3 A, 4 B => 1 AB','5 B, 7 C => 1 BC','4 C, 1 A => 1 CA','2 AB, 3 BC, 4 CA => 1 FUEL']
	splitedlist = []
	currentitems = []
	isFuel = 0
	counter = 0
	for row in startlist:
		items = row.split(", ")
		temp = items[len(items)-1].split("=> ")
		items[len(items)-1] = temp[0]
		items.append(temp[1])
		splitedlist.append(items)
		counter += 1
		if temp[1] == "1 FUEL":
			isFuel = counter
	print(splitedlist)
	print(isFuel)
	

Part1()