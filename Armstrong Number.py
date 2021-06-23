num1 = input("Give number : ")
num2 = list(map(lambda x: int(x)**len(num1), num1))
if str(sum(num2)) == num1:
	print("Armstrong.")
else:
	print("Not Armstrong.")