import sys
#start position and input value
#run like this:
#python d5_2.py 5 input.txt

start=0
input=int(sys.argv[1])


#return the value of the paramter, or the value stored at the position
def return_value(pos,m,data):
	if m == 1:
		return(pos)
	else:
		return(int(data[pos]))

#find the modes and opcodes
def get_opcode(start,opstr,input_list):
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

	return(modes,opcode)

input_program=[]
#read the input program
for line in open(sys.argv[2]):
	input_program.append(line.strip())


input_list=",".join(input_program).split(",")

while True:

	modes,opcode=get_opcode(start,input_list[start],input_list)

	if opcode == 99:
		break

	#operations that move 4 steps
	elif opcode in [1,2,7,8]:
		program=list(map(int,input_list[start:start+4]))
		param_1=return_value(program[1],modes[-1],input_list)
		param_2=return_value(program[2],modes[-2],input_list)
	
		if opcode == 1:
			input_list[ int(program[-1])  ]= param_1 + param_2
	
		elif opcode == 2:
			input_list[ int(program[-1])  ]= param_1 * param_2


		elif opcode == 7 and param_1 < param_2:
			input_list[ int(program[-1])  ]=1
		elif opcode == 7:
			input_list[ int(program[-1])  ]=0

		elif opcode == 8 and param_1 == param_2:
			input_list[ int(program[-1])  ]=1
		elif opcode == 8:
			input_list[ int(program[-1])  ]=0

		start=start+4

	#operations that move 2 steps
	elif opcode in [3,4]:
		program=list(map(int,input_list[start:start+2]))

		if opcode == 3:
			input_list[program[1]]=input

		elif opcode == 4:
			print("op4: {}".format( return_value(program[1],modes[-1],input_list)))

		start=start+2

	#operations that move 3 steps
	elif opcode in [5,6]:
		program=list(map(int,input_list[start:start+3]))
		param_1=return_value(program[1],modes[-1],input_list)
		param_2=return_value(program[2],modes[-2],input_list)

		if opcode == 5 and param_1 > 0:
			start=param_2

		elif opcode == 6 and param_1 == 0:
			start=param_2
		else:
			start+=3

	else:
		print(input_list[start])
		print("error")
		quit()
