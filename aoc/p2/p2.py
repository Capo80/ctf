def solve_1():
	fd = open("input.txt", "r")
	lines = fd.read().split("\n")
	for i in range(len(lines)):
		lines[i] = lines[i].split(" ")
		lines[i][1] = lines[i][1][:-1]
	
	c = 0
	for line in lines:
		ranges = line[0].split("-")
		print(lines[1], lines[2].count(lines[1]), ranges[1], ranges[0])
		if (line[2].count(line[1]) <= int(ranges[1]) and line[2].count(line[1]) >= int(ranges[0])):
			c += 1
			print(lines[2].count(lines[1]), ranges[1], ranges[0])

	print("solution:", c)
	print(len(lines))

def solve_2():
	fd = open("input.txt", "r")
	lines = fd.read().split("\n")
	for i in range(len(lines)):
		lines[i] = lines[i].split(" ")
		lines[i][1] = lines[i][1][:-1]
	
	c = 0
	for line in lines:
		ranges = line[0].split("-")
		print(line[2], line[1], ranges[1], ranges[0])
		if ( (line[2][int(ranges[0])-1] == line[1] and line[2][int(ranges[1])-1] != line[1] ) or  (line[2][int(ranges[0])-1] != line[1] and line[2][int(ranges[1])-1] == line[1] )):
			c += 1
			print(lines[2].count(lines[1]), ranges[1], ranges[0])

	print("solution:", c)
	print(len(lines))
solve_2()

