import math
def FindAsteroids(cordlist,cord):
	tempList = []
	for c in cordlist:
		c[0] -= cord[0]
		c[1] -= cord[1]
	remove = []
	for c in cordlist:
		if c == [0,0]:
			continue
		elif c not in remove:
			temp = math.degrees(math.atan2(c[0],c[1]))
			remove.append([c,temp])
			for r in range(len(remove)-1):
				if remove[r][1] == temp:
					if remove[r][0] > c:
						remove[r][0] == c
					remove.pop()
	#print(remove)
	#print(cordlist)
	#print(len(cords))
	
	#return len(remove) #Return for Part1
	return remove

def Part1():
	cords = []
	mostAsteroids = 0
	bestCords = []
	best = [[0,0],0]
	#map =[".#..#",".....","#####","....#","...##"]
	#map = ["......#.#.","#..#.#....","..#######.",".#.#.###..",".#..#.....","..#....#.#","#..#....#.",".##.#..###","##...#..#.",".#....####"]
	#map = ["#.#...#.#.",".###....#.",".#....#...","##.#.#.#.#","....#.#.#.",".##..###.#","..#...##..","..##....##","......#...",".####.###."]
	#map = [".#..#..###","####.###.#","....###.#.","..###.##.#","##.##.#.#.","....###..#","..#.#..#.#","#..#.#.###",".##...##.#",".....#.#.."]
	#map = [".#..##.###...#######","##.############..##.",".#.######.########.#",".###.#######.####.#.","#####.##.#.##.###.##","..#####..#.#########","####################","#.####....###.#.#.##","##.#################","#####.##.###..####..","..######..##.#######","####.##.####...##..#",".#####..#.######.###","##...#.##########...","#.##########.#######",".####.#.###.###.#.##","....##.##.###..#####",".#.#.###########.###","#.#.#.#####.####.###","###.##.####.##.#..##"]
	map = [".#......##.#..#.......#####...#..","...#.....##......###....#.##.....","..#...#....#....#............###.",".....#......#.##......#.#..###.#.","#.#..........##.#.#...#.##.#.#.#.","..#.##.#...#.......#..##.......##","..#....#.....#..##.#..####.#.....","#.............#..#.........#.#...","........#.##..#..#..#.#.....#.#..",".........#...#..##......###.....#","##.#.###..#..#.#.....#.........#.",".#.###.##..##......#####..#..##..",".........#.......#.#......#......","..#...#...#...#.#....###.#.......","#..#.#....#...#.......#..#.#.##..","#.....##...#.###..#..#......#..##","...........#...#......#..#....#..","#.#.#......#....#..#.....##....##","..###...#.#.##..#...#.....#...#.#",".......#..##.#..#.............##.","..###........##.#................","###.#..#...#......###.#........#.",".......#....#.#.#..#..#....#..#..",".#...#..#...#......#....#.#..#...","#.#.........#.....#....#.#.#.....",".#....#......##.##....#........#.","....#..#..#...#..##.#.#......#.#.","..###.##.#.....#....#.#......#...","#.##...#............#..#.....#..#",".#....##....##...#......#........","...#...##...#.......#....##.#....",".#....#.#...#.#...##....#..##.#.#",".#.#....##.......#.....##.##.#.##"]
	for x in range(len(map)):
		for y in range(len(map[x])):
			if map[x][y] == "#":
				cords.append([x,y])
	#print(cords)
	for c in cords:
		print(c)
		cTemp = c.copy()
		ltemp = cords.copy()
		bestCords.append([cTemp,0])
		temp = FindAsteroids(ltemp,cTemp)
		bestCords[len(bestCords)-1][1]=temp
		if mostAsteroids < temp:
			mostAsteroids = temp
	for b in bestCords:
		if b[1] > best[1]:
			best = b
	for b in bestCords:
		if b[1] == best[1]:
			print(b)
	print(best)
	print(mostAsteroids)

def Part2():
	best = [0, 6] #Output from Part1
	cords = []
	degrList = []
	currentdegree = 90
	currentlength = 0
	lastdestroyed = []
	#map =[".#....#####...#..","##...##.#####..##","##...#...#.#####.","..#.....X...###..","..#.#.....#....##"]
	map = [".#......##.#..#.......#####...#..","...#.....##......###....#.##.....","..#...#....#....#............###.",".....#......#.##......#.#..###.#.","#.#..........##.#.#...#.##.#.#.#.","..#.##.#...#.......#..##.......##","..#....#.....#..##.#..####.#.....","#.............#..#.........#.#...","........#.##..#..#..#.#.....#.#..",".........#...#..##......###.....#","##.#.###..#..#.#.....#.........#.",".#.###.##..##......#####..#..##..",".........#.......#.#......#......","..#...#...#...#.#....###.#.......","#..#.#....#...#.......#..#.#.##..","#.....##...#.###..#..#......#..##","...........#...#......#..#....#..","#.#.#......#....#..#.....##....##","..###...#.#.##..#...#.....#...#.#",".......#..##.#..#.............##.","..###........##.#................","###.#..#...#......###.#........#.",".......#....#.#.#..#..#....#..#..",".#...#..#...#......#....#.#..#...","#.#.........#.....#....#.#.#.....",".#....#......##.##....#........#.","....#..#..#...#..##.#.#......#.#.","..###.##.#.....#....#.#......#...","#.##...#............#..#.....#..#",".#....##....##...#......#........","...#...##...#.......#....##.#....",".#....#.#...#.#...##....#..##.#.#",".#.#....##.......#.....##.##.#.##"]
	for x in range(len(map)):
		for y in range(len(map[x])):
			if map[x][y] == "#":
				cords.append([x,y])
	degrList = FindAsteroids(cords,best)
	degrList.sort(key = lambda x: x[1], reverse = True)
	print(degrList)
	for i in range(200):
		for x in range(len(degrList)):
			if currentdegree <= 0:
				currentdegree = 180
			#print(cordlist[x])
			if degrList[x][1] > currentdegree:
				continue
			else:
				print(str(i)+" "+str(currentdegree))
				currentdegree = degrList[x][1]
				lastdestroyed = degrList[x]
				degrList.remove(degrList[x])
				break
	print((lastdestroyed[0][0]+best[0])*100+lastdestroyed[0][1]+best[1])


	#print(degrList)
	#print(math.degrees(math.atan2(-1,0)))
	#print(math.sqrt(1**2+1**2))



Part2()