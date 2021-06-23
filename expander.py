def expander(num):
	expanded = []
	rem = 0
	n = 0
	while(num>0):
		rem = num % 10
		for _ in range(n):
			rem = rem*10
		n += 1
		expanded.append(str(rem))
		num = int(num/10)
	expanded = " + ".join(expanded[::-1])
	return expanded

print(expander(int(input("Enter number : "))))