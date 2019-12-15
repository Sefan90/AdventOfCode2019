import math

def Part1():	
	startlist = ['157 ORE => 5 NZVS','165 ORE => 6 DCFZ','44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL','12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ','179 ORE => 7 PSHF','177 ORE => 5 HKGWZ','7 DCFZ, 7 PSHF => 2 XJWVT','165 ORE => 2 GPVTF','3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT']
	splitedlist = []
	currentitems = []
	isFuel = 0
	counter = 0
	for row in startlist:
		items = row.split(", ")
		temp = items[len(items)-1].split("=> ")
		items[len(items)-1] = temp[0]
		items.insert(0,temp[1])
		splitedlist.append(items)
		counter += 1
		if temp[1] == "1 FUEL":
			isFuel = counter
	fuelList = splitedlist[isFuel-1][1:]
	print(fuelList)
	tempList = []
	while True:
		for element in fuelList:
			for row in splitedlist:
				splitElement = element.split(" ")
				#print(row[1].split(" ")[0])
				if splitElement[1] == row[1].split(" ")[1]:
					if splitElement[0] <= row[1].split(" ")[0]:
						for item in row[1:]:
							tempList.append(item)
					else:
						number = math.ceil(int(splitElement[0])/int(row[1].split(" ")[0]))
						for item in row[1:]:
							splitItem = item.split(" ")
							tempList.append(str(int(splitItem[0])*number)+" "+splitItem[1])
		fuelList = tempList
		print(fuelList)
		if fuelList[0][-3:] == "ORE":
			break
	prin(fuelList)
	



	print(splitedlist)
	print(isFuel)
	

Part1()