def dec2bin(decimal):
	binary = []
	while(decimal>0):
		rem = decimal%2
		binary.append(str(rem))
		decimal = int(decimal/2)
	binary = binary[::-1]
	binary = ''.join(binary)
	return binary

#:::::::::::::::::::::
def bin2dec(binary):
	decimal = 0
	j = 0
	for i in range(len(binary)-1, -1, -1):
		if binary[i] == '1' or binary[i] =='0':
			if binary[i] == '1':
				decimal = decimal + 2**j
			j += 1
		else:
			print("Invalid input")
			exit(0)
	else:
		return decimal	
#::::::::::::::::::::::::::::::::::::
def take_input():
	b1 = int(input("Enter first number : "))
	b2 = int(input("Enter second number : "))
	return b1, b2

def adder(b1, b2):
	if(len(b1) > len(b2)):
		diff = len(b1) - len(b2)
		b2 = '0'*diff + b2
	elif(len(b1) < len(b2)):
		diff = len(b2) - len(b1)
		b1 = '0'*diff + b1
	else:
		pass
	sum = ''
	carry = 0
	for i in range(len(b1)-1, -1, -1):
		if b1[i] == '0' and b2[i] == '0':
			if (carry):
				sum = sum + '1'
				carry = 0
			else:
				sum = sum + '0'
		elif (b1[i] == '1' and b2[i] == '0'):
			if(carry):
				sum = sum + '0'
				carry = 1
			else:
				sum = sum + '1'
		elif (b1[i] == '0' and b2[i] == '1'):
			if(carry):
				sum = sum + '0'
				carry = 1
			else:
				sum = sum + '1'
		elif(b1[i] == '1' and b2[i] == '1'):
			if(carry):
				sum = sum + '1'
				carry = 1
			else:
				sum = sum + '0'
				carry = carry + 1
	if(carry):
		sum = sum + '1'
	return sum[::-1]

def calculate():
	b1, b2 = take_input()
	print(b1, b2)
	b1 = dec2bin(b1)
	b2 = dec2bin(b2)
	print(b1, b2)
	sum = adder(b1, b2)
	print(sum)
	sum = bin2dec(sum)
	print("Sum is : ", sum)

calculate()
	
