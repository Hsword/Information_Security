#-*- coding: utf8 -*-
import os
def Text_Clean( text ):
	ans = ""
	for letter in text:
		if letter.isalpha():
			ans = ans + letter
	return ans

def Show_Ans( text ):
	print "Ciphertext is:"
	print text
	return

def Double_Track():
	plain_text = raw_input ( "Please input plain text:" )
	plain_text = Text_Clean ( plain_text )
                ans = ""
                length = len ( plain_text )
                for index in [ 0, 1 ]:
                	while index < length:
                		ans = ans +plain_text[index]
                		index = index + 2
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
if num == 1:
	Double_Track()
else if num == 2:
	exit()
