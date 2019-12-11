def GetReverseIntArray(number):
	result = []
	while number:
		result.append(number % 10)
		number //= 10
	return result

def modeChecker(input,relative,opcode,*args):
	item_list = GetReverseIntArray(input[opcode])
	if len(args) == 0:
		return item_list[0]
	if len(args) == 1:
		if len(item_list) > 1+args[0]+relative and item_list[1+args[0]] == 2:
			input[input[opcode+args[0]+relative]]
		elif len(item_list) > 1+args[0] and item_list[1+args[0]] == 1:
			return input[opcode+args[0]]
		return input[input[opcode+args[0]]]		
	else:
		if len(item_list) > 1+args[0]+relative and item_list[1+args[0]] == 2:
			input[input[opcode+args[0]+relative]] = args[1]
		if len(item_list) > 1+args[0] and item_list[1+args[0]] == 1:
			input[opcode+args[0]] = args[1]
		else:
			input[input[opcode+args[0]]] = args[1]	

def IntcodeComputer(input,startInput):
	startInputCounter = 0
	output = 0
	breaks = False
	relative = 0
	i = 0
	while i < len(input):
		if (modeChecker(input,relative,i) == 1):
			modeChecker(input,relative,i,3,modeChecker(input,relative,i,1) + modeChecker(input,relative,i,2))
			i += 4
		
		elif (modeChecker(input,relative,i) == 2):
			modeChecker(input,relative,i,3,modeChecker(input,relative,i,1) * modeChecker(input,relative,i,2))
			i += 4
		
		elif (modeChecker(input,relative,i) == 3):
			modeChecker(input,relative,i,1,startInput[startInputCounter])
			startInputCounter += 1
			i += 2
		
		elif (modeChecker(input,relative,i) == 4):
			print(input[input[i + 1]])
			output = modeChecker(input,relative,i,1)
			startInput.append(modeChecker(input,relative,i,1))
			i += 2
		
		elif (modeChecker(input,relative,i) == 5):
			if modeChecker(input,relative,i,1) != 0:
				i = modeChecker(input,relative,i,2)
			else:
				i += 3

		elif (modeChecker(input,relative,i) == 6):
			if modeChecker(input,relative,i,1) == 0:
				i = modeChecker(input,relative,i,2)
			else:
				i += 3

		elif (modeChecker(input,relative,i) == 7):
			if modeChecker(input,relative,i,1) < modeChecker(input,relative,i,2):
				modeChecker(input,relative,i,3,1)
			else:
				modeChecker(input,relative,i,3,0)
			i += 4

		elif (modeChecker(input,relative,i) == 8):
			if modeChecker(input,relative,i,1) == modeChecker(input,relative,i,2):
				modeChecker(input,relative,i,3,1)
			else:
				modeChecker(input,relative,i,3,0)
			i += 4
		elif (modeChecker(input,relative,i) == 9):
			relative = modeChecker(input,relative,i,1)
			i += 2
		else:
			break;
	#return breaks, output

def Part1():
	inputList = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
	startInput = 1
	IntcodeComputer(inputList,[startInput])

Part1();