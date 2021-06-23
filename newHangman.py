import random

categories = {"sports":['cricket', 'tennis', 'football', 'carrom', 'boxing'], "countries":['India', 'srilanka', 'china', 'australia', 'brazil', 'nepal'], "continent":['asia', 'australia', 'europe', 'afrika', 'antartika'], "oceans":['pecific', 'arctic', 'indian', 'atlantic']}

category = random.choice(list(categories.keys()))

correct_word = str(categories[category][int(random.randrange(len(categories[category])))])

word = correct_word[:]
#word = categories[category[random.randrange(len(categories[category]))]]
#print(word)

jumble = ""

while word:
	index = random.randrange(len(word))
	jumble = jumble + word[index]
	word = word[:index] + word[index+1:]

chances = 5
print("Category : ", category)
print("Jumbled word : ", jumble)

while chances:
	print("Chances : ", chances)
	if(correct_word == input("Guess the word : ")):
		print("You won")
		break
	else:
		chances -= 1
if(not(chances)):
	print("You Lost.")

