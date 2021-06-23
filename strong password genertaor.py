#PASSWORD GENERATOR 
#DEVELOPED BY JAYDEEP SAHU

#Generate a 15character long strong password randomly
import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = '0123456789'
punctuation = "@#&*_?"

#selects 5 punctuations, 5 digits and 5 letters randomly
password_punctuation = [random.choice(punctuation) for i in range(5)]
password_digits = [random.choice(digits) for i in range(5)]
password_chars = [random.choice(ascii_letters) for i in range(5)]

#join them to make a single string
password = ''.join(password_digits)  + ''.join(password_punctuation) +  ''.join(password_chars)

#strong password
strong_password =""

#jumble all the letters of password to make it stronger
while password:
  position = random.randrange(len(password))
  strong_password += password[position]
  password = password[:position] + password[(position + 1):]
  
print(strong_password)
#strong password

