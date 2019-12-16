def FindAsteroids(cordlist,cord):

	for c in cordlist:
		c[0] -= cord[0]
		c[1] -= cord[1]
	remove = []
	for c in cordlist:
		for cc in cordlist:
			if (c == [0,0] and c not in remove):
				remove.append(c)
			for i in range(1,30):
				if (c[0] == cc[0]*i and c[1] == cc[1]*i and c not in remove and c != cc):
					remove.append(c)

	for r in remove:
		cordlist.remove(r)
	#print(cordlist)
	#print(len(cords))
	return len(cordlist)

def Part1():
	cords = []
	mostAsteroids = 0
	bestCords = []
	#map = ["......#.#.","#..#.#....","..#######.",".#.#.###..",".#..#.....","..#....#.#","#..#....#.",".##.#..###","##...#..#.",".#....####"]
	#map = ["#.#...#.#.",".###....#.",".#....#...","##.#.#.#.#","....#.#.#.",".##..###.#","..#...##..","..##....##","......#...",".####.###."]
	map = [".#..#..###","####.###.#","....###.#.","..###.##.#","##.##.#.#.","....###..#","..#.#..#.#","#..#.#.###",".##...##.#",".....#.#.."]
	#map = [".#......##.#..#.......#####...#..","...#.....##......###....#.##.....","..#...#....#....#............###.",".....#......#.##......#.#..###.#.","#.#..........##.#.#...#.##.#.#.#.","..#.##.#...#.......#..##.......##","..#....#.....#..##.#..####.#.....","#.............#..#.........#.#...","........#.##..#..#..#.#.....#.#..",".........#...#..##......###.....#","##.#.###..#..#.#.....#.........#.",".#.###.##..##......#####..#..##..",".........#.......#.#......#......","..#...#...#...#.#....###.#.......","#..#.#....#...#.......#..#.#.##..","#.....##...#.###..#..#......#..##","...........#...#......#..#....#..","#.#.#......#....#..#.....##....##","..###...#.#.##..#...#.....#...#.#",".......#..##.#..#.............##.","..###........##.#................","###.#..#...#......###.#........#.",".......#....#.#.#..#..#....#..#..",".#...#..#...#......#....#.#..#...","#.#.........#.....#....#.#.#.....",".#....#......##.##....#........#.","....#..#..#...#..##.#.#......#.#.","..###.##.#.....#....#.#......#...","#.##...#............#..#.....#..#",".#....##....##...#......#........","...#...##...#.......#....##.#....",".#....#.#...#.#...##....#..##.#.#",".#.#....##.......#.....##.##.#.##"]
	for x in range(len(map)):
		for y in range(len(map[x])):
			if map[x][y] == "#":
				cords.append([x,y])

	for c in cords:
		print(c)
		cTemp = c.copy()
		temp = FindAsteroids(cords,c)
		if mostAsteroids < temp:
			mostAsteroids = temp
			bestCords = cTemp

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