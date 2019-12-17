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

Part1():
	inputList = []



Part1()