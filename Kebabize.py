from string import ascii_letters
capital_letters = ascii_letters[26:]

def kebabize(word):
	outword = ''
	count = 0
	for char in word:
		if char not in capital_letters:
			outword += char
		elif char in capital_letters:
			outword += '-' + char.lower()
	return outword
	
print(kebabize(input("Give word : ")))