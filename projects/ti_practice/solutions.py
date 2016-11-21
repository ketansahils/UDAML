from helper import Edge, MST, search_helper, Stack, Node

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
		checker(i-1,i)

	if not sum(longest) == n - 1:
		for j in range(1,n-1):
			checker(j-1,j+1)
	return a[longest[0]:longest[1]+1]


	
def question3(d):
	N = len(d)
	lookup = {}
	rev = [None] * N
	edges = []
	index = 0
	for k in d.keys():
		lookup[k] = index
		rev[index] = k
		index += 1

	index = 0
	
	for k,v in d.iteritems():
		for tup in v:
			edges.append(Edge(lookup[k],lookup[tup[0]],tup[1]))
			index += 1

	obj = MST(edges,N)
	return obj.createMST(rev)


def question4(T, r, n1, n2):
	if n1 > n2:
		smaller = n2
		larger = n1
	else:
		smaller = n1
		larger = n2

	return search_helper(T,r,smaller,larger)

def question5(ll,m):
	s = Stack(ll.data)
	while ll.next:
		s.push(ll.next.data)
		ll = ll.next
	k = 0
	while k != m:
		answer = s.pop()
		k += 1
	return answer.data


print "############## QUESTION 1 ##############"
s1 = "Udacity ketaan"
t = "ekyt"

t1 = ""
t2 = None
t3 = "ana"
t4 = "ektanu"

T = [t,t1,t2,t3,t4]
for item in T:
	print question1(s1,item)

# True
# True
# True
# True
# False
print "########################################"
print
print "############## QUESTION 2 ##############"
print question2('nurses run')
# nurses run
print question2('asma da m ')
# ma da m
print question2('asanokakontog otnoklol')
# kontog otnok
print "########################################"
print
print "############## QUESTION 3 ##############"
l = ['A','B','C','D','E','F','G','H']
d = {}
for item in l:
	d[item] = []
l2 = [('E','F',0.35),('B','C',0.36),('E','H',0.37),\
		('A','E',0.38),('G','C',0.40),('D','G',0.52),\
		('G','A',0.58),('G','E',0.93),('C','H',0.34),\
		('B','F',0.32),('B','D',0.29),('F','H',0.28),\
		('A','C',0.26),('B','H',0.19),('C','D',0.17),('A','H',0.16)]
for item in l2:
	d[item[0]].append((item[1],item[2]))
	d[item[1]].append((item[0],item[2]))

from pprint import pprint
pprint(question3(d))

# {'A': [('H', 0.16), ('C', 0.26)], \
# 'C': [('D', 0.17), ('A', 0.26), ('G', 0.4)], \
# 'B': [('H', 0.19)], \
# 'E': [('F', 0.35)], \
# 'D': [('C', 0.17)], \
# 'G': [('C', 0.4)], \
# 'F': [('H', 0.28), ('E', 0.35)], \
# 'H': [('A', 0.16), ('B', 0.19), ('F', 0.28)]}
print "########################################"

print
print "############## QUESTION 4 ##############"
print "Answer to Test question is", question4([[0, 1, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[1, 0, 0, 0, 1],[0, 0, 0, 0, 0]],3,1,4)
# Answer to Test question is 3

# Another tree that looks like:
#        5
#      /   \
#     2     9
#    / \   / \
#    0 3   8 10
#         /
#        6
#         \
#          7

tree = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
		[1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], \
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0], \
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], \
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
		[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], \
		[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], \
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print "Answer with two nodes 5 and 9 should be 5:",(question4(tree,5,5,9) == 5)
print "Answer with two nodes 2 and 9 should be 5:",(question4(tree,5,2,9) == 5)
print "Answer with two nodes 2 and 3 should be 2:",(question4(tree,5,3,2) == 2)
print "Answer with two nodes 0 and 3 should be 2:",(question4(tree,5,3,0) == 2)
print "Answer with two nodes 3 and 7 should be 5:",(question4(tree,5,3,7) == 5)
print "Answer with two nodes 6 and 10 should be 9:",(question4(tree,5,6,10) == 9)
# True
# True
# True
# True
# True
# True
# True
# True
print "########################################"

print
print "############## QUESTION 5 ##############"
# consider a linked list 5,4,5,6,7,3,1,7

for i,item in enumerate([5,4,5,6,7,3,1,7]):
	if i == 0:
		ist = Node(item)
		last = ist
	else:
		newLast = Node(item)
		last.next = newLast
		last = newLast

print "First element from last:",question5(ist,1)
print "Second element from last:",question5(ist,2)
print "Third element from last:",question5(ist,3)
print "Fourth element from last:",question5(ist,4)
print "Fifth element from last:",question5(ist,5)
# First element from last: 7
# Second element from last: 1
# Third element from last: 3
# Fourth element from last: 7
# Fifth element from last: 6
print "########################################"
