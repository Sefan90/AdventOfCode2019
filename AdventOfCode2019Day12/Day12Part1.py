'''
<x=-4, y=-14, z=8>
<x=1, y=-8, z=10>
<x=-15, y=2, z=1>
<x=-17, y=-17, z=16>
'''
def Part2():
	moons = [[-4,-14,8],[1,-8,10],[-15, 2, 1],[-17, -17, 16]]
	vel = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
	moonsMatch = [[-4,-14,8],[1,-8,10],[-15, 2, 1],[-17, -17, 16]]
	velMatch = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
	steps = 0
	while True:
		for x in range(len(moons)):
			for y in range(len(moons[0])):
				for moon in moons:
					if moons[x][y] < moon[y]:
						vel[x][y] += 1
					elif moons[x][y] > moon[y]:
						vel[x][y] -= 1
		moons = [[x+y for x,y in zip(m,v)] for m,v in zip(moons,vel)]
		steps += 1
		if moons == moonsMatch: #and vel == velMatch:
			print(steps)
			break

def Part1():
	output = 0
	moons = [[-4,-14,8],[1,-8,10],[-15, 2, 1],[-17, -17, 16]]
	vel = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
	steps = 1000
	for step in range(steps):
		for x in range(len(moons)):
			for y in range(len(moons[0])):
				for moon in moons:
					print(str(moons[x][y])+" "+str(moon[y]))
					if moons[x][y] < moon[y]:
						vel[x][y] += 1
					elif moons[x][y] > moon[y]:
						vel[x][y] -= 1
		for x in range(len(moons)):
			for y in range(len(moon)):	
				moons[x][y] += vel[x][y]
		print(moons)
		print(vel)
		if step >= steps-1:
			for i in range(len(moons)):
				output += (abs(moons[i][0])+abs(moons[i][1])+abs(moons[i][2]))*(abs(vel[i][0])+abs(vel[i][1])+abs(vel[i][2]))
			print(output)


Part2()
