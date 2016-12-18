import hashlib
pw=''
check=False
num=0
def bruteforce(num):
	s=''	
	while num:
		ch = ''
		ch = (num - 1) % 26 + 65
		s = s + chr(ch)
		num = (num) / 26;
	return s

while check == False:
	s = bruteforce(num)
	pw = hashlib.md5(s).hexdigest()
	if pw[28:] == '1337':
		print pw, s
		check = True
	num += 1
