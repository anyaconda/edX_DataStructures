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
    stack =[]

    def __init__(self, label, parent):
        self._label = label
        self._parent = parent
        self._child = []
        #self._level = -1

    #accessor functions
    def get_parent(self):
        return self._parent

    def has_child(self):
        if self.howManyChildren() > 0:
            return True
        else:
            return False

    def howManyChildren(self):
        return len(self._child)

    def get_child(self):
        return self._child

    def traverseNode(self):
        leaf = False
        me = self
        while leaf == False:
            if me.has_child():
                print('me has ', me.howManyChildren())
                me_children = me.get_child()
                for i in range(0, me.howManyChildren()):
                    me = me_children[i]
                    continue
            else:
                leaf = True
                print('me has no kids')

        leaf = True
        return me._label


    #setter functions
    #def add_parent(self, p):
    #    self._parent = p

    def add_child(self, c):
        self._child.append(c)


#define Tree class: n is number of nodes, parent is the index of parent node
class Tree:

    def read(self):
        #temp = '8 8 5 6 7 3 1 6 -1 5'
        #self.parent = list(map(int, temp.split()))
        # print('my lentth', len(self.parent))

        self.n = 5 #int(sys.stdin.readline())
        self.parent = [4, -1, 4, 1, 1] #[-1, 0, 4, 0, 3] #list(map(int, sys.stdin.readline().split()))


    def compute_height(self):
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

#---- MAIN --------
#instantiate a tree
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

#look at kids - manually
print ('\nStart - look at each node and its kids (manually)')
for node in nodes:
    print('---')
    print('Node ', node._label, ' Look at kids: ', node.has_child())

    if node.has_child():
        n_children = node.howManyChildren()
        print('Parent node ', node._label, 'number of kids: ', n_children)
        for i in range(0, n_children):
            kid = node.get_child()[i]
            print ('kid label ', kid._label)

print ('done - look at each node and its kids (manually)')

print ('\nTraverse - using recursion')
print (nodes[1].traverseNode())