def question1(s='',t=''):
	text = s.split(' ') if s is not None else ['']
	pat = t.split(' ') if t is not None else ['']
	s = str.lower(''.join(text))
	t = str.lower(''.join(pat))
	counter = 0
	arr = [0] * 26

	for char in t:
		if ord(char) > 122 or ord(char) < 97:
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

def question2(a):
	n = len(a)
	longest = [0,0]

	def checker(x,y):
		temp = [0,0]
		while x >= 0 and y < n:
			#print "Comparing",a[x],"and",a[y]
			#print "temp",a[temp[0]:temp[1]+1]
			if not a[x].isalpha():
				x = x-1
			elif not a[y].isalpha():
				y = y+1
			elif a[x] == a[y]:
				temp[0] = x
				temp[1] = y
				x,y = x-1, y+1
			else:
				break
		if temp[1] - temp[0] > longest[1] - longest[0]:
			longest[0], longest[1] = temp[0], temp[1]
		return

	for i in range(1,n):
		#print "i:",i,"array:",a[longest[0]:longest[1]+1]
		checker(i-1,i)

	if not sum(longest) == n - 1:
		#print "2nd loop"
		for j in range(1,n-1):
			#print "j:",j,"array:",a[longest[0]:longest[1]+1]
			checker(j-1,j+1)
	return a[longest[0]:longest[1]+1]


	
def question3():
	pass

def question4():
	pass

def question5():
	pass

############## QUESTION 1 ##############
# s1 = "Udacity ketaan"
# t = "ekyt"
# 
# t1 = ""
# t2 = None
# t3 = "ana"
# t4 = "ektanu"
# 
# T = [t,t1,t2,t3,t4]
# for item in T:
# 	print question1(s1,item)

# True
# True
# True
# True
# False
########################################

############## QUESTION 2 ##############
print question2('nurses run')
# nurses run
print question2('asma da m ')
# ma da m