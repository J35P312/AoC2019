pwd=range(278384,824796)

n_ok=0
for i in pwd:
	ok=True
	str_code=str(i)
	double=False
	for n in range(0,len(str_code)-1):
		if int(str_code[n]) > int(str_code[n+1]):
			ok=False

		if n > 0 and n < len(str_code)-2:
			if str_code[n] != str_code[n-1] and str_code[n] == str_code[n+1] and str_code[n+1] != str_code[n+2]:
				double=True


	if str_code[-1] == str_code[-2] and str_code[-2] != str_code[-3]:
		double=True
	if str_code[0] == str_code[1] and str_code[1] != str_code[2]:
		double=True





	if not double:
		ok=False
	if ok:
		n_ok+=1

print(n_ok)
