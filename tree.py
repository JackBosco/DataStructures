#Practice the Tree data structure
#Jack Bosco
from drawTree import PrintNode
class Node(PrintNode):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def getChildren(self):
		return [self.left, self.right]

	def getVal(self):
		return str(self.value)

class Queue():
	def __init__(self):
		self.size = 0
		self.head = Node(None)
		self.tail = Node(None)
		self.head.right = self.tail
		self.tail.left = self.head
	def add(self, newVal):
		self.size += 1
		newNode = Node(newVal)
		newNode.right = self.head.right
		self.head = Node(None)
		newNode.right.left = newNode
		self.head.right = newNode
		newNode.left = self.head
		if self.size == 1:
			self.tail.left = newNode
	def pop(self):
		if self.tail.left == self.head:
			#print("Tried to pop from empty queue")
			return
		self.size -= 1
		ret = self.tail.left.value
		self.tail.left = self.tail.left.left
		self.tail.left.right = self.tail
		return ret
	def __len__(self):
		return self.size
		

class BST():
	def __init__(self, values):
		values.sort()
		#make the root
		self.root = None
		#add the nodes in a legal way
		self.makeTree(values)
		
	def addNode(self, value, cur=None):
		if cur is None:
			self.root = Node(value)
			return
		#dfs for the place to put new Node
		#print("DFS to place", value)
		if cur.left is None and value < cur.value:
			cur.left = Node(value)
			return
		elif cur.left is not None and value < cur.value:
			#print("Left on", cur.value)
			self.addNode(value, cur.left)
		elif cur.right is None and value >= cur.value:
			cur.right = Node(value)
			return
		elif cur.right is not None and value >= cur.value:
			#print("Right on", cur.value)
			self.addNode(value, cur.right)
		else:
			print("something went wrong")
			return			

	def makeTree(self, values): #makes the tree using queue
		q = Queue()
		#partion
		def part(lst):
			mid = len(lst)//2
			#print(lst[mid])
			self.addNode(lst[mid], self.root)
			if len(lst) == 1:
				return
			elif len(lst) == 2:
				q.add([lst[1]])
			else:
				q.add(lst[:mid])
				q.add(lst[mid + 1:])
		part(values)
		while len(q) > 0:
			part(q.pop())

	def __repr__(self):
		levels = [[self.root]]
		curLevel = 1
		while any([n.left is not None or n.right is not None for n in levels[curLevel-1]]):
			maxWidth = 2 ** curLevel
			levels.append([])
			for parent in levels[curLevel - 1]:
				for child in [parent.left, parent.right]:
					if child is not None:
						levels[curLevel].append(child)
					else:
						levels[curLevel].append(Node('*'))
			curLevel += 1
		ret = ''
		curLevel -= 1
		spaces = 1
		while curLevel >= 0:
			line = ''
			if curLevel != len(levels) - 1:
				for item in levels[curLevel]:
					line += ' '*(spaces) + '/' + ' '*(spaces) + '\\'
			ret = '\n' + line + ret
			line = ''
			for item in levels[curLevel]:
				line += ' '*(spaces*3//2) + str(item.value) + ' '*spaces
			ret = '\n' + line + ret
			curLevel -= 1
			spaces *=2
		return ret

def main():
	lst = [5, 7, 8, 2, 3, 4, 1, 0]
	myTree = BST(lst)		
	print(myTree)	

if __name__ == '__main__':
	main()
