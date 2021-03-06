import math

def Compress(inputList):
	#print("T1: "+ str(inputList))
	tempList = []
	for i in range(len(inputList)):
		tempList.append(inputList[i])
		for x in range(len(tempList)-1):
			if inputList[i][1] == tempList[x][1]:
				tempList.pop()
				tempList[x][0] = str(int(tempList[x][0]) + int(inputList[i][0]))
				#print(tempList)
				#print(tempList[x][0])
				#print(str(int(tempList[x][0]) + int(inputList[i][0])))
				break
	#print("T2: "+ str(tempList))
	return tempList

def Part1():
	startlist = ['9 ORE => 2 A','8 ORE => 3 B','7 ORE => 5 C','3 A, 4 B => 1 AB','5 B, 7 C => 1 BC','4 C, 1 A => 1 CA','2 AB, 3 BC, 4 CA => 1 FUEL']	
	#startlist = ['157 ORE => 5 NZVS','165 ORE => 6 DCFZ','44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL','12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ','179 ORE => 7 PSHF','177 ORE => 5 HKGWZ','7 DCFZ, 7 PSHF => 2 XJWVT','165 ORE => 2 GPVTF','3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT']
	#startlist = ["2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG","17 NVRVD, 3 JNWZP => 8 VPVL","53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL","22 VJHF, 37 MNCFX => 5 FWMGM","139 ORE => 4 NVRVD","144 ORE => 7 JNWZP","5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC","5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV","145 ORE => 6 MNCFX","1 NVRVD => 8 CXFTF","1 VJHF, 6 MNCFX => 4 RFSQX","176 ORE => 6 VJHF"]
	#startlist = ['171 ORE => 8 CNZTR','7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL','114 ORE => 4 BHXH','14 VRPVC => 6 BMBT','6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL','6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT','15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW','13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW','5 BMBT => 4 WPTQ','189 ORE => 9 KTJDG','1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP','12 VRPVC, 27 CNZTR => 2 XDBXC','15 KTJDG, 12 BHXH => 5 XCVML','3 BHXH, 2 VRPVC => 7 MZWV','121 ORE => 7 VRPVC','7 XCVML => 6 RJRHP','5 BHXH, 4 VRPVC => 5 LTCX']
	#Real
	#startlist = ['13 WDSR, 16 FXQB => 6 BSTCB','185 ORE => 9 BWSCM','1 WDSR => 9 RLFSK','5 LCGL, 7 BWSCM => 9 BSVW','6 NLSL => 3 MJSQ','1 JFGM, 7 BSVW, 7 XRLN => 6 WDSR','3 WZLFV => 3 BZDPT','5 DTHZH, 12 QNTH, 20 BSTCB => 4 BMXF','18 JSJWJ, 6 JLMD, 6 TMTF, 3 XSNL, 3 BWSCM, 83 LQTJ, 29 KDGNL => 1 FUEL','1 LWPD, 28 RTML, 16 FDPM, 8 JSJWJ, 2 TNMTC, 20 DTHZH => 9 JLMD','1 SDVXW => 6 BPTV','180 ORE => 7 JFGM','13 RLFSK, 15 HRKD, 1 RFQWL => 5 QNTH','1 RFQWL, 3 NZHFV, 18 XRLN => 9 HRKD','2 NLSL, 2 JXVZ => 5 GTSJ','19 SDVXW, 2 BSVW, 19 XRLN => 6 QMFV','1 CSKP => 8 LQTJ','4 ZSZBN => 5 RBRZT','8 WZLFV, 3 QNWRZ, 1 DTHZH => 4 RTRN','1 CGXBG, 1 PGXFJ => 3 TNMTC','4 CGCSL => 7 RNFW','9 CGCSL, 1 HGTL, 3 BHJXV => 8 RSVR','5 NGJW => 8 HTDM','21 FPBTN, 1 TNMTC, 2 RBRZT, 8 BDHJ, 28 WXQX, 9 RNFW, 6 RSVR => 1 XSNL','2 WZLFV => 5 BHJXV','10 BSTCB, 4 NLSL => 4 HQLHN','1 JFGM => 7 SDVXW','6 CSKP => 8 FXQB','6 TNMTC, 4 BZDPT, 1 BPTV, 18 JSJWJ, 2 DTHZH, 1 LWPD, 8 RTML => 8 KDGNL','6 XFGWZ => 7 CGCSL','3 GTSJ => 4 LWPD','1 WDSR, 1 QNWRZ => 5 XFGWZ','11 CSKP, 10 SDVXW => 4 QNWRZ','7 BSVW, 4 QMFV => 1 RFQWL','12 QNTH, 10 HTDM, 3 WXQX => 3 FDPM','2 HGTL => 7 PGXFJ','14 SDVXW => 6 CSKP','11 HQLHN, 1 GTSJ, 1 QNTH => 5 TMTF','173 ORE => 9 LCGL','4 WXQX => 9 BDHJ','5 BZDPT => 7 NGJW','1 GTSJ, 23 QNWRZ, 6 LQTJ => 7 JSJWJ','23 NZHFV, 3 HQLHN => 6 DTHZH','2 JFGM => 4 XRLN','20 CGCSL => 9 WXQX','2 BSTCB, 3 HRKD => 9 NLSL','1 MJSQ, 1 BPTV => 8 CGXBG','1 RTRN, 1 RSVR => 3 ZSZBN','2 NZHFV, 1 BSTCB, 20 HRKD => 1 JXVZ','2 BZDPT => 5 HGTL','1 ZSZBN, 14 FDPM => 9 RTML','3 BMXF => 8 FPBTN','1 SDVXW, 8 XRLN => 9 NZHFV','18 QNWRZ, 7 RLFSK => 1 WZLFV']
	splitedlist = []
	currentitems = []
	isFuel = 0
	counter = 0
	splitedlist = [[[ i.split(" ") for i in item.split(", ")]for item in sl.split(" => ")] for sl in startlist]
	for i in range(len(splitedlist)):
		if splitedlist[i][len(splitedlist[i])-1][0][1] == "FUEL":
			isFuel = i
	fuelList = splitedlist[isFuel][len(splitedlist[isFuel])-2]
	print(fuelList)
	tempList = []
	while True:
		isBrake = False
		for element in fuelList:
			if element[1] == "ORE":
				continue
			for row in splitedlist:
				#print(element[1])
				#print(row[len(row)-1][0][1])
				if element[1] == row[len(row)-1][0][1] and row[0][0][1] != "ORE":
					if int(element[0]) <= int(row[len(row)-1][0][0]):
						tmp = [[item[i] for i in range(len(item))] for item in row[:-1]]
						fuelList.remove(element)
						fuelList.extend(tmp[0])
						fuelList = Compress(fuelList)
						isBrake = True
						break
					elif row[0][0][1] != "ORE":
						number = math.ceil(int(element[0])/int(row[len(row)-1][0][0]))
						tmp = [[[str(int(item[i][0])*number),item[i][1]]for i in range(len(item))] for item in row[:-1]]
						fuelList.remove(element)
						fuelList.extend(tmp[0])
						fuelList = Compress(fuelList)
						isBrake = True
						print(fuelList)
						break
						#print(tmp[0])
							#tempList.append([str(int(item[0][0])*number),item[0][1]])
			if isBrake == True:
				isBrake = False
				break
		#print(tempList)
		#print(tempList)
		#fuelList = tempList
		#print(fuelList)
		if all(item[1] == "ORE" for item in fuelList):
			break
		if tempList == fuelList:
			break
		tempList = fuelList
	while True:
		isBrake = False
		for element in fuelList:
			if element[1] == "ORE":
				continue
			for row in splitedlist:
				#print(element[1])
				#print(row[len(row)-1][0][1])
				if element[1] == row[len(row)-1][0][1]:
					if int(element[0]) <= int(row[len(row)-1][0][0]):
						tmp = [[item[i] for i in range(len(item))] for item in row[:-1]]
						fuelList.remove(element)
						fuelList.extend(tmp[0])
						fuelList = Compress(fuelList)
						isBrake = True
						break
					else:
						number = math.ceil(int(element[0])/int(row[len(row)-1][0][0]))
						tmp = [[[str(int(item[i][0])*number),item[i][1]]for i in range(len(item))] for item in row[:-1]]
						fuelList.remove(element)
						fuelList.extend(tmp[0])
						fuelList = Compress(fuelList)
						isBrake = True
						print(fuelList)
						break
						#print(tmp[0])
							#tempList.append([str(int(item[0][0])*number),item[0][1]])
			if isBrake == True:
				isBrake = False
				break
		#print(tempList)
		#print(tempList)
		#fuelList = tempList
		#print(fuelList)
		if all(item[1] == "ORE" for item in fuelList):
			break
	print(fuelList[0][0])

