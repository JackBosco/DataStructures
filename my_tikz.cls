\documentclass{standalone}
\ProvidesClass{my_tikz}[2022/11/28 My custom tikz class]
\RequirePackage{tikz}
\usepackage{tikz}
\usetikzlibrary{automata, positioning, arrows}
\tikzset{
        ->, % makes the edges directed
        >=stealth, % makes the arrow heads bold
        node distance=1.5cm, % specifies the minimum distance between two nodes. Change if necessary.
        every state/.style={thick, fill=gray!10, minimum size = 0.1mm}, % sets the properties for each ’state’ node
        initial text=root, % sets the text that appears on the start arrow
    }