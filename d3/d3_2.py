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
intersections=line_pos[0].intersection(line_pos[1])
print(intersections)
intersection_list=[]
for line in lines:
	x=0;y=0
	line_pos.append(set([]))
	total_dist=0
	intersection_list.append({})

	for op in line:
		dist=int(op.strip("UDRL"))
		if op[0] == "R":
			for i in range(0,dist):
				total_dist+=1
				x+=1
				line_pos[-1].add("{}|{}".format(x,y))

				if "{}|{}".format(x,y) in intersections  and not "{}|{}".format(x,y) in intersection_list[-1]:
					intersection_list[-1]["{}|{}".format(x,y)]=total_dist

		elif op[0] == "U":
			for i in range(0,dist):
				total_dist+=1
				y+=1
				line_pos[-1].add("{}|{}".format(x,y))

				if "{}|{}".format(x,y) in intersections and not "{}|{}".format(x,y) in intersection_list[-1]:
					intersection_list[-1]["{}|{}".format(x,y)]=total_dist


		elif op[0] == "D":
			for i in range(0,dist):
				y=y-1
				total_dist+=1
				line_pos[-1].add("{}|{}".format(x,y))

				if "{}|{}".format(x,y) in intersections  and not "{}|{}".format(x,y) in intersection_list[-1]:
					intersection_list[-1]["{}|{}".format(x,y)]=total_dist

		elif op[0] == "L":
			for i in range(0,dist):
				x=x-1
				total_dist+=1
				line_pos[-1].add("{}|{}".format(x,y))

				if "{}|{}".format(x,y) in intersections  and not "{}|{}".format(x,y) in intersection_list[-1]:
					intersection_list[-1]["{}|{}".format(x,y)]=total_dist



print(intersection_list)
dist_to_cross=[]
for intersection in intersections:
	dist_to_cross.append(intersection_list[0][intersection]+intersection_list[1][intersection])

print(min(dist_to_cross))