def Part11():
	startlist = ['9 ORE => 2 A','8 ORE => 3 B','7 ORE => 5 C','3 A, 4 B => 1 AB','5 B, 7 C => 1 BC','4 C, 1 A => 1 CA','2 AB, 3 BC, 4 CA => 1 FUEL']
	oreList = []
	splitedlist = [[[ i.split(" ") for i in item.split(", ")]for item in sl.split(" => ")] for sl in startlist]
	for i in range(len(splitedlist)):
		if splitedlist[i][0][0][1] == "ORE":
			oreList += [[int(splitedlist[i][0][0][0]),int(splitedlist[i][len(splitedlist[i])-1][0][0]),splitedlist[i][len(splitedlist[i])-1][0][1]]]
	while True:
		for item in splitedlist:
			for ore in oreList:
				print(oreList)
				if item[0][0][1] == ore[2]:
					for i in range(1,len(item)):
						if ore[1] >= int(item[0][0][0]):
							#print(item[0][0][0])
							oreList += [[ore[0],int(item[i][0][0]),item[i][0][1]]]
						else:
							number = math.ceil(int(item[0][0][0])/ore[1])
							oreList += [[ore[0]*number,int(item[i][0][0])*number,item[i][0][1]]]
						#print(item[i])
						#print(ore[2])
					oreList.remove(ore)
					oreList = Compress(oreList)
					break
		if all(item[1] == "FUEL" for item in oreList):
			break
	print(splitedlist)
	print(oreList)

