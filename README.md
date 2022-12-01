# DataStructures

This module is dedicated to making graphical representations of data structures
taught in CSCI-112 at Washington and Lee University. It uses Python to parse data
structures and returns a new LaTeX document capable of producing a PDF.
You must have a [LaTeX](https://www.latex-project.org/get/) distribution installed
to convert the TeX document into a PDF, or use an online distribution such as [Overleaf](https://www.overleaf.com).

---

## drawTree.py

### Interface PrintableTreeNode

To make a tree drawable, each element in the tree must be an
instance of some Node class implementing the following methods:

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
        
        def getVal(self) -> AnyStr['getVal']:
            """
            With no required parameters aside from self,
            return the element inside this node. 
            This element must either be type String, or be convertable to String
            """

### Method printToPDF

PrintableTreeNode objects inherit the method printToPDF using `self` as the head/root of the tree,
this method completes two levelorder traversals of the tree under `self`. It takes one optional 
parameter `width` specifying the coefficient of the horizontal width between nodes.

    def printToPDF(self, width=2.5):
        """
        Creates the LaTex file in a folder named 'out' 
        in the current working directory
        Width is a factor of the horizontal space between each node
        """
        ...

---

## my_tikz.cls

A class LaTeX document for building the Tikz environment. Don't mess with this unless you know
what you are doing.

## width

You can chage the width within a PDF at __any time__ through the `drawTree.tex` file in the
in the `out` folder. Look for the following in line 2:

>    \newcommand\nodespace{1.0mm}

In this case, changing `1.0` to `2.0` would ***double*** the coefficient.

>    \newcommand\nodespace{2.0mm}

