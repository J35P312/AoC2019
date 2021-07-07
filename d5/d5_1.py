import sys

def return_value(pos,m,data):
	if m == 1:
		return(pos)
	else:
		return(int(data[pos]))

input=[]
for line in open(sys.argv[1]):
	input.append(line.strip())


input_list=",".join(input).split(",")

start=0
input=1

while True:
	modes=[]
	opcode=input_list[start]
	opstr=str(opcode)

	if len(opstr) > 2:
		if len(str(opcode)) == 2:
			opcode="".join(["000",opstr])
		elif len(str(opcode)) == 3:
			opcode="".join(["00",opstr])
		elif len(str(opcode)) == 4:
			opcode="".join(["0",opstr])

		modes=list(map(int,list(opcode[0:3])))

		opcode=int(opcode[-2:])
	else:
		opcode=int(opcode)
		modes=[0,0,0]

	if opcode == 99:
		break

	elif opcode in [3,4]:
		program=list(map(int,input_list[start:start+2]))
		if opcode == 3:
			input_list[program[1]]=input

		elif opcode == 4:
			print("op4: {}".format( return_value(program[1],modes[-1],input_list)))

		start=start+2

	elif opcode in [1,2]:
		program=list(map(int,input_list[start:start+4]))
		param_1=return_value(program[1],modes[-1],input_list)
		param_2=return_value(program[2],modes[-2],input_list)
	
		if opcode == 1:
			input_list[ int(program[-1])  ]= param_1 + param_2
	
		elif opcode == 2:
			input_list[ int(program[-1])  ]= param_1 * param_2

		start=start+4
	else:
		print(input_list[start])
		print("error")
		quit()

