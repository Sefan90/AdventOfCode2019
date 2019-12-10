def GetReverseIntArray(number):
	result = []
	while number:
		result.append(number % 10)
		number //= 10
	if result == []:
		result = [0]
	return result

def IntcodeComputer(input,startInput):
	startInputCounter = 0
	output = 0
	breaks = False
	i = 0
	while i < len(input):
		PosModeA = False
		PosModeB = False
		PosModeC = False
		input1 = 0
		input2 = 0

		if i+2 < len(input): #För att inte få out of range på input
			#print(" I:"+str(i)+" OP:"+str(input[i])+" In1:"+str(input[input[i + 1]])+" In2:"+str(input[i + 2])+" In3:"+str(input[i + 3]))
			input2 = input[i + 2]
		if i+1 < len(input):
			input1 = input[i + 1]
			
		item_list = GetReverseIntArray(input[i])
		if (len(item_list) > 1):
			if (len(item_list) == 2 and item_list[1] == 9 and item_list[0] == 9):
				breaks = True
				break

			#if (len(item_list) >= 2 and item_list[1] != 0):
			#	breaks = True
			#	print(item_list)
		#	break
			
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
			#print(input[input[i + 1]])
			output = input[input[i + 1]]
			startInput.append(input[input[i + 1]])
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
			breaks = True
			break
	return breaks, output
	#print(input[0])

def PhaseSender():
	output = 0
	for a in range(5,10):
		for b in range(5,10):
			for c in range(5,10):
				for d in range(5,10):
					for e in range(5,10):
						if a not in [b,c,d,e] and b not in [c,d,e] and c not in [d,e] and d not in [e]:
							breaks = False
							phases = [a,b,c,d,e]
							startInput = 0
							inputlist = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
							#inputlist = [3,8,1001,8,10,8,105,1,0,0,21,42,55,64,85,98,179,260,341,422,99999,3,9,101,2,9,9,102,5,9,9,1001,9,2,9,1002,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,4,9,4,9,99,3,9,101,3,9,9,4,9,99,3,9,1002,9,4,9,101,3,9,9,102,5,9,9,101,4,9,9,4,9,99,3,9,1002,9,3,9,1001,9,3,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99]
							while True:	
								for phase in phases:
									breaks = False
									print(phase)
									breaks, startInput = IntcodeComputer(inputlist,[phase,startInput])
									if breaks:
										break
								if output < startInput:
									output = startInput
									print(output)
								if breaks:
									break
	print(output)

PhaseSender();