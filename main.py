#-*- coding: utf8 -*-
import os
def Text_Clean(text):
	ans = ""
	for letter in text:
		if letter.isalpha():
			ans = ans + letter
	return ans

def Show_Ans(text):
	print "Ciphertext is          :"+text
	return

def Double_Track():
	plain_text = raw_input( "Please input plain text:" )
	plain_text = Text_Clean (plain_text)
	ans = ""
	length = len(plain_text)
	index=0
	while index<length:
		ans=ans+plain_text[index]
		index=index+2
	index=1
	while index<length:
		ans=ans+plain_text[index]
		index=index+2
	Show_Ans(ans)
	return

def my_cmp(x,y):
	return cmp(x[0],y[0])

def Key_Controller_Sequence():
	plain_text = raw_input("Please input plain text:")
	plain_text=Text_Clean(plain_text)
	key = raw_input("Please input key:")
	key=Text_Clean(key)
	plength=len(plain_text)
	klength=len(key)
	ans=""
	if plength>=klength:
		mod=plength%klength
		plength=plength-mod
		mat=[]
		for index in xrange(0,klength):
			mat.append((key[index],[]))
		for index in xrange(0,plength):
			mat[index%klength][1].append(plain_text[index])
		mat.sort(my_cmp)
		for index in xrange(0,plength/klength):
			for k in xrange(0,klength):
				ans=ans+mat[k][1][index]
	Show_Ans(ans)
	return


num_selections = 2
num = 0
while True:
	print "Please select one encryption algorithm:"
	print "1.Double track encryption"
	print "2.Key controlled sequence encryption"
	num = int(raw_input())
	if num < 1 or num > num_selections:
		print "Input error!"
		continue
	else:
		break
if num==1:
	Double_Track()
elif num==2:
	Key_Controller_Sequence()
