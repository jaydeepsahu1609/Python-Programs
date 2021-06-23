def backwardsPrime(prime):
	backwardsPrime = []
	for i in prime:
		if(i>11):
			j = i
			rev = 0
			rem = 0
			while(j>1):
				rem = j%10
				rev = rev*10 + rem
				j = int(j/10) 
			if(i != rev):
				if(isPrime(rev)):
					backwardsPrime.append(i)
	return backwardsPrime
	
def Prime(alist):
	LowLimit = alist[0]
	UppLimit = alist[1]
	prime = []
	for i in range(LowLimit, UppLimit+1):
		if isPrime(i):
			prime.append(i)
	return prime
	
def isPrime(n):
	if n==1:
		return False
	elif n==2:
		return True
	for i in range(2, n):
		if(n%i==0):
			return False
	return True

print(backwardsPrime(Prime([2, 100])))