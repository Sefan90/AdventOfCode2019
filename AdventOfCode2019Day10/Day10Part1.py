import math
def FindAsteroids(cordlist,cord):

	for c in cordlist:
		c[0] -= cord[0]
		c[1] -= cord[1]
	remove = []
	for c in cordlist:
		for cc in cordlist:
			if c == [0,0] and c not in remove:
				remove.append(c)
				print("1 "+str(c)+" "+str(cc))
				break
			elif c != cc and c != [0,0] and cc != [0,0] and c[0] == 0 and cc[0] == 0 and ((c[1] > 0 and cc[1] > 0 and c[1] > cc[1]) or (c[1] < 0 and cc[1] < 0 and c[1] < cc[1])) not in remove and c != cc:
				remove.append(c)
				print("2 "+str(c)+" "+str(cc))
				break
			elif c != cc and c != [0,0]and cc != [0,0] and c[1] == 0 and cc[1] == 0 and ((c[0] > 0 and cc[0] > 0 and c[0] > cc[0]) or (c[0] < 0 and cc[0] < 0 and c[0] < cc[0])) not in remove and c != cc:
				remove.append(c)
				print("3 "+str(c)+" "+str(cc))
				break
			elif c[0] > 1 and cc[0] > 1 and c[1] > 1 and cc[1] > 1 and c[0]/cc[0] == c[0]//cc[0] and c[1]/cc[1] == c[1]//cc[1] and c[0]//cc[0] == c[1]//cc[1] and c not in remove and c != cc:
				remove.append(c)
				print("4 "+str(c)+" "+str(cc))
				print(str(c[1]/cc[1])+" "+str(c[1]//cc[1]))
				break
			elif c[0] < -1 and cc[0] > 1 and c[1] < -1 and cc[1] > 1 and c[0]/cc[0] == c[0]//cc[0] and c[1]/cc[1] == c[1]//cc[1] and c[0]//cc[0] == c[1]//cc[1] and c not in remove and c != cc:
				remove.append(c)
				print("5 "+str(c)+" "+str(cc))
				print(str(c[1]/cc[1])+" "+str(c[1]//cc[1]))
				break
			elif c[0] < -1 and cc[0] < -1 and c[1] < -1 and cc[1] < -1 and c[0]/cc[0] == c[0]//cc[0] and c[1]/cc[1] == c[1]//cc[1] and c[0]//cc[0] == c[1]//cc[1] and c not in remove and c != cc:
				remove.append(c)
				print("6 "+str(c)+" "+str(cc))
				print(str(c[1]/cc[1])+" "+str(c[1]//cc[1]))
				break
			elif c[0] > 1 and cc[0] < -1 and c[1] > 1 and cc[1] < -1 and c[0]/cc[0] == c[0]//cc[0] and c[1]/cc[1] == c[1]//cc[1] and c[0]//cc[0] == c[1]//cc[1] and c not in remove and c != cc:
				remove.append(c)
				print("7 "+str(c)+" "+str(cc))
				print(str(c[1]/cc[1])+" "+str(c[1]//cc[1]))
				break
				#for i in range(1,30):
				#if c[0] == cc[0]*i and c[1] == cc[1]*i and c not in remove and c != cc:
				#remove.append(c)
				#break
	print(remove)
	for r in remove:
		cordlist.remove(r)
	print(cordlist)
	#print(len(cords))
	return len(cordlist)

def Part1():
	cords = []
	mostAsteroids = 0
	bestCords = []
	map =[".#..#",".....","#####","....#","...##"]
	#map = ["......#.#.","#..#.#....","..#######.",".#.#.###..",".#..#.....","..#....#.#","#..#....#.",".##.#..###","##...#..#.",".#....####"]
	#map = ["#.#...#.#.",".###....#.",".#....#...","##.#.#.#.#","....#.#.#.",".##..###.#","..#...##..","..##....##","......#...",".####.###."]
	#map = [".#..#..###","####.###.#","....###.#.","..###.##.#","##.##.#.#.","....###..#","..#.#..#.#","#..#.#.###",".##...##.#",".....#.#.."]
	#map = [".#......##.#..#.......#####...#..","...#.....##......###....#.##.....","..#...#....#....#............###.",".....#......#.##......#.#..###.#.","#.#..........##.#.#...#.##.#.#.#.","..#.##.#...#.......#..##.......##","..#....#.....#..##.#..####.#.....","#.............#..#.........#.#...","........#.##..#..#..#.#.....#.#..",".........#...#..##......###.....#","##.#.###..#..#.#.....#.........#.",".#.###.##..##......#####..#..##..",".........#.......#.#......#......","..#...#...#...#.#....###.#.......","#..#.#....#...#.......#..#.#.##..","#.....##...#.###..#..#......#..##","...........#...#......#..#....#..","#.#.#......#....#..#.....##....##","..###...#.#.##..#...#.....#...#.#",".......#..##.#..#.............##.","..###........##.#................","###.#..#...#......###.#........#.",".......#....#.#.#..#..#....#..#..",".#...#..#...#......#....#.#..#...","#.#.........#.....#....#.#.#.....",".#....#......##.##....#........#.","....#..#..#...#..##.#.#......#.#.","..###.##.#.....#....#.#......#...","#.##...#............#..#.....#..#",".#....##....##...#......#........","...#...##...#.......#....##.#....",".#....#.#...#.#...##....#..##.#.#",".#.#....##.......#.....##.##.#.##"]
	for x in range(len(map)):
		for y in range(len(map[x])):
			if map[x][y] == "#":
				cords.append([x,y])
	print(cords)
	for c in cords:
		print(c)
		cTemp = c.copy()
		ltemp = cords.copy()
		bestCords.append([cTemp,0])
		temp = FindAsteroids(ltemp,cTemp)
		bestCords[len(bestCords)-1][1]=temp
		if mostAsteroids < temp:
			mostAsteroids = temp

	print(mostAsteroids)
	print(bestCords)

Part1()

''' OLD
def FindAsteroids1(map,ex,ey):
	counter = 0
	cords = []
	remove = []
	for x in range(-ex, len(map)-ex):
		for y in range(-ey,len(map[ex])-ey):
			if map[x+ex][y+ey] == "#":
				counter += 1
				cords.append([x,y])
	#print(cords)
	for c in cords:
		for cc in cords:
			if (c == [0,0] and c not in remove):
				remove.append(c)
			for i in range(2,30):
				if (c[0] == cc[0]*i and c[1] == cc[1]*i and c not in remove and c != cc):
					remove.append(c)

	for r in remove:
		cords.remove(r)
	#print(cords)
	#print(len(cords))
	return len(cords)

def Part11():
	mostAsteroids = 0
	map = [".#..#..###",
"####.###.#",
"....###.#.",
"..###.##.#",
"##.##.#.#.",
"....###..#",
"..#.#..#.#",
"#..#.#.###",
".##...##.#",
".....#.#.."]
	for x in range(len(map)):
		for y in range(len(map[x])):
			temp = 0
			if map[x][y] == "#":
				temp = FindAsteroids1(map,x,y)
			if mostAsteroids < temp:
				mostAsteroids = temp
	print(mostAsteroids)
'''