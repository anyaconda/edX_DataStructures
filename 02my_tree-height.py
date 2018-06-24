# python3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# submission #6 addendum
#   only looking at leaf nodes - less memory but still time limit exceeded
#   switched from list to array - more memory and more time than previous
#   (not tracking ancestors)


import sys, threading
import numpy as np
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


#define Tree class: n is number of nodes, parent is the index of parent node
class Tree:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        # allocate arrays
        self.idx = np.arange(self.n)
        self.parent_idx = np.array(self.parent)


    def leaf_idx(self):
        # find the set difference
        leaf_idx = np.setdiff1d(self.idx, self.parent_idx)
        #print('tree leaves: ', leaf_idx)

        return leaf_idx

    def set_level(self):
        self.level = 1

    # traverse up each node - recursive
    def traverseNodeUp(self, n_idx):
        node_parent_idx = self.parent_idx[n_idx]

        if node_parent_idx!=-1:
            self.level += 1
            self.traverseNodeUp(node_parent_idx)

        return self.level  # len(ancestors)

    # def compute_height(self):
    #     # Replace this code with a faster implementation
    #     maxHeight = 0
    #     for vertex in range(self.n):
    #         height = 0
    #         i = vertex
    #         while i != -1:
    #             height += 1
    #             i = self.parent_idx[i]
    #         maxHeight = max(maxHeight, height);
    #     return maxHeight;

def main():
    myTree = Tree()
    myTree.read()
    # print(myTree.compute_height())

    # find leaves only
    tree_leaves = myTree.leaf_idx()

    max_height = 0

    for n_idx in tree_leaves:
        # print('arr ', node)
        myTree.set_level()
        height = myTree.traverseNodeUp(n_idx)
        # print(height)
        max_height = max(height, max_height)

    print(max_height)


threading.Thread(target=main).start()

