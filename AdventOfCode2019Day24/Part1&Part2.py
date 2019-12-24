def Part1():
	#bugmap = ["....#","#..#.","#..##","..#..","#...."]	#test done
	bugmap = ["#####",".#.##","#...#","..###","#.##."]
	bigbugmap = [[".",".",".",".",".",".","."]]
	for i in bugmap:
		bigbugmap.append(list("."+i+"."))
	bigbugmap.append([".",".",".",".",".",".","."])
	bugmaphistory = []
	bugmaphistory.append(bigbugmap)

	while True:
		tempmap = [['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']]
		for x in range(1,len(bigbugmap)-1):
			for y in range(1,len(bigbugmap[x])-1):
				counter = 0
				if bigbugmap[x-1][y] == "#":
					counter += 1
				if bigbugmap[x][y-1] == "#":
					counter += 1
				if bigbugmap[x+1][y] == "#":
					counter += 1
				if bigbugmap[x][y+1] == "#":
					counter += 1
				if bigbugmap[x][y] == "#":
					if counter == 1:
						tempmap[x][y] = "#"
					continue
				else:
					if counter in [1,2]:
						tempmap[x][y] = "#"
					continue
		bigbugmap = tempmap
		if bigbugmap in bugmaphistory:
			break
		bugmaphistory.append(bigbugmap)
	biodiversityRating = 0
	for x in range(1,len(bigbugmap)-1):
		for y in range(1,len(bigbugmap[x])-1):
			if bigbugmap[x][y] == "#":
				biodiversityRating += 2**((x-1)*5+(y-1))
	print(biodiversityRating)


Part1()

#264
