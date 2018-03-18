Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
random_list=[]
list_length=20
while len(random_list)<list_length:
	random_list.append(random.randint(0,10))
index=0
count=0
while  index<len (random_list):
	if random_list[index]==9:
		count=count+1
		index=index+1
print random_list
print count	
