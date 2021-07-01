import sys
input=[]
for line in open(sys.argv[1]):
	input.append(line.strip())

input_list=",".join(input).split(",")

start=0
end=4

input_list[1]=12
input_list[2]=2

while True:
	
	start=start+4
	end=end+4
	if int(input_list[start]) == 99:
		break

	program=input_list[start:end]
	if int(input_list[start]) == 1:
		input_list[ int(program[-1])  ]= int( input_list[int(program[1])] ) +int(input_list[int(program[2])])
	
	elif int(input_list[start]) == 2:
		input_list[ int(program[-1])  ]= int( input_list[int(program[1])] ) *int(input_list[int(program[2])])


