import sys

lines=[]
for line in open(sys.argv[1]):
	lines.append(line.strip().split(","))

line_pos=[]

for line in lines:
	x=0;y=0
	line_pos.append(set([]))
	for op in line:
		dist=int(op.strip("UDRL"))
		if op[0] == "R":
			for i in range(0,dist):
				x+=1
				line_pos[-1].add("{}|{}".format(x,y))
		elif op[0] == "U":
			for i in range(0,dist):
				y+=1
				line_pos[-1].add("{}|{}".format(x,y))
		elif op[0] == "D":
			for i in range(0,dist):
				y=y-1
				line_pos[-1].add("{}|{}".format(x,y))
		elif op[0] == "L":
			for i in range(0,dist):
				x=x-1
				line_pos[-1].add("{}|{}".format(x,y))

closest=float("inf")
for cross in line_pos[0].intersection(line_pos[1]):
	print(cross)
	x=abs(int(cross.split("|")[0]))
	y=abs(int(cross.split("|")[1]))	
	
	if x+y < closest:
		closest=x+y

print(closest)
