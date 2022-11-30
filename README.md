# DataStructures
This Module is dedicated to making graphical representations of various Data Structures
taught in CSCI-112 at Washington and Lee University.

## drawTree


    class PrintableTreeNode:
        """
        With no required parameters aside from self,
        return a list of only PrintableTreeNodes representing the children of this node
        """
        def getChildren(self) -> List[Type[PrintableTreeNode]]:
            pass

        """
        With no required parameters aside from self,
        return the element inside this node. 
            This element must either be type String, or be convertable to String
        """
        def getVal(self) -> AnyStr:
            pass

"""
Creates the LaTex file in a folder named 'out' 
in the current working directory
Width is a factor of the horizontal space between each node
"""
