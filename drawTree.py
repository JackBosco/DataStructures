from typing import List, AnyStr

class PrintNode:
    #returns a list of all children
    def getChildren(self) -> List:
        pass
    def getVal() -> AnyStr:
        pass

class drawTree:
    def run(head:PrintNode):
        ret = '\LoadClass{my_tikz}\n' + \
        '\\begin{document}\n' + \
        '\\begin{tikzpicture}\n'
        
        parentLevel = [head]
        childLevel = []
        #childLevel = List(Node)
        tag = [0, 0]
        getTag = {head : [0, 0]}
        findParent = {head : None}
        youngerSibling = {head : None}
        level = 0
        while any([n is not None for n in parentLevel]):
            print(str([(p.getVal(), getTag[p]) for p in parentLevel]), end='')
            input()
            isFirstInLevel = True
            for p in parentLevel:
                kids = p.getChildren()
                for child in range(len(kids)):
                    if kids[child]:
                        findParent[kids[child]] = p
                        if child == 0 or not kids[child-1]:
                            youngerSibling[kids[child]] = None
                            getTag[kids[child]] = [getTag[p][0] + 1, len(childLevel)]
                        else:
                            youngerSibling[kids[child]] = kids[child - 1]
                            getTag[kids[child]] = [getTag[p][0] + 1, child + getTag[kids[child - 1]][1]]
                        childLevel.append(kids[child])
                        
                #remove non init DONE
                #only fist in a level is below DONE
                #first sibling shifted left 1 cm
                #edges
                if findParent[p]:
                    ret += '\\node[state'
                    if isFirstInLevel:
                        isFirstInLevel = False
                        ret += ', below of=' + str(getTag[findParent[p]][0]) + '-' + str(getTag[findParent[p]][1])
                        ret += ', xshift=-1cm'
                    #if youngerSibling[p]:
                    else:
                        ret += ', right of=' + str(getTag[p][0]) + '-' + str(getTag[p][1] - 1)
                        if youngerSibling[p]:
                            ret += ', xshift=1cm'
                    ret += '] ('+ str(getTag[p][0]) + '-' + str(getTag[p][1]) + ') {' + str(p.getVal()) + '};\n'
                else:
                    ret += '\\node[state, initial] (0-0) {' + head.getVal() + '};\n'
                    
            #draw the edges
            ret += '\\draw'
            for child in childLevel:
                if child and findParent[child]:
                    p = findParent[child]
                    ret += '(' + str(getTag[p][0]) + '-' + str(getTag[p][1]) + ') \
                    edge[below] node{$ $} (' + str(getTag[child][0]) + '-' + str(getTag[child][1]) +')\n'
            ret = ret[:-1] + ';' 
            parentLevel = childLevel.copy()
            childLevel.clear()
            level += 1
            
        ret += '\\end{tikzpicture}\n' + \
        '\\end{document}'
        return ret
            
    def levelOrder():
        return 
	    # levels = [[self.root]]
		# curLevel = 1
		# while any([n.left is not None or n.right is not None for n in levels[curLevel-1]]):
		# 	maxWidth = 2 ** curLevel
		# 	levels.append([])
		# 	for parent in levels[curLevel - 1]:
		# 		for child in [parent.left, parent.right]:
		# 			if child is not None:
		# 				levels[curLevel].append(child)
		# 			else:
		# 				levels[curLevel].append(Node('*'))
		# 	curLevel += 1
        #     ret = ''
        #     curLevel -= 1
        #     spaces = 1
        #     while curLevel >= 0:
        #         line = ''
        #         if curLevel != len(levels) - 1:
        #             for item in levels[curLevel]:
        #                 line += ' '*(spaces) + '/' + ' '*(spaces) + '\\'
        #         ret = '\n' + line + ret
        #         line = ''
        #         for item in levels[curLevel]:
        #             line += ' '*(spaces*3//2) + str(item.value) + ' '*spaces
        #         ret = '\n' + line + ret
        #         curLevel -= 1
        #         spaces *=2
		#     return ret
        
def main():
    from tree import BST
    lst = [5, 7, 8, 2, 3, 4, 1, 0]
    myTree = BST(lst)
    dt = drawTree
    print(dt.run(myTree.root))


if __name__ == '__main__':
    main()