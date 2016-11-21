class MinPQ(object):
	def __init__(self):
		self.N = 0
		self.arr = []

	def insert(self,edge):
		self.arr.append(edge)
		self.N += 1

	def delMin(self):
		if self.N == 0:
			return
		xmin = 0
		for i in range(1,self.N):
			if self.arr[i] < self.arr[xmin]:
				xmin = i
		self.exch(xmin,self.N-1,self.arr)
		k = self.arr[self.N-1]
		del self.arr[self.N-1]
		self.N -= 1
		return k

	def exch(self,i,j,arr):
		arr[i], arr[j] = arr[j], arr[i]


class Edge(object):
	def __init__(self,v,w,weight):
		self.v = v
		self.w = w
		self.weight = weight

	def other(self,v):
		return w

	def __lt__(self,other):
		return self.weight < other.weight


class MST(object):
	def __init__(self,edges,V):
		self.V = V
		minPQ = MinPQ()
		self.mst = []
		for edge in edges:
			minPQ.insert(edge)

		qu = QuickUnion(V)
		while minPQ.N > 0:
			e = minPQ.delMin()
			v1 = e.v
			v2 = e.w
			if not qu.connected(v1,v2):
				qu.union(v1,v2)
				self.mst.append(e)

	def createMST(self,rev):
		ans = {}
		for i in range(self.V):
			ans[rev[i]] = []

		for edge in self.mst:
			ans[rev[edge.v]].append((rev[edge.w],edge.weight))
			ans[rev[edge.w]].append((rev[edge.v],edge.weight))
		return ans

class QuickUnion(object):
	def __init__(self,N):
		self._N = N
		self._array = [_ for _ in range(N)]

	def root(self,i):
		if self._array[i] == i: return i
		return self.root(self._array[i])

	def rootFlatten(self, p, q):
		while self._array[p] != p:
			temp = p
			p = self._array[p]
			self._array[temp] = q
		return p

	def connected(self,i,j):
		return self.root(i) == self.root(j)

	def union(self,i,j):
		l = self.root(j)
		k = self.rootFlatten(i,l)
		self._array[k] = l

def search_helper(T, parent, smaller, larger):
	if smaller <= parent <= larger:
		return parent
	if parent > larger:
		for i, j in enumerate(T[parent]):
			if j == 1:
				break
	if parent < smaller:
		for i in range(len(T[parent])-1,-1,-1):
			if T[parent][i] == 1:
				break
	parent = i
	return search_helper(T,parent,smaller,larger)

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack(object):
	def __init__(self,val=None):
		self._first = Node(val)
		self._size = 0 if val is None else 1

	def isEmpty(self):
		return self._first == None

	def push(self,val):
		latest = Node(val)
		latest.next = self._first
		self._first = latest
		self._size += 1

	def pop(self):
		if not self.isEmpty():
			popped = self._first
			self._first = self._first.next
			self._size -= 1
			return popped
		return