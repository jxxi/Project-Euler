a = 1
b = 2
total = 0
while b <= 4000000:
	if not b % 2:
		total+=b
	a, b = b, a+b
print(total)
