from typing import List, AnyStr, Type
from numpy import arange
import os
class PrintableTreeNode:
    """
    Allows for a head node of a tree to
    be printed to a PDF
    """
    def getChildren(self) -> List['PrintableTreeNode']['getChildren']:
        """
        With no required parameters aside from self,
        return a list of only PrintableTreeNodes representing the children of this node
        """
        pass
    
    def getVal(self) -> AnyStr['getVal']:
        """
        With no required parameters aside from self,
        return the element inside this node. 
        This element must either be type String, or be convertable to String
        """
        pass
    
    def printToPDF(self, width=2.5):
        """
        Creates the LaTex file in a folder named 'out' 
        in the current working directory
        Width is a factor of the horizontal space between each node
        """
        parentLevel = [self]
        childLevel = []
        getTag = {self : [0, 0]}
        findParent = {self : None}
        youngerSibling = {self : None}
        level = 0
        #first levelorder traversal to 
        #define all the parent, child relations
        while any([n is not None for n in parentLevel]):
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
        #second levelorder traversal to
        #store the LaTex code for the output file in a string named ret
        ret = ''
        parentLevel = [self]
        curLev = 1
        while any([n is not None for n in parentLevel]):
            sibNum = 0
            for p in parentLevel:     
                if p and findParent[p]:
                    siblings = findParent[p].getChildren()
                    numSiblings = 1 if len(siblings) == 1 else len(siblings) - 1
                    spaceRange = (numSiblings+1)**(level - curLev)
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
                    ret += '\\node[state, initial] (0-0) {' + self.getVal() + '};\n'
                if p:
                    childLevel += p.getChildren()
            parentLevel = childLevel.copy()
            childLevel.clear()
            curLev += 1
        ret += '\\end{tikzpicture}\n' + \
            '\\end{document}'
        #ret is now complete
        #create the output file and directory
        fileName = 'drawTree'
        if 'out' not in os.listdir('.'):
            os.mkdir('out')
        files = set(os.listdir('.'+os.sep+'out'+os.sep))
        n = ''
        while fileName + n + '.tex' in files:
            if len(n) == 0:
                n = '1'
            else:
                n = str(int(n) + 1)
        fileName += n + '.tex'
        f = open('out' + os.sep + fileName, 'w')
        f.write('\LoadClass{my_tikz}\n' + \
            '\\newcommand\\nodespace{'+ str(width) +'mm}\n' + \
            '\\begin{document}\n' + \
            '\\begin{tikzpicture}\n' + ret)
        if 'my_tikz.cls' not in os.listdir('.' + os.sep + 'out' + os.sep):
            new = open('my_tikz.cls', 'r').read()
            open('out' + os.sep + 'my_tikz.cls', 'w').write(new)
        print('Output written to ' + str(os.getcwd()) + os.sep + 'out' + os.sep + fileName)
        return True
        
def main():
    print("Running main() from drawTree.py")
    width = float(input("Specify width between nodes: "))
    kind = int(input("What kind? "))
    if kind == 1:
        from tree import BST
        #lst = [5, 7, 8, 2, 3, 4, 1, 0 ,443, 5, 6, 7, 2]
        lst = [3, 2, 4]
        myTree = BST(lst)
        myTree.root.printToPDF(width)
    else:
        from trie import Trie
        myTree = Trie()
        myTree.insert('ok')
        myTree.insert('on')
        myTree.insert('oklahoma')
        myTree.insert('okanawa')
        myTree.insert('optimism')
        myTree.root.printToPDF(width)


if __name__ == '__main__':
    main()
