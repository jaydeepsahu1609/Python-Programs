str1 =  input("Enter a string : ") 
dict  = {} 
for  n  in  str1:     
	keys =  dict.keys() 
	if  n  in  keys: 
		dict[n] +=  1 
	else: 
		dict[n] =  1 
print(dict)