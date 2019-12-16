def GetIntArray(number):
	result = []
	while number:
		result.insert(0,number % 10)
		number //= 10
	if result == []:
		result = [0]
	return result

def Part1():
	inputList = 59791871295565763701016897619826042828489762561088671462844257824181773959378451545496856546977738269316476252007337723213764111739273853838263490797537518598068506295920453784323102711076199873965167380615581655722603274071905196479183784242751952907811639233611953974790911995969892452680719302157414006993581489851373437232026983879051072177169134936382717591977532100847960279215345839529957631823999672462823375150436036034669895698554251454360619461187935247975515899240563842707592332912229870540467459067349550810656761293464130493621641378182308112022182608407992098591711589507803865093164025433086372658152474941776320203179747991102193608
	splitedList = GetIntArray(inputList)
	#print(splitedList)
	for x in range(100):
		newList= []
		basePattern = [0,1,0,-1]
		bigPattern = [1,0,-1,0]
		for i in range(1,len(splitedList)+1):
			if i > 1:
				for b in range(len(basePattern)):
					#print("t"+str(i*b))
					bigPattern.insert(i*b,basePattern[b])
			#print(bigPattern)
			output = 0
			bp = 0
			for item in splitedList:
				output += item*bigPattern[bp]
				#print(output)
				bp += 1
				bp = bp%len(bigPattern)
			if abs(output) < 10:
				newList.append(abs(output))
			else:
				outputList = GetIntArray(output)
				outputTemp = outputList[len(outputList)-1]
				newList.append(abs(outputTemp))
		splitedList = newList
	print(splitedList)
	print(str(splitedList[0])+str(splitedList[1])+str(splitedList[2])+str(splitedList[3])+str(splitedList[4])+str(splitedList[5])+str(splitedList[6])+str(splitedList[7]))

Part1()