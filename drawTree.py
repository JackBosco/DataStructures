from typing import List, AnyStr
from numpy import arange
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
            #print(str([(p.getVal(), getTag[p]) for p in parentLevel]), end='')
            #input()
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
            parentLevel = childLevel.copy()
            childLevel.clear()
            level += 1
        
        parentLevel = [head]
        curLev = 1
        while any([n is not None for n in parentLevel]):
            sibNum = 0
            for p in parentLevel:     
                if p and findParent[p]:
                    spaceRange = 2**(level - curLev)
                    siblings = findParent[p].getChildren()
                    numSiblings = 1 if len(siblings) == 1 else len(siblings) - 1
                    sibPos = [i for i in arange(-spaceRange/2.0, spaceRange/2.0+1, spaceRange/(numSiblings))]
                    ret += '\\node[state'
                    ret += ', below of=' + str(getTag[findParent[p]][0]) + '-' + str(getTag[findParent[p]][1])
                    ret += ', xshift='+ str(sibPos[sibNum]) +'mm*\\nodespace'
                    ret += '] ('+ str(getTag[p][0]) + '-' + str(getTag[p][1]) + ') {' + str(p.getVal()) + '};\n'
                    #draw the edges
                    grandpa = findParent[p]
                    ret += '\\draw'
                    ret += '(' + str(getTag[grandpa][0]) + '-' + str(getTag[grandpa][1]) + ')' + \
                    'edge[below] node{$ $} (' + str(getTag[p][0]) + '-' + str(getTag[p][1]) +');\n'
                    sibNum = (sibNum + 1) % (numSiblings + 1)
                else:
                    ret += '\\node[state, initial] (0-0) {' + head.getVal() + '};\n'
                if p:
                    childLevel += p.getChildren()
                
            parentLevel = childLevel.copy()
            childLevel.clear()
            curLev += 1
            
        ret += '\\end{tikzpicture}\n' + \
        '\\end{document}'
        ret = ret[:57] + '\\newcommand{\\numLevels}{'+ str(level)+'}\n' + ret[57:]
        return ret
        
def main():
    # from tree import BST
    # lst = [5, 7, 8, 2, 3, 4, 1, 0 ,443, 5, 6, 7, 2]
    # myTree = BST(lst)
    # print(myTree)
    from trie import Trie
    myTree = Trie()
    myTree.insert('ok')
    myTree.insert('on')
    myTree.insert('oklahoma')
    myTree.insert('okanawa')
    myTree.insert('optimism')
    dt = drawTree
    print(dt.run(myTree.root))


if __name__ == '__main__':
    main()