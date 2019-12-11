def GetReverseIntArray(number):
	result = []
	while number:
		result.append(number % 10)
		number //= 10
	return result

def modeChecker(input,opcode,parameter):
	item_list = GetReverseIntArray(input[opcode])
	if parameter == 0:
		return item_list[0]
	elif item_list[1+parameter] == 0:
		return input[input[opcode+parameter]]
	elif item_list[1+parameter] == 1:
		return input[opcode+parameter]

def IntcodeComputer(input,startInput):
	startInputCounter = 0
	output = 0
	i = 0
	while i < len(input):
		PosModeA = False
		PosModeB = False
		PosModeC = False
		input1 = 0
		input2 = 0

		if i+2 < len(input): #För att inte få out of range på input
			print("I:"+str(i)+" OP:"+str(input[i])+" In1:"+str(input[i + 1])+" In2:"+str(input[i + 2])+" In3:"+str(input[i + 3]))
			input2 = input[i + 2]
		if i+1 < len(input):
			input1 = input[i + 1]
			
		item_list = GetReverseIntArray(input[i])
		#print(i)
		#print(item_list)
		if (len(item_list) > 1):
			if (len(item_list) >= 2 and item_list[1] != 0):
				break
			
			if(len(item_list) >= 3 and item_list[2] == 1):
				PosModeC = True
			
			if (len(item_list) >= 4 and item_list[3] == 1):
				PosModeB = True
			
			if (len(item_list) >= 5 and item_list[4] == 1):
				PosModeA = True

		if (PosModeB == False and item_list[0] != 3 and item_list[0] != 4):
			input2 = input[input2]
		if (PosModeC == False and item_list[0] != 3 and item_list[0] != 4):
			input1 = input[input1]
		#print(input1)
		#print(input2)

		if (item_list[0] == 1):
			if (PosModeA == False):
				input[input[i + 3]] = input1 + input2
			else:
				input[i + 3] = input1 + input2
			i += 4
		
		elif (item_list[0] == 2):
			if (PosModeA == False):
				input[input[i + 3]] = input1 * input2
			else:
				input[i + 3] = input1 * input2
			i += 4
		
		elif (item_list[0] == 3):
			input[input[i + 1]] = startInput[startInputCounter]
			startInputCounter += 1
			i += 2
		
		elif (item_list[0] == 4):
			print(input[input[i + 1]])
			output.append(input[input[i + 1]])
			i += 2
		
		elif (item_list[0] == 5):
			if input1 != 0:
				i = input2
			else:
				i += 3

		elif (item_list[0] == 6):
			if input1 == 0:
				i = input2
			else:
				i += 3

		elif (item_list[0] == 7):
			if input1 < input2:
				if (PosModeA == False):
					input[input[i+3]] = 1
				else:
					input[i+3] = 1
			else:
				if (PosModeA == False):
					input[input[i+3]] = 0
				else:
					input[i+3] = 0
			i += 4

		elif (item_list[0] == 8):
			if input1 == input2:
				if (PosModeA == False):
					input[input[i+3]] = 1
				else:
					input[i+3] = 1
			else:
				if (PosModeA == False):
					input[input[i+3]] = 0
				else:
					input[i+3] = 0
			i += 4

		else:
			break;
	#print(input[0])

def Part1():
	inputList = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
	startInput = 1
	IntcodeComputer(inputList,startInput)

Part1();