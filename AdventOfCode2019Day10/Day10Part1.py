def FindAsteroids(map,ex,ey):
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

def Part1():
	mostAsteroids = 0
	map = [".#..##.###...#######",
"##.############..##.",
".#.######.########.#",
".###.#######.####.#.",
"#####.##.#.##.###.##",
"..#####..#.#########",
"####################",
"#.####....###.#.#.##",
"##.#################",
"#####.##.###..####..",
"..######..##.#######",
"####.##.####...##..#",
".#####..#.######.###",
"##...#.##########...",
"#.##########.#######",
".####.#.###.###.#.##",
"....##.##.###..#####",
".#.#.###########.###",
"#.#.#.#####.####.###",
"###.##.####.##.#..##"]
	for x in range(len(map)):
		for y in range(len(map[x])):
			temp = 0
			if map[x][y] == "#":
				temp = FindAsteroids(map,x,y)
			if mostAsteroids < temp:
				mostAsteroids = temp
	print(mostAsteroids)

Part1()