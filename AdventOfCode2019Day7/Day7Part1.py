def GetReverseIntArray(number):
	result = []
	while number:
		result.append(number % 10)
		number //= 10
	if result == []:
		result = [0]
	return result

def IntcodeComputer(input,startInput):
	skipUntil = 0
	output = 0
	for i, item in enumerate(input):
		if i < skipUntil:
			continue
		PosModeA = False
		PosModeB = False
		PosModeC = False
		input1 = 0
		input2 = 0

		if i+2 < len(input): #För att inte få out of range på input
			#print("I:"+str(i)+" OP:"+str(item)+" In1:"+str(input[i + 1])+" In2:"+str(input[i + 2])+" In3:"+str(input[i + 3]))
			input2 = input[i + 2]
		if i+1 < len(input):
			input1 = input[i + 1]
			
		item_list = GetReverseIntArray(item)
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
		#print(item_list)
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
			skipUntil += 4
		
		elif (item_list[0] == 2):
			if (PosModeA == False):
				input[input[i + 3]] = input1 * input2
			else:
				input[i + 3] = input1 * input2
			skipUntil += 4
		
		elif (item_list[0] == 3):
			input[input[i + 1]] = startInput
			skipUntil += 2
		
		elif (item_list[0] == 4):
			print(input[input[i + 1]])
			output = input[input[i + 1]]
			skipUntil += 2
		
		elif (item_list[0] == 5):
			if input1 != 0:
				skipUntil = input2
			else:
				skipUntil += 3

		elif (item_list[0] == 6):
			if input1 == 0:
				skipUntil = input2
			else:
				skipUntil += 3

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
			skipUntil += 4

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
			skipUntil += 4

		else:
			break;
	return output
	#print(input[0])

def PhaseSender():
	startInput = 0
	phases = [4,3,2,1,0]
	inputlist = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

	for phase in phases:
		templist = inputlist.copy()
		templist[0] = phase
		startInput = IntcodeComputer(templist,startInput)

PhaseSender();