def Part111():
	startlist = ['9 ORE => 2 A','8 ORE => 3 B','7 ORE => 5 C','3 A, 4 B => 1 AB','5 B, 7 C => 1 BC','4 C, 1 A => 1 CA','2 AB, 3 BC, 4 CA => 1 FUEL']	
	#startlist = ['157 ORE => 5 NZVS','165 ORE => 6 DCFZ','44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL','12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ','179 ORE => 7 PSHF','177 ORE => 5 HKGWZ','7 DCFZ, 7 PSHF => 2 XJWVT','165 ORE => 2 GPVTF','3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT']
	#startlist = ["2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG","17 NVRVD, 3 JNWZP => 8 VPVL","53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL","22 VJHF, 37 MNCFX => 5 FWMGM","139 ORE => 4 NVRVD","144 ORE => 7 JNWZP","5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC","5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV","145 ORE => 6 MNCFX","1 NVRVD => 8 CXFTF","1 VJHF, 6 MNCFX => 4 RFSQX","176 ORE => 6 VJHF"]
	#startlist = ['171 ORE => 8 CNZTR','7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL','114 ORE => 4 BHXH','14 VRPVC => 6 BMBT','6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL','6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT','15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW','13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW','5 BMBT => 4 WPTQ','189 ORE => 9 KTJDG','1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP','12 VRPVC, 27 CNZTR => 2 XDBXC','15 KTJDG, 12 BHXH => 5 XCVML','3 BHXH, 2 VRPVC => 7 MZWV','121 ORE => 7 VRPVC','7 XCVML => 6 RJRHP','5 BHXH, 4 VRPVC => 5 LTCX']
	#Real
	#startlist = ['13 WDSR, 16 FXQB => 6 BSTCB','185 ORE => 9 BWSCM','1 WDSR => 9 RLFSK','5 LCGL, 7 BWSCM => 9 BSVW','6 NLSL => 3 MJSQ','1 JFGM, 7 BSVW, 7 XRLN => 6 WDSR','3 WZLFV => 3 BZDPT','5 DTHZH, 12 QNTH, 20 BSTCB => 4 BMXF','18 JSJWJ, 6 JLMD, 6 TMTF, 3 XSNL, 3 BWSCM, 83 LQTJ, 29 KDGNL => 1 FUEL','1 LWPD, 28 RTML, 16 FDPM, 8 JSJWJ, 2 TNMTC, 20 DTHZH => 9 JLMD','1 SDVXW => 6 BPTV','180 ORE => 7 JFGM','13 RLFSK, 15 HRKD, 1 RFQWL => 5 QNTH','1 RFQWL, 3 NZHFV, 18 XRLN => 9 HRKD','2 NLSL, 2 JXVZ => 5 GTSJ','19 SDVXW, 2 BSVW, 19 XRLN => 6 QMFV','1 CSKP => 8 LQTJ','4 ZSZBN => 5 RBRZT','8 WZLFV, 3 QNWRZ, 1 DTHZH => 4 RTRN','1 CGXBG, 1 PGXFJ => 3 TNMTC','4 CGCSL => 7 RNFW','9 CGCSL, 1 HGTL, 3 BHJXV => 8 RSVR','5 NGJW => 8 HTDM','21 FPBTN, 1 TNMTC, 2 RBRZT, 8 BDHJ, 28 WXQX, 9 RNFW, 6 RSVR => 1 XSNL','2 WZLFV => 5 BHJXV','10 BSTCB, 4 NLSL => 4 HQLHN','1 JFGM => 7 SDVXW','6 CSKP => 8 FXQB','6 TNMTC, 4 BZDPT, 1 BPTV, 18 JSJWJ, 2 DTHZH, 1 LWPD, 8 RTML => 8 KDGNL','6 XFGWZ => 7 CGCSL','3 GTSJ => 4 LWPD','1 WDSR, 1 QNWRZ => 5 XFGWZ','11 CSKP, 10 SDVXW => 4 QNWRZ','7 BSVW, 4 QMFV => 1 RFQWL','12 QNTH, 10 HTDM, 3 WXQX => 3 FDPM','2 HGTL => 7 PGXFJ','14 SDVXW => 6 CSKP','11 HQLHN, 1 GTSJ, 1 QNTH => 5 TMTF','173 ORE => 9 LCGL','4 WXQX => 9 BDHJ','5 BZDPT => 7 NGJW','1 GTSJ, 23 QNWRZ, 6 LQTJ => 7 JSJWJ','23 NZHFV, 3 HQLHN => 6 DTHZH','2 JFGM => 4 XRLN','20 CGCSL => 9 WXQX','2 BSTCB, 3 HRKD => 9 NLSL','1 MJSQ, 1 BPTV => 8 CGXBG','1 RTRN, 1 RSVR => 3 ZSZBN','2 NZHFV, 1 BSTCB, 20 HRKD => 1 JXVZ','2 BZDPT => 5 HGTL','1 ZSZBN, 14 FDPM => 9 RTML','3 BMXF => 8 FPBTN','1 SDVXW, 8 XRLN => 9 NZHFV','18 QNWRZ, 7 RLFSK => 1 WZLFV']
	splitedlist = []
	oreList = []
	oreCheckList = []
	isFuel = 0
	isBreak = False 
	counter = 0
	splitedlist = [[[ i.split(" ") for i in item.split(", ")]for item in sl.split(" => ")] for sl in startlist]
	for i in range(len(splitedlist)):
		if splitedlist[i][len(splitedlist[i])-1][0][1] == "FUEL":
			isFuel = i
		if splitedlist[i][0][0][1] == "ORE":
			oreList += [splitedlist[i]]
			oreCheckList += splitedlist[i][1][0][1]
	fuelList = splitedlist[isFuel][len(splitedlist[isFuel])-2]
	print(fuelList)
	print(oreList)
	print(oreCheckList)
	while True:
		for item in splitedlist:
			print(item[1][0][1])
			print(oreCheckList)
			if item[1][0][1] not in oreCheckList:
				temp = [[item[1][0]]]
				print(temp)
				for i in item[0]:
					for o in range(1,len(oreList)-1):
						print(oreList)
						print(i[1])
						print(oreList[o])
						if i[1] == oreList[o][1][0][1]:
							oreCheckList += item[1][0][1]
							if i[0] <= oreList[o][1][0][0]:
								temp.insert(0,oreList[o][0])
							else:
								print(int(i[0])/int(oreList[o][1][0][0]))
								print(int(i[0]))
								print(int(oreList[o][1][0][0]))
								number = math.ceil(int(i[0])/int(oreList[o][1][0][0]))
								temp.insert(0,[[str(int(oreList[o][0][0][0])*number),oreList[o][0][0][1]]])
							print("Temp"+str(temp))
							print("A "+str(item[0]))
				if len(temp) >= len(i):
					isBreak = False
					continue
				else:
					oreList += [temp]
				print("ORE "+str(oreList))
		if len(oreList) == len(splitedlist):
			break
	for ore in oreList:
		print(ore)

