#password strength checker simulator
#DEVELOPED BY JAYDEEP SAHU

'''YOUR PASSWORD IS S
password = input("Enter your password : ")

length_points = 0
special_char = 0
digits_count = 0
 
if(len(password)<=8):
 	length_points += 4
elif 8< len(password)<=12:
 	length_points += 7
elif 12<len(password):
 	length_points += 10
 
 
for i in password:
 	if i in string.punctuation:
 		special_char += 1
 	if i in string.digits:
 		digits_count += 1
 
if special_char==0:
 	special_char_points = 0
elif special_char <=2:
 	special_char_points = 4
elif 2<special_char<=4:
 	special_char_points = 8
elif special_char >4:
 	special_char_points =10
 	
if digits_count ==0:
 	digit_points = 0
elif digits_count <= 2:
 	digit_points = 4
elif 2<digits_count<=4:
 	digit_points = 8
elif digits_count >4:
 	digit_points = 10

print("Digit points : ",digit_points)
print("Length points : ", length_points)
print("Special char points : ", special_char_points)

strength = (digit_points + length_points +special_char_points) / 30 * 100
 
print("Strength of password : {:.2f}%".format(strength))
 