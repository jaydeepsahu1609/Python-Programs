# Word Jumble
# 
# The computer picks a random word then "jumbles" it
# The player has to guess the original word
#  
import random
 
# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")          
  
#  pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word
 
# create a jumbled version of the word
jumble =""
 
while word:
  position = random.randrange(len(word))
  jumble += word[position]
  word = word[:position] + word[(position + 1):]
  
# sets score to zero
score = 0
 
# start the game
print(
   """
              Welcome to Word Jumble!
 
 Unscramble the letters to make a word.
 Enter a guess, an X to give up, or type ? and press enter for a hint.
 (Press the enter key at the prompt to quit.)
 
 Try to get the lowest score possible. For each hint, you gain a point.
 See if you can win with no points!
 """
 )
print("The jumble is:", jumble)
guess = input("\nYour guess: ")
guess = guess.lower()
lst = range(len(jumble))
hint_str = '_'*len(jumble)
while True:
 
     
 if guess == correct:
      print("That's it! You guessed it!\n Your score is", score)
      print("\n\nPress the enter key to exit.")
      break
      guess = input("Guess or '?' or 'X': ").lower()
 elif guess == '?':
       i = random.choice(lst)
       print(correct[i], "is the", i+1, "letter.")
       score += 1
       guess = input("Guess or '?' or 'X': ").lower()
       
       
 elif guess == 'x':
       print("Sorry you gave up!")
       break
 else:
       print("Sorry, thats not it. Try again.")
       guess = input("Guess or '?' or 'X': ").lower()