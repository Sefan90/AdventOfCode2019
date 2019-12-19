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
        if len(item_list) > 1+args[0] and item_list[1+args[0]] == 2:
            return input[input[opcode+args[0]]+relative]
        elif len(item_list) > 1+args[0] and item_list[1+args[0]] == 1:
            return input[opcode+args[0]]
        else:
            return input[input[opcode+args[0]]]
    else:
        if len(item_list) > 1+args[0] and item_list[1+args[0]] == 2:
             input[input[opcode+args[0]]+relative] = args[1]
        #elif len(item_list) > 1+args[0] and item_list[1+args[0]] == 1:
        #   print("ERROR")
        #   input[opcode+args[0]] = args[1]
        else:
             input[input[opcode+args[0]]] = args[1]
        return input

def IntcodeComputer(input,next_i,startInput):
    startInputCounter = 0
    output = 0
    relative = 0
    i = next_i
    while i < len(input):
        if (modeChecker(input,relative,i) == 1):
            input = modeChecker(input,relative,i,3,modeChecker(input,relative,i,1) + modeChecker(input,relative,i,2))
            i += 4
        
        elif (modeChecker(input,relative,i) == 2):
            input = modeChecker(input,relative,i,3,modeChecker(input,relative,i,1) * modeChecker(input,relative,i,2))
            i += 4
        
        elif (modeChecker(input,relative,i) == 3):
            modeChecker(input,relative,i,1,startInput[startInputCounter])
            startInputCounter += 1
            i += 2
        
        elif (modeChecker(input,relative,i) == 4):
            output = modeChecker(input,relative,i,1)
            i += 2
            return [input,i, [output]]
        
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
                input = modeChecker(input,relative,i,3,1)
            else:
                input = modeChecker(input,relative,i,3,0)
            i += 4

        elif (modeChecker(input,relative,i) == 8):
            if modeChecker(input,relative,i,1) == modeChecker(input,relative,i,2):
                input = modeChecker(input,relative,i,3,1)
            else:
                input = modeChecker(input,relative,i,3,0)
            i += 4
        elif (modeChecker(input,relative,i) == 9):
            if input[i] == 99:
                print(99)
                return [None,i,[output]]
            relative += modeChecker(input,relative,i,1)
            i += 2

def Part1():
    gridsize = 50
    result = [[0 for x in range(gridsize)] for y in range(gridsize)]
    bigList = [0] * 10000
    inputList = [109,424,203,1,21101,11,0,0,1106,0,282,21102,1,18,0,1105,1,259,1202,1,1,221,203,1,21101,0,31,0,1105,1,282,21102,1,38,0,1106,0,259,21001,23,0,2,22102,1,1,3,21102,1,1,1,21102,57,1,0,1106,0,303,2101,0,1,222,21002,221,1,3,21001,221,0,2,21101,0,259,1,21101,80,0,0,1105,1,225,21101,158,0,2,21101,0,91,0,1106,0,303,1201,1,0,223,20102,1,222,4,21101,259,0,3,21101,225,0,2,21102,225,1,1,21101,118,0,0,1106,0,225,20102,1,222,3,21101,0,79,2,21102,1,133,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21101,148,0,0,1105,1,259,2102,1,1,223,21001,221,0,4,20102,1,222,3,21101,16,0,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,0,195,0,106,0,108,20207,1,223,2,20101,0,23,1,21102,-1,1,3,21102,214,1,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1201,-4,0,249,21202,-3,1,1,21201,-2,0,2,22101,0,-1,3,21101,250,0,0,1106,0,225,21202,1,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,21202,-2,1,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22101,0,-2,3,21102,343,1,0,1106,0,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22101,0,-4,1,21101,384,0,0,1105,1,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21202,1,1,-4,109,-5,2106,0,0]
    startInput = 0
    counter = 0
    for i in range(len(inputList)):
        bigList[i] = inputList[i]
    for x in range(gridsize):
        for y in range(gridsize):
            tmp = IntcodeComputer(bigList.copy(),0,[x,y])
            result[x][y] = tmp[2][0]
            if result[x][y] == 1:
                counter += 1
    for i in range(gridsize):
        print(result[i])
    print(counter)

def Part2():
    gridsize = 100
    result = [[0 for x in range(gridsize)] for y in range(gridsize)]
    bigList = [0] * 10000
    inputList = [109,424,203,1,21101,11,0,0,1106,0,282,21102,1,18,0,1105,1,259,1202,1,1,221,203,1,21101,0,31,0,1105,1,282,21102,1,38,0,1106,0,259,21001,23,0,2,22102,1,1,3,21102,1,1,1,21102,57,1,0,1106,0,303,2101,0,1,222,21002,221,1,3,21001,221,0,2,21101,0,259,1,21101,80,0,0,1105,1,225,21101,158,0,2,21101,0,91,0,1106,0,303,1201,1,0,223,20102,1,222,4,21101,259,0,3,21101,225,0,2,21102,225,1,1,21101,118,0,0,1106,0,225,20102,1,222,3,21101,0,79,2,21102,1,133,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21101,148,0,0,1105,1,259,2102,1,1,223,21001,221,0,4,20102,1,222,3,21101,16,0,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,0,195,0,106,0,108,20207,1,223,2,20101,0,23,1,21102,-1,1,3,21102,214,1,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1201,-4,0,249,21202,-3,1,1,21201,-2,0,2,22101,0,-1,3,21101,250,0,0,1106,0,225,21202,1,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,21202,-2,1,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22101,0,-2,3,21102,343,1,0,1106,0,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22101,0,-4,1,21101,384,0,0,1105,1,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21202,1,1,-4,109,-5,2106,0,0]
    startInput = 0
    counter = 0
    for i in range(len(inputList)):
        bigList[i] = inputList[i]
    for x in range(gridsize):
        for y in range(gridsize):
            tmp = IntcodeComputer(bigList.copy(),0,[x,y])
            result[x][y] = tmp[2][0]
            if result[x][y] == 1:
                counter += 1
    for i in range(gridsize):
        print(result[i])
    print(counter)

Part2()