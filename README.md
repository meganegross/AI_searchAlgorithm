# AI_searchAlgorithm

<p> The purpose of this project is to explore a navigational search problem using artificial intelligence algorithm techniques. The problem involves efficiently navigating from one location in Sydney to another. Twenty different locations are used including parks, schools, and tourist spots. The artificial intelligence technique used is uniform cost search (UCS). UCS is an uninformed search algorithm that works through the search tree by choosing the next node with the lowest cost value associated to it. The secondary technique used is breadth-first search (BFS) - specifically the tree search version. BFS is also an uninformed search algorithm that expands the nodes of the starting node and the subsequent children’s nodes. In other words, it works left to right across all children.
From the two solutions to this problem, it was found that when the problem had locations where the goal node was close to the starting node, BFS had the same path result as UCS with only slightly more iterations. However, when the problem locations were farther path-wise from each other, BFS had exponentially more iterations, and found a solution with a higher cost than the UCS solution. Ultimately, we can draw the conclusion that if it is known to be a small sample space, breadth-first search is a strong option. However, if there are any uncertainties about the node distance, uniform cost search should be used as it uses less iterations and is guaranteed to find a solution with the least cost. Uniform-cost search is recommended for this specific search problem as it is more versatile and can handle the variance in root to goal distances quickly and efficiently.
<br>-------------------------------------------------------------------------------<br>
The notebook, originally made in Google Colaboratory can be found here: <a href=https://github.com/meganegross/repo/AI_searchAlgorithm/project1Problem.ipynb)>Search Algorithm Notebook</a>
