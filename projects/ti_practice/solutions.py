def question1(s='',t=''):
	text = s.split(' ')
	pat = t.split(' ')
	s = str.lower(''.join(text))
	t = str.lower(''.join(pat))
	counter = 0
	arr = [0] * 26

	for char in t:
		if 97 <= ord(char) <= 122:
			continue
		index = ord(char) - 97
		arr[index] += 1
	countx = [_ for _ in arr]

	for item in s:
		if counter == len(t):
			break
		if countx[ord(item) - 97] == 0:
			countx = [_ for _ in arr]
			counter = 0
			continue
		counter += 1
		countx[ord(item) - 97] -= 1

	if sum(countx) == 0:
		return True
	return False			

def question2():
	pass
	
def question3():
	pass

def question4():
	pass

def question5():
	pass


s = "Udacity ketan"
t = "ekyt"

print question1(s,t)