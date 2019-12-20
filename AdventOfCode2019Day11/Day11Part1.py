def GetReverseIntArray(number):
	result = []
	while number:
		result.append(number % 10)
		number //= 10
	if result == []:
		result = [0]
	return result

def modeChecker(input,opcode,*args):
	item_list = GetReverseIntArray(input[opcode])
	if len(args) == 0:
		return item_list[0]
	if len(args) == 1:
		if len(item_list) > 1+args[0] and item_list[1+args[0]] == 1:
			return input[opcode+args[0]]
		return input[input[opcode+args[0]]]		
	else:
		if len(item_list) > 1+args[0] and item_list[1+args[0]] == 1:
			input[opcode+args[0]] = args[1]
		else:
			input[input[opcode+args[0]]] = args[1]	

def IntcodeComputer(amp):
	input = amp[0]
	i = amp[1]
	startInput =amp[2]
	startInputCounter = 0
	output = 0

	while i < len(input):
		if (modeChecker(input,i) == 1):
			modeChecker(input,i,3,modeChecker(input,i,1) + modeChecker(input,i,2))
			i += 4
		
		elif (modeChecker(input,i) == 2):
			modeChecker(input,i,3,modeChecker(input,i,1) * modeChecker(input,i,2))
			i += 4
		
		elif (modeChecker(input,i) == 3):
			modeChecker(input,i,1,startInput[startInputCounter])
			startInputCounter += 1
			i += 2
		
		elif (modeChecker(input,i) == 4):
			output = modeChecker(input,i,1)
			startInput.append(modeChecker(input,i,1))
			i += 2
			return [input,i,[output]]
		
		elif (modeChecker(input,i) == 5):
			if modeChecker(input,i,1) != 0:
				i = modeChecker(input,i,2)
			else:
				i += 3

		elif (modeChecker(input,i) == 6):
			if modeChecker(input,i,1) == 0:
				i = modeChecker(input,i,2)
			else:
				i += 3

		elif (modeChecker(input,i) == 7):
			if modeChecker(input,i,1) < modeChecker(input,i,2):
				modeChecker(input,i,3,1)
			else:
				modeChecker(input,i,3,0)
			i += 4

		elif (modeChecker(input,i) == 8):
			if modeChecker(input,i,1) == modeChecker(input,i,2):
				modeChecker(input,i,3,1)
			else:
				modeChecker(input,i,3,0)
			i += 4
		else:
			print("break "+str(input[i]))
			return [None,i,[output]]

def Part1():
	paintList ={}
	for x in range(100):
		for y in range(100):
			paintList[str(x)+","+str(y)] = 0
	lastXY = "0,0"
	distinctPaintList = [[0,0]]
	direction = 0
	startInput = [0] 
	#Input: Provide 0 if the robot is over a black panel or 1 if the robot is over a white panel.
	#Output: First, it will output a value indicating the color to paint the panel the robot is over: 0 means to paint the panel black, and 1 means to paint the panel white.
	#Output: Second, it will output a value indicating the direction the robot should turn: 0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.
	inputList = [0] * 10000
	inputList2 = [3,8,1005,8,336,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,28,1006,0,36,1,2,5,10,1006,0,57,1006,0,68,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,63,2,6,20,10,1,106,7,10,2,9,0,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,97,1006,0,71,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,122,2,105,20,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,148,2,1101,12,10,1006,0,65,2,1001,19,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,181,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,204,2,7,14,10,2,1005,20,10,1006,0,19,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,236,1006,0,76,1006,0,28,1,1003,10,10,1006,0,72,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,271,1006,0,70,2,107,20,10,1006,0,81,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,303,2,3,11,10,2,9,1,10,2,1107,1,10,101,1,9,9,1007,9,913,10,1005,10,15,99,109,658,104,0,104,1,21101,0,387508441896,1,21102,1,353,0,1106,0,457,21101,0,937151013780,1,21101,0,364,0,1105,1,457,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,179490040923,1,1,21102,411,1,0,1105,1,457,21101,46211964123,0,1,21102,422,1,0,1106,0,457,3,10,104,0,104,0,3,10,104,0,104,0,21101,838324716308,0,1,21101,0,445,0,1106,0,457,21102,1,868410610452,1,21102,1,456,0,1106,0,457,99,109,2,22101,0,-1,1,21101,40,0,2,21101,0,488,3,21101,478,0,0,1106,0,521,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,483,484,499,4,0,1001,483,1,483,108,4,483,10,1006,10,515,1101,0,0,483,109,-2,2105,1,0,0,109,4,2101,0,-1,520,1207,-3,0,10,1006,10,538,21101,0,0,-3,22102,1,-3,1,21202,-2,1,2,21101,0,1,3,21101,557,0,0,1105,1,562,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,585,2207,-4,-2,10,1006,10,585,22101,0,-4,-4,1106,0,653,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,604,1,0,1106,0,562,21202,1,1,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,623,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,645,21202,-1,1,1,21101,0,645,0,106,0,520,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]
	for i in range(len(inputList2)):
		inputList[i] = inputList2[i]
	inputCommand = [inputList,0,startInput]
	while True:
		paint = IntcodeComputer(inputCommand)
		if paint[0] == None:
			break
		paintList[lastXY] = paint[2][0]
		inputCommand = paint
		rotation = IntcodeComputer(inputCommand)
		if rotation[0] == None:
			break
		if rotation[2][0] == 0:
			direction += 1
		else:
			direction -= 1
			if direction == -1:
				direction = 3
		if direction == 0:
			lastXY = str(int(lastXY.split(",")[0])+1)+","+lastXY.split(",")[1]
			paintList[lastXY] = paint[2][0]
		elif direction == 1:
			lastXY = lastXY.split(",")[0]+","+str(int(lastXY.split(",")[1])-1)
			paintList[lastXY] = paint[2][0]
		elif direction == 2:
			lastXY = str(int(lastXY.split(",")[0])-1)+","+lastXY.split(",")[1]
			paintList[lastXY] = paint[2][0]
		elif direction == 3:
			lastXY = lastXY.split(",")[0]+","+str(int(lastXY.split(",")[1])+1)
			paintList[lastXY] = paint[2][0]
		if [int(lastXY.split(",")[0]),int(lastXY.split(",")[1])] not in distinctPaintList:
			distinctPaintList.append([int(lastXY.split(",")[0]),int(lastXY.split(",")[1])])
		inputCommand[0] = rotation[0]
		inputCommand[1] = rotation[1]
		inputCommand[2] = [paintList[lastXY]]
	print(len(paintList))
	print(len(distinctPaintList))
	#print(paintList[len(paintList)-1][1]+1)
	#paintList.append(paintList[len(paintList)-1][1]+1)
	#print(paintList[len(paintList)-1])

Part1()
