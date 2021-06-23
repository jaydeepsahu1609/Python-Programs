def hangman(actualword, guessed, word):
    if guessed in actualword:
        index = actualword.index(guessed)
        word[index] = guessed
    print(' '.join(word), end='\n')
    return word
    
import random

def take_word():
	
	categories = {"sports":['cricket', 'tennis', 'football', 'carrom', 'boxing'], "countries":['India', 'srilanka', 'china', 'australia', 'brazil', 'nepal'], "continent":['asia', 'australia', 'europe', 'afrika', 'antartika'], "oceans":['pecific', 'arctic', 'indian', 'atlantic']}
	category = random.choice(list(categories.keys()))
	print("Category : ", category)
	actualword = str(categories[category][int(random.randrange(len(categories[category])))])
	word = actualword[:]
	jumble = ""
	while word:
		index = random.randrange(len(word))
		jumble = jumble + word[index]
		word = word[:index] + word[index+1:]
	print("Hint : ", jumble)
	actualword = [char for char in actualword]
	word = ('_ '*len(actualword)).strip()
	return actualword, word.split()
        
def guess(guessed_list):
    i = True
    while(i):
        guess = input("Guess a letter : ")
        if len(guess)>1 and guess!="exit" :
            print("Give a single letter.")
        elif guess == "exit":
            print("You lost.")
            quit()
        else:
            if guess in guessed_list:
                print("'{}' has already been guessed.".format(guess))
            else:
                guessed_list.append(guess)
                return guess

def intro():
	print("="*18, "HANGMAN GAME", "="*18)
	choice = int(input("Do you want to see the rules? Press 1 else 0 : "))
	if(choice):
		print("""
    Rules:
        * Player-1 gives a word,   and  Player-2 has 
          to guess the word in minimum of 5 attempts.
        * For each  correct  guess  Player-2 gets 10 
          points and with each wrong guess  Player-2 
          loses 5 points and 1 life.
        * Player-2 can only give  a single letter to 
          guess. A complete word is not allowed.
        * Player-2 can type 'exit'  anytime  to exit 
          the game.
        * If Player-2  guesses the correct word with
          atleast  1  life  remaining,  he / she  is 
          declared as the winner of this game.

        Play the Game. Good Luck.

    """)

def play():
    actualword, word = take_word()
    win = False
    life = 5
    score = 0
    guessed_list = []
    while(life >0 ):
        print("\nLife : {}\tScore : {}".format(life, score), end="\n\n")
        guessed = guess(guessed_list)
        prev_word = word[:]
        word = hangman(actualword, guessed, word[:])
        if(word == prev_word):
            print("Guessed Wrong !! ")
            life -= 1
            score -= 5
        else:
            score += 10
        if word == actualword:
            print("Guessed the word correctly. You Win.\nYour Score is :", score)
            break
        print('_'*20)
    if(not life):
        print("No life. You lost. Better luck Next time.")

play()        

