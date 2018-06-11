#python 3
"""
Description: edX UCSanDiegoX: ALGS201x PA#1
Problem 2: Walk the tree prep - manually walk a tree with 3 levels
"""
import numpy as np
import sys
sys.setrecursionlimit(10**3) # max depth of recursion

#define Tree class: n is number of nodes, parent is the index of parent node
class Tree:
    def read(self):
        self.n = 5 #int(sys.stdin.readline())
        self.parent = [4, -1, 4, 1, 1] #list(map(int, sys.stdin.readline().split()))

#instantiate a tree
myTree = Tree()
myTree.read()
print(myTree.n)
print(myTree.parent)


nodes = myTree.parent
#check if nodes is empty
if not nodes:
    print ('empty')
else:
    #check if root exist
    if -1 in nodes:
        print ('root exists')
        #find root node
        #root = nodes.index(-1)
        root_idx=nodes.index(min(nodes))

    #check if root has children
    if root_idx in nodes:
        #comprehension to get matching items
        root_child = [x for x in nodes if x == root_idx]
        #comprehension to get indices of matching items
        root_child_idx = [i for i, x in enumerate(nodes) if x == root_idx]
        print (root_child_idx)

        #check if children have children
        for item in root_child_idx:
            print (item)
            if item in nodes:
                root_child2_idx = [i for i,x in enumerate(nodes) if x==item]
                print(root_child2_idx)

                #check if these children have children
                for subitem in root_child2_idx:
                    print(subitem)
                    if subitem in nodes:
                        print('yes more descendants')
                    else:
                        print('no more descendants')
                        print('done, with this manual walk')

            else:
                print ('nope')


