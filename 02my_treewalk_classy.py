#python 3
"""
Description: edX UCSanDiegoX: ALGS201x PA#1
Problem 2: Walk the tree prep - manually walk a tree with 3 levels or 6 levels
6/12/2018
    add class Node (as hinted by assignment)
    add recursion
"""
import numpy as np
import sys
sys.setrecursionlimit(10**1) # max depth of recursion
import time #to track time

class Node:

    #--constructor
    def __init__(self, label, parent):
        self._label = label
        self._parent = parent
        self._child = []
        self._root = parent == -1
        #self._seen = False

    # --setter functions
    def add_child(self, c):
        self._child.append(c)

    #traverse up each node ($actodo: keep track of seen nodes
    def traverseUp(self, this_nodes):
        me = self
        done = False

        while not done:
            if me._root:
                done = True
            else:
                ancestors.append(self._parent)
                me = this_nodes[ancestors[len(ancestors) - 1]]
                me.traverseUp(this_nodes)

            return ancestors

#define Tree class: n is number of nodes, parent is the index of parent node
class Tree:

    def read(self):
        #temp = '8 8 5 6 7 3 1 6 -1 5'
        #self.parent = list(map(int, temp.split()))
        # print('my lentth', len(self.parent))

        self.n = 5 #int(sys.stdin.readline())
        self.parent = [4, -1, 4, 1, 1] #[-1, 0, 4, 0, 3] #list(map(int, sys.stdin.readline().split()))


    def build(self):
        # allocate Nodes array
        nodes = list(range(self.n))
        for i in range(0, len(nodes)):
            nodes[i] = Node(i, self.parent[i])

        # assign kids based on parents
        for child_idx in range(0, len(nodes)):
            parent_idx = nodes[child_idx]._parent
            # print (parent_idx)
            if parent_idx == -1:
                root_idx = child_idx
            else:
                nodes[parent_idx].add_child(nodes[child_idx])

        #print ('Tree built')
        return nodes

    def get_leaf_idx(self):
        # allocate Nodes array
        leaf_nodes = []
        leaf_nodes = [elem for elem in range(0,self.n) if elem not in self.parent]

        print("leaf idx ", leaf_nodes)
        return leaf_nodes

    def compute_height_was(self):
        # Replace this code with a faster implementation
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height)
        return maxHeight

    def compute_height(self):
        height = 0

        nodes = self.build()
        leaf_idx = self.get_leaf_idx()
        leaf_nodes = []
        leaf_nodes = [ elem for elem in nodes if elem._label in leaf_idx ]
        print('leaf nodes ', leaf_nodes)

        for node in leaf_nodes:
            print ('leaf node ', node._label)
            ancestors.clear()
            ancestors.append(node._label)
            node.traverseUp(nodes)

            if len(ancestors) > height:
                height = len(ancestors)
        return height



#---- MAIN --------
start_time = time.time()

global ancestors
ancestors = []

#read an incoming tree
myTree = Tree()
myTree.read()
#print(myTree.parent)
#was print(tree.compute_height())

# traverseUp with class Node
print ('\nTraverse - using recursion')
print(myTree.compute_height())

#track time
elapsed_time = time.time() - start_time
print('done in ', elapsed_time)


"""
output

/Users/Amigo/anaconda3/bin/python /Users/Amigo/PycharmProjects/edX_DataStructures/02my_treewalk_classy.py
10  nodes
[8, 8, 5, 6, 7, 3, 1, 6, -1, 5]

Traverse - using recursion
---
not root
[0, 8]
---
not root
[1, 8]
---
not root
[2, 5, 3, 6, 1, 8]
---
not root
[3, 6, 1, 8]
---
not root
[4, 7, 6, 1, 8]
---
not root
[5, 3, 6, 1, 8]
---
not root
[6, 1, 8]
---
not root
[7, 6, 1, 8]
---
root
[8]
---
not root
[9, 5, 3, 6, 1, 8]
6

Process finished with exit code 0
"""


