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

class Node:

    #--constructor
    def __init__(self, label, parent):
        self._label = label
        self._parent = parent
        self._child = []
        self._root = parent == -1

    #--accessor functions
    def get_parent(self):
        return self._parent

    def has_child(self):
        if self.howManyChildren() > 0:
            #node_level += 1
            return True
        else:
            return False

    def howManyChildren(self):
        return len(self._child)

    def get_child(self):
        return self._child


    #--setter functions
    def add_parent(self, p):
        self._parent = p

    def add_child(self, c):
        self._child.append(c)

    def traverseUp(self):
        me = self
        done = False

        while not done:
            if me._root:
                done = True
            else:
                descendants.append(self._parent)
                #print(descendants)
                me = nodes[descendants[len(descendants)-1]]
                me.traverseUp()

            return descendants


#define Tree class: n is number of nodes, parent is the index of parent node
class Tree:

    def read(self):
        temp = '8 8 5 6 7 3 1 6 -1 5'
        self.parent = list(map(int, temp.split()))
        # print('my lentth', len(self.parent))

        self.n = 10 #int(sys.stdin.readline())
        #self.parent = [4, -1, 4, 1, 1] #[-1, 0, 4, 0, 3] #list(map(int, sys.stdin.readline().split()))


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
        for node in nodes:
            descendants = []
            print('---')
            descendants.append(node._label)

            if not node._root:
                print('not root')
            else:
                print('root')
            print(node.traverseUp())

            if len(descendants) > height:
                height = len(descendants)
        return height



#---- MAIN --------
#read an incoming tree
myTree = Tree()
myTree.read()
print(myTree.n, ' nodes')
print(myTree.parent)

#allocate Nodes array
nodes = list(range(myTree.n))
for i in range(0, len(nodes)):
    nodes[i] = Node(i, myTree.parent[i])

#assign kids based on parents
for child_idx in range(0, len(nodes)):
    parent_idx = nodes[child_idx]._parent
    #print (parent_idx)
    if parent_idx == -1:
        root_idx = child_idx
    else:
        nodes[parent_idx].add_child(nodes[child_idx])

#traverse with class
print ('\nTraverse - using recursion')

#compute tree height
height = 0
for node in nodes:
    descendants = []
    print('---')
    descendants.append(node._label)

    if not node._root:
        print('not root')
    else:
        print('root')
    print (node.traverseUp())

    if len(descendants) > height:
        height = len(descendants)

print (height)

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


