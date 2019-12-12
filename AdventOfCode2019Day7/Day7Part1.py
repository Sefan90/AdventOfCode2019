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
	breaks = False

	while i < len(input):
		if (modeChecker(input,i) == 1):
			modeChecker(input,i,3,modeChecker(input,i,1) + modeChecker(input,i,2))
			i += 4
		
		elif (modeChecker(input,i) == 2):
			modeChecker(input,i,3,modeChecker(input,i,1) * modeChecker(input,i,2))
			i += 4
		
		elif (modeChecker(input,i) == 3):
			print(startInput)
			modeChecker(input,i,1,startInput[startInputCounter])
			startInputCounter += 1
			i += 2
		
		elif (modeChecker(input,i) == 4):
			#print(input[input[i + 1]])
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
			return [None,i,[output]]

def PhaseSender():
	output = 0
	for a in range(5,10):
		for b in range(5,10):
			for c in range(5,10):
				for d in range(5,10):
					for e in range(5,10):
						if a not in [b,c,d,e] and b not in [c,d,e] and c not in [d,e] and d not in [e]:
							breaks = False
							phases = [9,7,8,5,6] #[a,b,c,d,e]
							startInput = 0
							#inputlist = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
							inputlist = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
							#inputlist = [3,8,1001,8,10,8,105,1,0,0,21,42,55,64,85,98,179,260,341,422,99999,3,9,101,2,9,9,102,5,9,9,1001,9,2,9,1002,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,4,9,4,9,99,3,9,101,3,9,9,4,9,99,3,9,1002,9,4,9,101,3,9,9,102,5,9,9,101,4,9,9,4,9,99,3,9,1002,9,3,9,1001,9,3,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99]
							amp = [[inputlist,0,[phases[0],startInput]],[inputlist,0,[phases[1],startInput]],[inputlist,0,[phases[2],startInput]],[inputlist,0,[phases[3],startInput]],[inputlist,0,[phases[4],startInput]]]
							while True:	
								for i in range(len(phases)):
									amp[i] = IntcodeComputer(amp[i])
									if len(amp[(i+1)%5][2]) == 1:
										amp[(i+1)%5][2][0] = amp[i][2][0]
									else:
										amp[(i+1)%5][2][1] = amp[i][2][0]
									#breaks, startInput = IntcodeComputer(inputlist,[phase,startInput])
								if output < amp[4][2][0]:
									output = amp[4][2][0]
									print(output)
								if amp[i][0] == None:
									break
								#if breaks:
								#	break
	print(output)

PhaseSender();