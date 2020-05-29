#CHECKING A PASSWORD VALIDITY
upper= lower= digit= punct = 0
password=input('Enter your password: ')#getting users input
if((len(password)>=6) and (len(password)<=16)):#checking the password lenght
	if((any(c.islower() for c in password))==True):#Looking for lower case letters
		lower=lower+1
	if((any(c.isupper() for c in password))==True):#looking for upper case letters
		upper=upper+1 
	if((any(c.isdigit() for c in password))==True):#looking for numbers
		digit=digit+1
	for c in password:#punctuation marks
		if(c=='.'or c==',' or c==';' or c==':' or c=='-' or c=='_' or c=='?' or c=='!'):
			punct=punct+1
if(lower>=1 and upper>=1 and digit>=1 and punct>=1):#final condition
	print("Valid password!:)")
else: 
    print("Invalid Password:c")