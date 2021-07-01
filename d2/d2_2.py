import sys
import copy

input=[]
for line in open(sys.argv[1]):
	input.append(line.strip())

input_list=",".join(input).split(",")


backup_input_list=copy.deepcopy(input_list)
for i in range(0,100):
	for j in range(0,100):
		input_list=copy.deepcopy(backup_input_list)

		start=0
		end=4

		input_list[1]=i
		input_list[2]=j
			
		while True:
	
			#if start > len(input_list) -1:
			#	break
			if int(input_list[start]) == 99:
				break
			program=input_list[start:end]
			if start == 0:
				print(program)

			if int(input_list[start]) == 1:
				input_list[ int(program[-1])  ]= int( input_list[int(program[1])] ) +int(input_list[int(program[2])])
	
			elif int(input_list[start]) == 2:
				input_list[ int(program[-1])  ]= int( input_list[int(program[1])] ) *int(input_list[int(program[2])])

			start=start+4
			end=end+4


		#print(input_list[0])
		if input_list[0] == 19690720:
			#print("hej")
			print(100*i+j)
			quit()