def Part1111():
	startlist = ['9 ORE => 2 A','8 ORE => 3 B','7 ORE => 5 C','3 A, 4 B => 1 AB','5 B, 7 C => 1 BC','4 C, 1 A => 1 CA','2 AB, 3 BC, 4 CA => 1 FUEL']	
	#startlist = ['157 ORE => 5 NZVS','165 ORE => 6 DCFZ','44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL','12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ','179 ORE => 7 PSHF','177 ORE => 5 HKGWZ','7 DCFZ, 7 PSHF => 2 XJWVT','165 ORE => 2 GPVTF','3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT']
	#startlist = ["2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG","17 NVRVD, 3 JNWZP => 8 VPVL","53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL","22 VJHF, 37 MNCFX => 5 FWMGM","139 ORE => 4 NVRVD","144 ORE => 7 JNWZP","5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC","5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV","145 ORE => 6 MNCFX","1 NVRVD => 8 CXFTF","1 VJHF, 6 MNCFX => 4 RFSQX","176 ORE => 6 VJHF"]
	#startlist = ['171 ORE => 8 CNZTR','7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL','114 ORE => 4 BHXH','14 VRPVC => 6 BMBT','6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL','6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT','15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW','13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW','5 BMBT => 4 WPTQ','189 ORE => 9 KTJDG','1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP','12 VRPVC, 27 CNZTR => 2 XDBXC','15 KTJDG, 12 BHXH => 5 XCVML','3 BHXH, 2 VRPVC => 7 MZWV','121 ORE => 7 VRPVC','7 XCVML => 6 RJRHP','5 BHXH, 4 VRPVC => 5 LTCX']
	#Real
	#startlist = ['13 WDSR, 16 FXQB => 6 BSTCB','185 ORE => 9 BWSCM','1 WDSR => 9 RLFSK','5 LCGL, 7 BWSCM => 9 BSVW','6 NLSL => 3 MJSQ','1 JFGM, 7 BSVW, 7 XRLN => 6 WDSR','3 WZLFV => 3 BZDPT','5 DTHZH, 12 QNTH, 20 BSTCB => 4 BMXF','18 JSJWJ, 6 JLMD, 6 TMTF, 3 XSNL, 3 BWSCM, 83 LQTJ, 29 KDGNL => 1 FUEL','1 LWPD, 28 RTML, 16 FDPM, 8 JSJWJ, 2 TNMTC, 20 DTHZH => 9 JLMD','1 SDVXW => 6 BPTV','180 ORE => 7 JFGM','13 RLFSK, 15 HRKD, 1 RFQWL => 5 QNTH','1 RFQWL, 3 NZHFV, 18 XRLN => 9 HRKD','2 NLSL, 2 JXVZ => 5 GTSJ','19 SDVXW, 2 BSVW, 19 XRLN => 6 QMFV','1 CSKP => 8 LQTJ','4 ZSZBN => 5 RBRZT','8 WZLFV, 3 QNWRZ, 1 DTHZH => 4 RTRN','1 CGXBG, 1 PGXFJ => 3 TNMTC','4 CGCSL => 7 RNFW','9 CGCSL, 1 HGTL, 3 BHJXV => 8 RSVR','5 NGJW => 8 HTDM','21 FPBTN, 1 TNMTC, 2 RBRZT, 8 BDHJ, 28 WXQX, 9 RNFW, 6 RSVR => 1 XSNL','2 WZLFV => 5 BHJXV','10 BSTCB, 4 NLSL => 4 HQLHN','1 JFGM => 7 SDVXW','6 CSKP => 8 FXQB','6 TNMTC, 4 BZDPT, 1 BPTV, 18 JSJWJ, 2 DTHZH, 1 LWPD, 8 RTML => 8 KDGNL','6 XFGWZ => 7 CGCSL','3 GTSJ => 4 LWPD','1 WDSR, 1 QNWRZ => 5 XFGWZ','11 CSKP, 10 SDVXW => 4 QNWRZ','7 BSVW, 4 QMFV => 1 RFQWL','12 QNTH, 10 HTDM, 3 WXQX => 3 FDPM','2 HGTL => 7 PGXFJ','14 SDVXW => 6 CSKP','11 HQLHN, 1 GTSJ, 1 QNTH => 5 TMTF','173 ORE => 9 LCGL','4 WXQX => 9 BDHJ','5 BZDPT => 7 NGJW','1 GTSJ, 23 QNWRZ, 6 LQTJ => 7 JSJWJ','23 NZHFV, 3 HQLHN => 6 DTHZH','2 JFGM => 4 XRLN','20 CGCSL => 9 WXQX','2 BSTCB, 3 HRKD => 9 NLSL','1 MJSQ, 1 BPTV => 8 CGXBG','1 RTRN, 1 RSVR => 3 ZSZBN','2 NZHFV, 1 BSTCB, 20 HRKD => 1 JXVZ','2 BZDPT => 5 HGTL','1 ZSZBN, 14 FDPM => 9 RTML','3 BMXF => 8 FPBTN','1 SDVXW, 8 XRLN => 9 NZHFV','18 QNWRZ, 7 RLFSK => 1 WZLFV']
	splitedlist = []
	oreList = []
	oreCheckList = []
	isFuel = 0
	isBreak = False 
	counter = 0
	splitedlist = [[[ i.split(" ") for i in item.split(", ")]for item in sl.split(" => ")] for sl in startlist]
	for i in range(len(splitedlist)):
		if splitedlist[i][len(splitedlist[i])-1][0][1] == "FUEL":
			isFuel = i
		if splitedlist[i][0][0][1] == "ORE":
			oreList += [splitedlist[i]]
			oreCheckList += splitedlist[i][1][0][1]
	fuelList = splitedlist[isFuel][len(splitedlist[isFuel])-2]

	while True:
		tempList = [splitedlist[i] for i in range(len(splitedlist)) if splitedlist[i][1][0][1] not in oreCheckList]
		#print("A "+str(tempList))
		for i in range(len(tempList)):
			for j in range(len(tempList[i][0])):
				#print(tempList[i][0][j])
				for k in range(len(oreList)):
					#print(oreList)
					if tempList[i][0][j][1] == oreList[k][1][0][1]:
						tempList[i][0][j][1] = oreList[k][0][0][1]
						if tempList[i][0][j][0] <= oreList[k][1][0][0]:
							tempList[i][0][j][0] = oreList[k][0][0][0]
						else:
							number = math.ceil(int(tempList[i][0][j][0])/int(oreList[k][1][0][0]))
							tempList[i][0][j][0] = str(int(oreList[k][0][0][0])*number)
			#print(tempList)
			if len(tempList[i][0]) > 1:
				for x in reversed(range(1,len(tempList[i][0]))):
					if tempList[i][0][x][1] == tempList[i][0][x-1][1]:
						tempList[i][0][x-1][0] = str(int(tempList[i][0][x-1][0])+int(tempList[i][0][x][0]))
						del tempList[i][0][x]
		for i in range(len(tempList)):
			if tempList[i][0][0][1] == 'ORE':
				oreList += [tempList[i]]
				oreCheckList += [tempList[i][1][0][1]]

		print(oreList)
		#print(oreCheckList)
		tempList = []
		if len(oreList) == len(splitedlist):
			break
Part1111()
#342346
#2716308
#435408 För högt